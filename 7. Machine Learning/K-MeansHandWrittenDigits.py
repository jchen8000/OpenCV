from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
import cv2

def show_random_digits(X, Y, row, col):
    fig, axarr = plt.subplots(row, col, figsize=(6, 6))
    for i in range(row):
        filter = np.where((Y == i))
        X1, Y1 = X[filter], Y[filter]
        for j in range(col):
            index = np.random.randint(X1.shape[0])
            axarr[i, j].imshow(X1[index], cmap="binary")
            axarr[i, j].axis('off')
    plt.show()
    # Save the plot
    # file4save = "c:/temp/handDigits.png"
    # fig.savefig(file4save, dpi=200, format="png", transparent=True)
    # print(file4save, "file saved.")

def show_result(results):
    fig, ax = plt.subplots(1, 10, figsize=(6, 1))
    for axi, result in zip(ax.flat, results):
        axi.imshow(result, interpolation='nearest', cmap="binary")
        axi.axis('off')
    plt.show()
    # Save the plot
    # file4save = "c:/temp/handDigits2.png"
    # fig.savefig(file4save, dpi=200, format="png", transparent=True)
    # print(file4save, "file saved.")

if __name__ == "__main__":
    print("Loading MINST dataset...")
    (X_train, Y_train), (X_test, Y_test) = mnist.load_data()
    print('X_train: ' + str(X_train.shape))
    print('Y_train: ' + str(Y_train.shape))
    print('X_test:  ' + str(X_test.shape))
    print('Y_test:  ' + str(Y_test.shape))
    show_random_digits(X_train, Y_train, 10, 10)

    print("Running K-Means...")
    X = X_train.reshape(X_train.shape[0], X_train.shape[1] * X_train.shape[2])
    X = np.float32(X)
    clusters = 10
    criteria = (cv2.TERM_CRITERIA_MAX_ITER, 50, 1.0)
    ret,label,center=cv2.kmeans(X, clusters, Y_train, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    results = center.reshape(clusters, X_train.shape[1], X_train.shape[2])
    show_result(results)




