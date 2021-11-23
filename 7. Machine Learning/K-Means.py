import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from sklearn.datasets import make_blobs

def sample_tshirt():
    X, y = make_blobs(n_samples=600, centers=1, center_box=(50,80), cluster_std=8.8, random_state=1)
    X[:,0] += 100
    X = np.float32(X)
    fig = plt.figure(figsize=(8, 5))
    plt.scatter(X[:,0],X[:,1],cmap='winter')
    ellipse_s = Ellipse(xy=(143.0, 70.0), width=18, height=50, angle=10, edgecolor='r', fc='None', lw=3)
    ellipse_m = Ellipse(xy=(158.5, 75.0), width=18, height=55, angle=15, edgecolor='r', fc='None', lw=3)
    ellipse_l = Ellipse(xy=(175.0, 80.0), width=20, height=55, angle=15, edgecolor='r', fc='None', lw=3)
    plt.gca().add_patch(ellipse_s)
    plt.gca().add_patch(ellipse_m)
    plt.gca().add_patch(ellipse_l)
    plt.text(138, 90, "S", fontsize=18, c='r')
    plt.text(150, 96, "M", fontsize=18, c='r')
    plt.text(168, 100, "L", fontsize=18, c='r')
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')
    plt.show()
    # Save the plot
    # file4save = "c:/temp/kmeans01.png"
    # fig.savefig(file4save, dpi=180, format="png", transparent=True)
    # print(file4save, "file saved.")

def sample_cluster():
    X, y = make_blobs(n_samples=600, centers=2, cluster_std=1.8, random_state=3)
    X = np.float32(X)
    fig = plt.figure(figsize=(8, 5))
    plt.scatter(X[:,0],X[:,1],s=30, marker="o", c='tab:olive')

    # A = X[y==0]
    # B = X[y==1]
    # plt.scatter(A[:,0],A[:,1],s=20, marker="o", c='tab:olive')
    # plt.scatter(B[:,0],B[:,1],s=20, marker="x", c='tab:cyan')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    # Save the plot
    # file4save = "c:/temp/kmeans02.png"
    # fig.savefig(file4save, dpi=200, format="png", transparent=True)
    # print(file4save, "file saved.")

    return X, y

def run_kmeans(X, iter=1):
    criteria = (cv2.TERM_CRITERIA_MAX_ITER, iter, 1.0)
    ret,label,center=cv2.kmeans(X, 2, None , criteria, iter, cv2.KMEANS_RANDOM_CENTERS)
    print(ret)
    A = X[label.ravel()==0]
    B = X[label.ravel()==1]
    font = {'color': 'k', 'size':20, 'weight': 'bold'}
    fig = plt.figure(figsize=(8, 5))
    plt.scatter(A[:,0],A[:,1],s=30, marker="o", c='tab:olive')
    plt.scatter(B[:,0],B[:,1],s=30, marker="x", c='tab:cyan')
    plt.scatter(center[:,0],center[:,1],s = 180, c='k')
    plt.text(center[0,0]+0.5, center[0,1]-0.5, "$\mu_1$", fontdict=font)
    plt.text(center[1,0]+0.5, center[1,1]-0.5, "$\mu_2$", fontdict=font)
    plt.text(-10, 10, "Distance={:.2f}".format(ret), fontsize=12)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    # Save the plot
    # file4save = "c:/temp/kmeans03.png"
    # fig.savefig(file4save, dpi=200, format="png", transparent=True)
    # print(file4save, "file saved.")

if __name__ == "__main__":
    sample_tshirt()
    X, y = sample_cluster()
    run_kmeans(X, iter=1)
    run_kmeans(X, iter=1)
    run_kmeans(X, iter=100)

