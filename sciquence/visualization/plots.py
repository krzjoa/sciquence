import matplotlib.pyplot as plt






def plot_matrix(M, save=False):
    plt.imshow(M, interpolation='nearest', aspect='auto', cmap='jet')
    plt.show()

    if save:
        plt.savefig(save)

