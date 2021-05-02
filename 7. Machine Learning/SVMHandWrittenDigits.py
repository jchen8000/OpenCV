from keras.datasets import mnist
import numpy as np
import cv2
from datetime import datetime
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import KNNHandWrittenDigits

if __name__ == "__main__":
    ##############################
    # Load MNIST dataset
    ##############################
    print("Loading MNIST dataset...")
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
    y_train = np.int32(y_train)
    y_test = np.int32(y_test)

    ##############################
    # Build and Train the model
    ##############################
    print("Training SVM, it could take about one or two minutes...")
    print("start time =", datetime.now().time())
    svm = cv2.ml.SVM_create()
    svm.setKernel(cv2.ml.SVM_LINEAR)
    svm.setTermCriteria((cv2.TERM_CRITERIA_MAX_ITER, 100, 1e-6))
    svm.train(X_train, cv2.ml.ROW_SAMPLE, y_train)

    ##############################
    # Prediction
    ##############################
    predict = svm.predict(X_test)
    print("end time =", datetime.now().time())

    ##############################
    # Post-processing
    ##############################
    y_test = np.uint(y_test)
    results = np.uint(predict[1])
    results = np.hstack(results)
    X_test = X_test.reshape(X_test.shape[0], w, h)
    print("results:", results.shape)
    print("y_test:", y_test.shape)

    ##############################
    # Evalutation
    ##############################
    print("Accuracy Score:", accuracy_score(y_test, results))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, results))
    print("\nClassification Report:\n", classification_report(y_test, results))

    ##############################
    # (Optional) Display the results
    ##############################
    # Show the predicted digits randomly
    print("Show the predicted digits randomly:")
    KNNHandWrittenDigits.show_random_result(X_test , y_test, 10, 10, results)

    # Show the erroneously predicted digits randomly
    pred_err = np.where(y_test != results)
    print("Show the erroneously predicted digits randomly:")
    print("y_test(error):", y_test[pred_err].shape)
    print("results(error):", results[pred_err].shape)
    print("X_test(error):", X_test[pred_err,:,:][0].shape)
    KNNHandWrittenDigits.show_random_result(X_test[pred_err,:,:][0], y_test[pred_err], 10, 10, results[pred_err])
