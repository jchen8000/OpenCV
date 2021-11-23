from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import numpy as np
import cv2
from datetime import datetime
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import KNNHandWrittenDigits


def create_ANN(layers):
    ann = cv2.ml.ANN_MLP_create()
    ann.setLayerSizes(np.array(layers))
    ann.setTrainMethod(cv2.ml.ANN_MLP_BACKPROP)
    ann.setActivationFunction(cv2.ml.ANN_MLP_SIGMOID_SYM)
    ann.setTermCriteria((cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT, 100, 0.0001))
    return ann

def save_model(model, filename):
    print("Save ANN model to ", filename)
    model.save(filename)

def load_model(filename):
    print("Load ANN model from ", filename)
    ann = cv2.ml.ANN_MLP_load(filename)
    return ann

if __name__ == "__main__":
    save_model_name = None
    # load_model_name = None
    load_model_name = "../res/mnist_ann_784_64_10.xml"

    ##############################
    # Load MNIST dataset
    ##############################
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    print('X_train: ' + str(X_train.shape))
    print('y_train: ' + str(y_train.shape))
    print('X_test:  ' + str(X_test.shape))
    print('y_test:  ' + str(y_test.shape))
    KNNHandWrittenDigits.show_random_digits(X_train, y_train, 10, 10)

    ##############################
    # Pre-processing
    ##############################
    w, h = X_test[0, :, :].shape
    X_train = X_train.reshape(X_train.shape[0], w * h).astype(np.float32)
    X_test = X_test.reshape(X_test.shape[0], w * h).astype(np.float32)
    X_train = X_train / 255
    X_test = X_test / 255
    y_train_onehot = to_categorical(y_train)
    y_train_onehot = np.float32(y_train_onehot)
    y_test = np.uint(y_test)

    if load_model_name == None:
        ##############################
        # Build and Train the model
        ##############################
        print("Training ANN..., depends on the layers of the ANN model, "
              "it could take some time from minutes to hours.")
        print("start time =", datetime.now().time())
        ann = create_ANN([784, 16, 10])
        ann.train(X_train, cv2.ml.ROW_SAMPLE, y_train_onehot)
        print("end time =", datetime.now().time())
    else:
        ##############################
        # Load a previously saved model
        ##############################
        ann = load_model(load_model_name)

    ##############################
    # Save the model
    ##############################
    if save_model_name != None:
        save_model(ann, save_model_name)

    ##############################
    # Prediction
    ##############################
    result = ann.predict(X_test)

    ##############################
    # Post-process
    ##############################
    predict = result[1]
    predict = predict.argmax(axis=1)
    X_test = X_test.reshape(X_test.shape[0], w, h)

    ##############################
    # Evaluation
    ##############################
    print("Accuracy Score:", accuracy_score(y_test, predict))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, predict))
    print("\nClassification Report:\n", classification_report(y_test, predict))

    ##############################
    # (Optional) Display the results
    ##############################
    # Show the predicted digits randomly
    print("Show the predicted digits randomly:")
    KNNHandWrittenDigits.show_random_result(X_test, y_test, 10, 10, predict)

    # Show the erroneously predicted digits randomly
    print("Show the erroneously predicted digits randomly:")
    pred_err = np.where(y_test != predict)
    KNNHandWrittenDigits.show_random_result(X_test[pred_err, :, :][0], y_test[pred_err], 10, 10, predict[pred_err])
