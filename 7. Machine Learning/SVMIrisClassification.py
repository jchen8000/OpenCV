import numpy as np
import cv2
from sklearn import datasets
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

def show_iris(feature1, feature2):
    n_samples = len(iris.target)
    for t in set(iris.target):
        x = [iris.data[i,feature1] for i in range(n_samples) if iris.target[i]==t]
        y = [iris.data[i,feature2] for i in range(n_samples) if iris.target[i]==t]
        if t == 0:
            plt.scatter(x, y, c='blue',s=60, marker="p", label=iris.target_names[t])
        elif t == 1:
            plt.scatter(x, y, c='brown',s=60, marker="o", label=iris.target_names[t])
        elif t == 2:
            plt.scatter(x, y, c='gray',s=80, marker="*", label=iris.target_names[t])

    plt.xlabel(iris.feature_names[feature1])
    plt.ylabel(iris.feature_names[feature2])
    plt.title(iris.feature_names[feature1] + " vs. " + iris.feature_names[feature2], fontsize=18)
    plt.legend(iris.target_names)

if __name__ == "__main__":
    ##############################
    # Load IRIS dataset
    ##############################
    iris = datasets.load_iris()
    print("Data Structure:", dir(iris))
    print("Description:\n", iris.DESCR)
    print("Data (first 10):\n", iris.data[0:10])
    print("Label:\n", iris.target)
    print("Label Name:", iris.target_names)
    print("Unique Label:", np.unique(iris.target))
    print("Feature:", iris.feature_names)

    # Show the data
    fig = plt.figure(figsize=(16, 6))
    plt.subplot(1, 2, 1)
    show_iris(0, 1)
    plt.subplot(1, 2, 2)
    show_iris(2, 3)
    plt.show()
    # Save the plot
    # file4save = "c:/temp/iris.png"
    # fig.savefig(file4save, dpi=200, format="png", transparent=True)
    # print(file4save, "file saved.")

    ##############################
    # Pre-processing
    ##############################
    data = iris.data.astype(np.float32)
    target = iris.target.astype(np.int32)
    X_train, X_test, y_train, y_test = \
        model_selection.train_test_split(data, target, test_size=0.2, random_state=2)
    print('X_train: ' + str(X_train.shape))
    print('y_train: ' + str(y_train.shape))
    print('X_test:  ' + str(X_test.shape))
    print('y_test:  ' + str(y_test.shape))

    ##############################
    # Build and Train the model
    ##############################
    svm = cv2.ml.SVM_create()
    svm.setKernel(cv2.ml.SVM_LINEAR)
    svm.setTermCriteria((cv2.TERM_CRITERIA_MAX_ITER, 100, 1e-6))
    svm.train(X_train, cv2.ml.ROW_SAMPLE, y_train)

    ##############################
    # Prediction
    ##############################
    predict = svm.predict(X_test)

    ##############################
    # Post-processing
    ##############################
    results = np.uint(predict[1])
    results = np.hstack(results)
    print("results:", results.shape)
    print("y_test:", y_test.shape)

    ##############################
    # Evalutation
    ##############################
    print("Accuracy Score:", accuracy_score(y_test, results))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, results))
    print("\nClassification Report:\n", classification_report(y_test, results))




