#import plotly
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#from plotly.graph_objs import Scatter, Figure, Layout
#init_notebook_mode(connected=True)
#
#from plotly.graph_objs import *
#import numpy as np
#-------------------------------------------------------------------------------

#plotly.offline.plot([{"x": [1, 2, 3], "y": [3, 1, 6]}])

#-------------------------------------------------------------------------------
#x = np.random.randn(2000)
#y = np.random.randn(2000)
#
#plot([Histogram2dContour(x=x, y=y, contours=Contours(coloring='heatmap')),
#       Scatter(x=x, y=y, mode='markers', marker=Marker(color='white', size=3, opacity=0.3))], show_link=False)

#-------------------------------------------------------------------------------
#import plotly
#from plotly.graph_objs import Scatter, Layout
#
#plotly.offline.plot({
#    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#    "layout": Layout(title="hello world")
#})