import numpy as np
import matplotlib.pyplot as plt


def identity_function():
    X = np.linspace(-4, 4, 100)
    fig, ax = plt.subplots(1, 2, figsize=figsize)
    ax[0].arrow(-4, 0, 7.5, 0, head_width=0.15, head_length=0.4, fc='k', ec='k')
    ax[0].arrow(0, -4, 0, 7.5, head_width=0.15, head_length=0.4, fc='k', ec='k')
    ax[0].plot(X, X, 'b')
    ax[0].set_title('Identity Function', fontsize=18)
    ax[0].grid()
    ax[0].set_ylim([-4, 4])
    ax[0].text(0.1, 3.5, r'$g(z)=z$', fontsize=16)
    ax[0].text(3.95, -0.5, r'$z$', fontsize=16)
    ax[1].arrow(-4, 0, 7.5, 0, head_width=0.15, head_length=0.4, fc='k', ec='k')
    ax[1].arrow(0, -4, 0, 7.5, head_width=0.15, head_length=0.4, fc='k', ec='k')
    ax[1].plot(X, (0.0*X+1.0), 'b')
    ax[1].set_title('Identity Derivative', fontsize=18)
    ax[1].grid()
    ax[1].set_ylim([-4, 4])
    ax[1].text(0.1, 3.5, r"$g'(z)=1", fontsize=16)
    ax[1].text(3.95, -0.5, r'$z$', fontsize=16)
    plt.show()
    # Save the plot
    # file4save = "c:/temp/identity_func.png"
    # fig.savefig(file4save, dpi=150, format="png", transparent=True)
    # print(file4save, "file saved.")


def sigmoid(z):
  return 1/(1+np.exp(-z))

def sigmoidDerivative(z):
    return sigmoid(z) * (1 - sigmoid(z) )

def sigmoid_function():
    X = np.linspace(-5, 5, 100)
    fig, ax = plt.subplots(1, 2, figsize=figsize)
    ax[0].arrow(-5, 0, 9.8, 0, head_width=0.04, head_length=0.5, fc='k', ec='k')
    ax[0].arrow(0, -0.1, 0, 1.15, head_width=0.2, head_length=0.1, fc='k', ec='k')
    ax[0].plot(X, sigmoid(X),'b')
    ax[0].set_title('Sigmoid Function',fontsize=18)
    ax[0].grid()
    ax[0].set_ylim([-0.05, 1.2])
    ax[0].text(0.1, 1.1, r'$g(z)=\frac{1}{1+e^{-z}}$', fontsize=16)
    ax[0].text(4.95, 0.03, r'$z$', fontsize=16)
    ax[1].arrow(-5, 0, 9.8, 0, head_width=0.04, head_length=0.5, fc='k', ec='k')
    ax[1].arrow(0, -0.1, 0, 1.15, head_width=0.2, head_length=0.1, fc='k', ec='k')
    ax[1].plot(X, sigmoidDerivative(X),'b')
    ax[1].set_title('Sigmoid Derivative',fontsize=18)
    ax[1].set_ylim([-0.05, 1.2])
    ax[1].grid()
    ax[1].text(0.1, 1.1, r"$g'(z) = g(z)(1-g(z))$", fontsize=16)
    ax[1].text(4.95, 0.03, r'$z$', fontsize=16)
    plt.show()
    # Save the plot
    # file4save = "c:/temp/sigmoid_func.png"
    # fig.savefig(file4save, dpi=150, format="png", transparent=True)
    # print(file4save, "file saved.")

def tanh_function():
    z = np.arange(-5, 5, .1)
    t = np.tanh(z)
    dz = 1 - t**2
    fig, ax = plt.subplots(1, 2, figsize=figsize)
    ax[0].arrow(-5, 0, 9.8, 0, head_width=0.06, head_length=0.5, fc='k', ec='k')
    ax[0].arrow(0, -1.1, 0, 2.25, head_width=0.2, head_length=0.15, fc='k', ec='k')
    ax[0].plot(z, t,'b')
    ax[0].set_title('Tanh Function',fontsize=18)
    ax[0].grid()
    ax[0].set_ylim([-1.2, 1.4])
    ax[0].text(0.1, 1.15, r'$g(z)=\frac{e^{z}-e^{-z}}{e^{z}+e^{-z}}$', fontsize=16)
    ax[0].text(4.95, 0.03, r'$z$', fontsize=16)
    ax[1].arrow(-5, 0, 9.8, 0, head_width=0.06, head_length=0.5, fc='k', ec='k')
    ax[1].arrow(0, -1.1, 0, 2.25, head_width=0.2, head_length=0.15, fc='k', ec='k')
    ax[1].plot(z, dz,'b')
    ax[1].set_title('Tanh Derivative',fontsize=18)
    ax[1].grid()
    ax[1].set_ylim([-1.2, 1.4])
    ax[1].text(0.1, 1.2, r"$g'(z)=1-g(z)^2$", fontsize=16)
    ax[1].text(4.95, 0.03, r'$z$', fontsize=16)
    plt.show()
    # Save the plot
    # file4save = "c:/temp/tanh_func.png"
    # fig.savefig(file4save, dpi=150, format="png", transparent=True)
    # print(file4save, "file saved.")

def ReLU(x):
    return np.maximum(0.0, x)

# derivation of relu
def ReLU_Derivative(x):
    return np.greater(x, 0).astype(int)

def relu_function():
    X = np.linspace(-4, 4, 100)
    fig, ax = plt.subplots(1, 2, figsize=figsize)
    ax[0].arrow(0, -0.1, 0, 4.4, head_width=0.15, head_length=0.4, fc='k', ec='k')
    ax[0].arrow(-4.2, 0, 8, 0, head_width=0.15, head_length=0.4, fc='k', ec='k')
    ax[0].plot(X, ReLU(X), 'b')
    ax[0].set_title('ReLU Function', fontsize=18)
    ax[0].grid()
    ax[0].set_ylim([-0.2, 5])
    ax[0].text(0.1, 4.5, r'$g(z)=max(0,z)$', fontsize=16)
    ax[0].text(3.95, -0.3, r'$z$', fontsize=16)
    ax[1].arrow(0, -0.1, 0, 4.4, head_width=0.15, head_length=0.4, fc='k', ec='k')
    ax[1].arrow(-4.2, 0, 8, 0, head_width=0.15, head_length=0.4, fc='k', ec='k')
    ax[1].plot(X, ReLU_Derivative(X), 'b')
    ax[1].set_title('ReLU Derivative', fontsize=18)
    ax[1].grid()
    ax[1].set_ylim([-0.2, 5])
    ax[1].text(0.1, 4.5, r"$g'(z)=1, z>0$", fontsize=16)
    ax[1].text(1.18, 4.2, r"$=0, z<0$", fontsize=16)
    ax[1].text(3.95, -0.3, r'$z$', fontsize=16)
    plt.show()
    # Save the plot
    # file4save = "c:/temp/relu_func.png"
    # fig.savefig(file4save, dpi=150, format="png", transparent=True)
    # print(file4save, "file saved.")

def Leaky_ReLU(z, epsilon=0.01):
    return np.maximum(epsilon * z, z)

def Leaky_ReLU_Derivative(z, epsilon=0.01):
    dz = np.ones_like(z)
    dz[z < 0] = epsilon
    return dz

def leaky_relu_function():
    z = np.linspace(-4, 4, 100)
    fig, ax = plt.subplots(1, 2, figsize=figsize)
    ax[0].arrow(0, -0.1, 0, 4.4, head_width=0.15, head_length=0.4, fc='k', ec='k')
    ax[0].arrow(-4.2, 0, 8, 0, head_width=0.15, head_length=0.4, fc='k', ec='k')
    ax[0].plot(z, Leaky_ReLU(z, 0.1), 'b')
    ax[0].set_title(r'Leaky ReLU Function $(\epsilon = 0.1)$', fontsize=18)
    ax[0].grid()
    ax[0].set_ylim([-0.5, 5])
    ax[0].text(0.1, 4.5, r'$g(z)=max(\epsilon z, z)$', fontsize=16)
    ax[0].text(3.95, -0.3, r'$z$', fontsize=16)
    ax[1].arrow(0, -0.1, 0, 4.4, head_width=0.15, head_length=0.4, fc='k', ec='k')
    ax[1].arrow(-4.2, 0, 8, 0, head_width=0.15, head_length=0.4, fc='k', ec='k')
    ax[1].plot(z, Leaky_ReLU_Derivative(z, 0.1), 'b')
    ax[1].set_title(r'Leaky ReLU Derivative $(\epsilon = 0.1)$', fontsize=18)
    ax[1].grid()
    ax[1].set_ylim([-0.5, 5])
    ax[1].text(0.1, 4.5, r"$g'(z)=1, z>0$", fontsize=16)
    ax[1].text(1.18, 4.2, r"$=\epsilon, z<0$", fontsize=16)
    ax[1].text(3.95, -0.3, r'$z$', fontsize=16)
    plt.show()
    # Save the plot
    # file4save = "c:/temp/leaky_func.png"
    # fig.savefig(file4save, dpi=150, format="png", transparent=True)
    # print(file4save, "file saved.")

def gaussian(z):
    return np.exp(-z*z)

def gaussian_derivative(z):
    return -2*z*gaussian(z)

def gaussian_function():
    X = np.linspace(-5, 5, 100)
    fig, ax = plt.subplots(1, 2, figsize=figsize)
    ax[0].arrow(-5, 0, 9.8, 0, head_width=0.04, head_length=0.5, fc='k', ec='k')
    ax[0].arrow(0, -1.0, 0, 2.2, head_width=0.2, head_length=0.1, fc='k', ec='k')
    ax[0].plot(X, gaussian(X),'b')
    ax[0].set_title('Gaussian Function',fontsize=18)
    ax[0].grid()
    ax[0].set_ylim([-1.0, 1.35])
    ax[0].text(0.1, 1.15, r'$g(z)=e^{-z^{2}}}$', fontsize=14)
    ax[0].text(4.95, 0.03, r'$z$', fontsize=16)
    ax[1].arrow(-5, 0, 9.8, 0, head_width=0.04, head_length=0.5, fc='k', ec='k')
    ax[1].arrow(0, -1.0, 0, 2.2, head_width=0.2, head_length=0.1, fc='k', ec='k')
    ax[1].plot(X, gaussian_derivative(X),'b')
    ax[1].set_title('Gaussian Derivative',fontsize=18)
    ax[1].set_ylim([-1.0, 1.35])
    ax[1].grid()
    ax[1].text(0.1, 1.15, r"$g'(z) = -2ze^{-z^{2}}}$", fontsize=14)
    ax[1].text(4.95, 0.03, r'$z$', fontsize=16)
    plt.show()
    # Save the plot
    # file4save = "c:/temp/gaussian_func.png"
    # fig.savefig(file4save, dpi=150, format="png", transparent=True)
    # print(file4save, "file saved.")

if __name__ == "__main__":
    figsize = (12, 5)
    identity_function()
    sigmoid_function()
    tanh_function()
    relu_function()
    leaky_relu_function()
    gaussian_function()