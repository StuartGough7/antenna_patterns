import plotly as py
import plotly.graph_objs as go
import pandas as pd

#=============================================================================
def PolarPlot(location, Heading, FileNaming):
    df = pd.read_excel(location, sheetname='Sheet1')                            #r needs to be there for location (raw string. Can use double backslashes or forward slashes)
    data = [
        go.Scatterpolar(
            r = df['x'],
            theta = df['y'],
            mode = 'lines',name = 'MP124G',line =  dict(color = 'peru'))]
    layout = go.Layout(
        title = Heading,
        font = dict(family = 'Arial, sans-serif;', size = 12, color = '#000'),showlegend = False)
    
    fig = go.Figure(data=data, layout=layout)
    py.offline.plot(fig, filename= FileNaming)
    return
#=============================================================================    
    