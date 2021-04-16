from keras.datasets import mnist
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import numpy as np
import matplotlib.pyplot as plt
import cv2
from datetime import datetime

def show_random_digits(X, Y, row, col):
    _, axarr = plt.subplots(row, col, figsize=(6, 6))
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

def show_random_result(X, Y, row, col, pred):
    _, axarr = plt.subplots(row, col, figsize=(6, 6))
    for i in range(row):
        for j in range(col):
            index = np.random.randint(X.shape[0])
            axarr[i, j].imshow(X[index], cmap="binary")
            axarr[i, j].axis('off')
            axarr[i, j].text(0.5, 1, str(Y[index]), fontsize=12, c='g')
            axarr[i, j].text(10,  1, str(pred[index]), fontsize=12, c='r')
    print("The true label is shown in green, "
          "and the predicted value is shown within [] in red.")
    plt.show()

if __name__ == "__main__":
    print("Loading MINST dataset...")
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    print('X_train: ' + str(X_train.shape))
    print('y_train: ' + str(y_train.shape))
    print('X_test:  ' + str(X_test.shape))
    print('y_test:  ' + str(y_test.shape))
    show_random_digits(X_train, y_train, 10, 10)

    w, h = X_test[0, :, :].shape
    X_train = X_train.reshape(X_train.shape[0], w * h).astype(np.float32)
    X_test = X_test.reshape(X_test.shape[0], w * h).astype(np.float32)
    y_train = np.float32(y_train)
    y_test = np.float32(y_test)

    print("Running KNN, it could take about 5 or more minutes...")
    print("start time =", datetime.now().time())
    k = 7
    knn = cv2.ml.KNearest_create()
    knn.train(X_train, cv2.ml.ROW_SAMPLE, y_train)
    _, results, _, _ = knn.findNearest(X_test, k)
    print("end time =", datetime.now().time())

    X_test = X_test.reshape(X_test.shape[0], w, h)
    y_test = np.uint8(y_test)
    results = np.uint8(results)
    print("K=", k)
    print("Accuracy Score:", accuracy_score(y_test, results))
    print("Confusion Matrix:\n", confusion_matrix(y_test, results))
    print("Classification Report:\n", classification_report(y_test, results))
    show_random_result(X_test , y_test, 10, 10, results)


