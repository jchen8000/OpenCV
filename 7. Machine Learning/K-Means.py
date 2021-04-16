import numpy as np
import cv2
from matplotlib import pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

def sample_tshirt():
    X, y = make_blobs(n_samples=600, centers=1, center_box=(50,80), cluster_std=8.8, random_state=1)
    X[:,0] += 100
    X = np.float32(X)
    plt.scatter(X[:,0],X[:,1],c='azure')
    plt.xlabel('Height')
    plt.ylabel('Weight')
    plt.show()

def sample_cluster():
    X, y = make_blobs(n_samples=600, centers=2, cluster_std=1.8, random_state=3)
    X = np.float32(X)
    plt.figure(figsize=(6, 4))
    plt.scatter(X[:,0],X[:,1],s=10,cmap='winter')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    return X, y

def run_kmeans(X, iter=1):
    criteria = (cv2.TERM_CRITERIA_MAX_ITER, iter, 1.0)
    ret,label,center=cv2.kmeans(X, 2, None , criteria, iter, cv2.KMEANS_RANDOM_CENTERS)
    print(ret)
    A = X[label.ravel()==0]
    B = X[label.ravel()==1]
    font = {'color': 'k', 'size':16, 'weight': 'bold'}
    plt.figure(figsize=(6, 4))
    plt.scatter(A[:,0],A[:,1],s=10, c='tab:olive')
    plt.scatter(B[:,0],B[:,1],s=10, c='tab:cyan')
    plt.scatter(center[:,0],center[:,1],s = 180, c='k')
    plt.text(center[0,0]+1, center[0,1]-2, "$\mu_1$", fontdict=font)
    plt.text(center[1,0]+1, center[1,1]-2, "$\mu_2$", fontdict=font)
    plt.text(-18, 15, "Distance={:.2f}".format(ret), fontsize=12)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

if __name__ == "__main__":
    # sample_tshirt()
    X, y = sample_cluster()
    run_kmeans(X, iter=1)
    run_kmeans(X, iter=1)
    run_kmeans(X, iter=10)

