import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.datasets import make_blobs
from sklearn.datasets import make_circles

def plot_svc_decision_function(model, ax=None):
    """Plot the decision function for a 2D SVC"""
    if ax is None:
        ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # create grid to evaluate model
    x = np.linspace(xlim[0], xlim[1], 100)
    y = np.linspace(ylim[0], ylim[1], 100)
    Y, X = np.meshgrid(y, x)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    P = model.decision_function(xy).reshape(X.shape)

    # plot decision boundary and margins
    ax.contour(X, Y, P, colors='red',
               levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--']
               )
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

def plot_support_vectors(model):
    sv_color = 'red'
    plt.scatter(model.support_vectors_[:, 0],
                model.support_vectors_[:, 1],
                s=300, edgecolors=sv_color, facecolors='none',
                label='Support Vectors');

def plot_boundary_line():
    xfit = np.linspace(0, 3)
    for m, b in [(1, 1.65), (0.5, 1.6), (-0.3, 2.9)]:
        plt.plot(xfit, m * xfit + b, '-r')

if __name__ == "__main__":
    # Linear kernel sample
    X, y = make_blobs(n_samples=500, centers=2, random_state=0, cluster_std=0.40)

    svc = SVC(kernel='linear', C=1E10)
    svc.fit(X, y)

    fig = plt.figure(1, figsize=(6, 4))
    plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='cividis')

    # plot_boundary_line()
    plot_svc_decision_function(svc)
    plot_support_vectors(svc)
    plt.legend(loc="upper right")
    plt.show()
    # Save the plot
    # file4save = "c:/temp/svm03.png"
    # fig.savefig(file4save, dpi=220, format="png", transparent=True)
    # print(file4save, "file saved.")

    # Non-Linear kernel sample
    X_c, y_c = make_circles(500, factor=.2, noise=.1, random_state=0)
    fig = plt.figure(1, figsize=(6, 4))
    plt.scatter(X_c[:, 0], X_c[:, 1], c=y_c, s=50, cmap='viridis')
    plt.show()
    # Save the plot
    # file4save = "c:/temp/svm04.png"
    # fig.savefig(file4save, dpi=220, format="png", transparent=True)
    # print(file4save, "file saved.")

    clf = SVC(kernel='rbf', gamma='auto', C=1E6).fit(X_c, y_c)
    z = np.exp(-(X_c ** 2).sum(1))

    fig = plt.figure(figsize=(14, 4))
    fig.subplots_adjust(left=0.0625, wspace=0.5)
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax.scatter3D(X_c[:, 0], X_c[:, 1], z, c=y_c, s=50, cmap='viridis')
    ax.set_xlabel('$x_0$', fontsize=14)
    ax.set_ylabel('$x_1$', fontsize=14)
    ax.set_zlabel('z', fontsize=14)
    ax.set_title('Transform input data to 3D with Gaussian function\n'
                 'Data can be separated by a 2D-hyperplane', fontsize=12)
    ax.text(1.2, 1.2, 1.15, "$z=e^{-(x_0^2+x_1^2)}$", color='black', fontsize=12)

    plt.subplot(1, 2, 2)
    plt.scatter(X_c[:, 0], X_c[:, 1], c=y_c, s=50, cmap='viridis')
    plot_svc_decision_function(clf);
    plot_support_vectors(clf);
    plt.legend(loc="upper right")
    plt.show()
    # Save the plot
    # file4save = "c:/temp/svm05.png"
    # fig.savefig(file4save, dpi=250, format="png", transparent=True)
    # print(file4save, "file saved.")
