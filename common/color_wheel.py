import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


def show_color_wheel():
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], projection='polar')

    colormap = plt.get_cmap('hsv')
    norm = mpl.colors.Normalize(0.0, 2*np.pi)

    n = 180
    t = np.linspace(0, 2*np.pi, n)
    r = np.linspace(0.3, 1)
    rg, tg = np.meshgrid(r, t)
    c = tg
    im = ax.pcolormesh(t, r, c.T, norm=norm, cmap=colormap)
    ax.set_yticklabels([])
    # ax.set_xticklabels([])
    ax.spines['polar'].set_visible(False)
    # plt.savefig("../res/color_wheel.png", transparent=True)
    plt.show()
    # Save the plot
    # file4save = "c:/temp/colorwheel.png"
    # fig.savefig(file4save, dpi=200, format="png", transparent=True)
    # print(file4save, "file saved.")

if __name__ == "__main__":
    show_color_wheel()