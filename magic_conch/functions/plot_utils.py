import pylab
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
def suplabel(axis,label,label_prop=None,
             labelpad=5,
             ha='center',va='center'):
    ''' Add super ylabel or xlabel to the figure
    Similar to matplotlib.suptitle
    axis       - string: "x" or "y"
    label      - string
    label_prop - keyword dictionary for Text
    labelpad   - padding from the axis (default: 5)
    ha         - horizontal alignment (default: "center")
    va         - vertical alignment (default: "center")
    '''
    fig = pylab.gcf()
    xmin = []
    ymin = []
    for ax in fig.axes:
        xmin.append(ax.get_position().xmin)
        ymin.append(ax.get_position().ymin)
    xmin,ymin = min(xmin),min(ymin)
    dpi = fig.dpi
    if axis.lower() == "y":
        rotation=90.
        x = xmin-float(labelpad)/dpi
        y = 0.5
    elif axis.lower() == 'x':
        rotation = 0.
        x = 0.5
        y = ymin - float(labelpad)/dpi
    else:
        raise Exception("Unexpected axis: x or y")
    if label_prop is None:
        label_prop = dict()
    pylab.text(x,y,label,rotation=rotation,
               transform=fig.transFigure,
               ha=ha,va=va,fontsize=34,
               **label_prop)

def hex_hist(x, y, ax, grid, colors,Z ):
    ''' Make hexbin 2d histogram with given Z value instead of counts
        Similar to matplotlib hexgrid
        x      - 1-D array-like: x values
        y      - 1-D array-like: y values
        ax     - axis object to plot on
        grid   - int: number of bins per row, column
        colors - string: matplotlib.Colormap
        Z      - 1-D array-like: bin value for each x,y pair
    '''

    hx = ax.hexbin(x, y, gridsize=grid,bins=np.linspace(0,1,20), cmap =colors, mincnt=1,C=Z, reduce_C_function=np.mean)
    return(hx.get_array(), hx.get_offsets())
