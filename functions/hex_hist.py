import matplotlib
import numpy as np
import matplotlib.pyplot as plt





def hex_hist(x, y,  grid, colors,Z ):
    fig = plt.figure(figsize=(12, 12))
    left, width = 0.075, 0.65
    bottom, height = 0.075, 0.65
    spacing = 0.005
    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom + height + spacing, width, 0.1]
    rect_histy = [left + width + spacing, bottom, 0.1, height]
    ax = fig.add_axes(rect_scatter)


    # no labels
    cm = plt.cm.get_cmap('viridis')

    #ax_histx.tick_params(axis="x", labelbottom=False)
    #ax_histy.tick_params(axis="y", labelleft=False)


    ax.hexbin(x, y, gridsize=grid,bins=np.linspace(0,1,20), cmap =colors, mincnt=1,C=Z)


    binwidth = 0.025
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
