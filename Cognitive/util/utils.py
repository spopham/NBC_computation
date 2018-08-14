import numpy as np
import itertools
from matplotlib.pyplot import figure

def draw_slices(volume, nr=6, nc=6, tmin=None, tmax=None, cmap=None):
    """Creates a new figure and displays each slice of [volume] in a separate subplot.
    The figure will have [nr] rows of subplots and [nc] columns.
    The minimum color value for every subplot will be [tmin] (or the minimum of the volume
    if [tmin] is None).
    Similarly, the maximum color value for every subplot will be [tmax] (or the maximum of
    the volume if [tmax] is None).
    The colormap [cmap] will be used if given, otherwise the matplotlib default will be used.
    """
    fig = figure(figsize=(20,20)) ## Create the new figure

    if tmin is None: ## If tmin isn't given
        tmin = volume.min() ## Use the minimum of the whole volume
    if tmax is None: ## If tmax isn't given
        tmax = volume.max() ## Use the maximum of the whole volume
    if cmap is None:
        cmap = 'inferno'
    
    ## Using matplotlib's "subplot" function adds a lot of space between subplots,
    ## so we're going to manually set up the subplot locations here
    ledges = np.linspace(0, 1, nc+1)[:-1] ## The left edge of each column (in fraction of figure)
    bedges = np.linspace(1, 0, nr+1)[1:] ## The bottom edge of each row
    width = 1/float(nc) ## The width of each column
    height = 1/float(nr) ## The width of each row

    bottoms,lefts = zip(*list(itertools.product(bedges, ledges))) ## The bottom and left for each subplot
    
    for ni,sl in enumerate(np.split(volume, len(volume))): ## Iterate through slices of volume
        ax = fig.add_axes((lefts[ni], bottoms[ni], width, height)) ## Create a new axis
        ax.imshow(sl.squeeze(), ## Plot the slice
                  vmin=tmin, ## With the specified minimum
                  vmax=tmax, ## And maximum
                  cmap=cmap, ## With specified colormap
                  interpolation="nearest") ## Make sure it's not interpolated
        ax.set_xticks([]) ## Turn off x-axis ticks
        ax.set_yticks([]) ## Turn off y-axis ticks
    
    return fig ## Return the figure object
