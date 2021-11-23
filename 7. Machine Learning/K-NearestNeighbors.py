import numpy as np
import cv2
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs

def sample_knn_dataset(k, r=None):
    X, y = make_blobs(n_samples=60, centers=2, cluster_std=8.8, random_state=2)
    X = np.float32(X)
    A = X[y.ravel()==0]
    B = X[y.ravel()==1]
    plt.figure(figsize=(8, 8))
    plt.scatter(A[:, 0], A[:, 1], marker='x', s=30, c='blue', label='0')
    plt.scatter(B[:, 0], B[:, 1], marker='o', s=30, c='chocolate', label='1')
    plt.legend(loc='upper right', fontsize=12)
    if r == None:
        new = np.random.randint(-20, 20, (1, 2)).astype(np.float32)
        plt.scatter(new[:, 0], new[:, 1], s=50, marker='X', c='r')
    else:
        new = [[0,0]]
        new = np.float32(new)
        plt.scatter(0, 0, s=50, marker='D', c='r')
        circle = plt.Circle((0, 0), r, color='r', fill=False)
        plt.gca().add_patch(circle)
        plt.text(-1, r, "k="+str(k), fontsize=12, c='r')
    knn = cv2.ml.KNearest_create()
    knn.train(X, cv2.ml.ROW_SAMPLE, y)
    ret, results, neighbours, dist = knn.findNearest(new, k)
    print("result: ", np.uint8(results))
    print("neighbours: ", np.uint8(neighbours))
    print("distance: ", dist)
    plt.text(-20, 20, "k=" + str(k) + ", result=" + str(int(results)), fontsize=16, c='r')
    plt.show()

if __name__ == "__main__":
    sample_knn_dataset(k=7, r=4.0)
    sample_knn_dataset(k=9, r=5.2)
    sample_knn_dataset(k=7)


