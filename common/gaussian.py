import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.stats import multivariate_normal

def plot_2d_gaussian(mu, sigma):
    #Create grid and multivariate normal
    x = np.linspace(-10,10,500)
    y = np.linspace(-10,10,500)
    X, Y = np.meshgrid(x,y)
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X; pos[:, :, 1] = Y
    rv = multivariate_normal(mu, sigma)

    # plot the gaussian function
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.plot_surface(X, Y, rv.pdf(pos), cmap='viridis', linewidth=0)
    ax.text2D(0.05, 0.95, "$\mu=$ %s\n$\Sigma=$ %s" % (mu,sigma), transform=ax.transAxes)
    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')
    ax.set_zlabel('$P$')
    plt.show()
    # #Save the plot
    # file4save = "c:/temp/gaussian2d.png"
    # fig.savefig(file4save, dpi=200, format="png", transparent=True)
    # print(file4save, "file saved.")



if __name__ == "__main__":
    mu = [0,0]
    sigma = [[9,0],[0,9]]
    plot_2d_gaussian(mu, sigma)