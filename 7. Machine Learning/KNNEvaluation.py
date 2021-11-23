import numpy as np
import cv2
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


def evaluate_knn(k=None):
    X, y = make_blobs(n_samples=800, centers=2, cluster_std=6.8,
                      random_state=2)
    X = np.float32(X)
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size = 0.2, random_state = 1)
    print('X_train: ' + str(X_train.shape))
    print('y_train: ' + str(y_train.shape))
    print('X_test:  ' + str(X_test.shape))
    print('y_test:  ' + str(y_test.shape))

    A = X_train[y_train.ravel() == 0]
    B = X_train[y_train.ravel() == 1]
    fig = plt.figure(figsize=(8, 6))
    plt.scatter(A[:, 0], A[:, 1], marker='D', s=20, c='blue', label='0')
    plt.scatter(B[:, 0], B[:, 1], marker='o', s=20, c='chocolate', label='1')
    plt.legend(loc='upper right', fontsize=12)
    plt.show()
    # Save the plot
    # file4save = "c:/temp/KNN01.png"
    # fig.savefig(file4save, dpi=200, format="png", transparent=True)
    # print(file4save, "file saved.")

    knn = cv2.ml.KNearest_create()
    knn.train(X_train, cv2.ml.ROW_SAMPLE, y_train)

    accuracies_test = []
    accuracies_train = []
    kVals = np.arange(1,100,2)
    for kv in kVals:
        _, res_test, _, _ = knn.findNearest(X_test, kv)
        acc_test = accuracy_score(y_test, res_test)
        accuracies_test.append(acc_test)
        _, res_train, _, _ = knn.findNearest(X_train, kv)
        acc_train = accuracy_score(y_train, res_train)
        accuracies_train.append(acc_train)
    if k != None:
        print("Report for Test set at K=" + str(k))
        _, res_test, _, _ = knn.findNearest(X_test, k)
        print("Accuracy Score:", accuracy_score(y_test, res_test))
        print("Confusion Matrix:\n", confusion_matrix(y_test, res_test))
        print("Classification Report:\n", classification_report(y_test, res_test))


    fig2 = plt.figure(figsize=(8, 6))
    plt.plot(kVals, accuracies_train, label="Training set")
    plt.plot(kVals, accuracies_test, label = "Testing set")
    plt.xlabel("K Value")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.show()
    # Save the plot
    # file4save = "c:/temp/KNN02.png"
    # fig2.savefig(file4save, dpi=200, format="png", transparent=True)
    # print(file4save, "file saved.")

if __name__ == "__main__":
    evaluate_knn(k=20)