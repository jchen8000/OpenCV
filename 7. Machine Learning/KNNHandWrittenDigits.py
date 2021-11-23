from keras.datasets import mnist
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import numpy as np
import matplotlib.pyplot as plt
import cv2
from datetime import datetime

def show_random_digits(X, Y, row, col):
    fig, axarr = plt.subplots(row, col, figsize=(6, 6))
    for i in range(row):
        filter = np.where((Y == i))
        X1, Y1 = X[filter], Y[filter]
        for j in range(col):
            index = np.random.randint(X1.shape[0])
            axarr[i, j].imshow(X1[index], cmap="binary")
            axarr[i, j].axis('off')
            axarr[i, j].text(0.5, 1, str(Y1[index]), fontsize=12, c='g')
    print("The true label is shown in green.")
    plt.show()
    # Save the plot
    # file4save = "c:/temp/KNNHandDigits.png"
    # fig.savefig(file4save, dpi=200, format="png", transparent=True)
    # print(file4save, "file saved.")

def show_random_result(X, Y, row, col, pred):
    fig, axarr = plt.subplots(row, col, figsize=(6, 6))
    for i in range(row):
        for j in range(col):
            index = np.random.randint(X.shape[0])
            axarr[i, j].imshow(X[index], cmap="binary")
            axarr[i, j].axis('off')
            axarr[i, j].text(0.5, 1, str(Y[index]), fontsize=12, c='g')
            axarr[i, j].text(10,  1, "("+str(pred[index])+")", fontsize=12, c='r')
    print("The true label is shown in green, "
          "and the predicted value is shown within () in red.")
    plt.show()
    # Save the plot
    # file4save = "c:/temp/KNNHandDigits2.png"
    # fig.savefig(file4save, dpi=200, format="png", transparent=True)
    # print(file4save, "file saved.")

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
    show_random_digits(X_train, y_train, 10, 10)

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
    knn = cv2.ml.KNearest_create()
    knn.train(X_train, cv2.ml.ROW_SAMPLE, y_train)

    ##############################
    # Prediction
    ##############################
    print("Running KNN, it could take about 5 or more minutes...")
    print("start time =", datetime.now().time())
    k = 7
    _, results, _, _ = knn.findNearest(X_test, k)
    print("end time =", datetime.now().time())

    ##############################
    # Post-process
    ##############################
    y_test = np.uint(y_test)
    results = np.hstack(results)
    results = np.uint(results)
    X_test = X_test.reshape(X_test.shape[0], w, h)

    ##############################
    # Evaluation
    ##############################
    print("K=", k)
    print("Accuracy Score:", accuracy_score(y_test, results))
    print("Confusion Matrix:\n", confusion_matrix(y_test, results))
    print("Classification Report:\n", classification_report(y_test, results))

    ##############################
    # (Optional) Display the results
    ##############################
    # Show the predicted digits randomly
    print("Show the predicted digits randomly:")
    show_random_result(X_test , y_test, 10, 10, results)

    # Show the erroneously predicted digits randomly
    pred_err = np.where(y_test != results)
    print("Show the erroneously predicted digits randomly:")
    print("y_test(error):", y_test[pred_err].shape)
    print("results(error):", results[pred_err].shape)
    print("X_test(error):", X_test[pred_err,:,:][0].shape)
    show_random_result(X_test[pred_err,:,:][0] , y_test[pred_err], 10, 10, results[pred_err])
