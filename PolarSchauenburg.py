import plotly as py
import plotly.graph_objs as go
import pandas as pd

df1 = pd.read_excel(r'C:\Users\Hans-PC\Desktop\Stuart\Companies\Schauenburg\09.03.18\Schauenburg Graphs\Excels\First Mounting 2.4G.xlsx', sheetname='Sheet1')        #r needs to be there for location (raw string. Can use double backslashes or forward slashes)

data = [
    go.Scatterpolar(
        r = df1['x'],
        theta = df1['y'],
        mode = 'lines',name = 'MP124G',line =  dict(color = 'peru'))]

layout = go.Layout(
    title = 'UHF 1 Standard, UHF 2 Standard: Mounting Point 1 @ 2.4GHz',
    font = dict(family = 'Arial, sans-serif;', size = 12, color = '#000'),showlegend = False,
)

fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig, filename='my-graph.html')


#==============================================================================

df2 = pd.read_excel(r'C:\Users\Hans-PC\Desktop\Stuart\Companies\Schauenburg\09.03.18\Schauenburg Graphs\Excels\First Mounting 868.xlsx', sheetname='Sheet1')        #r needs to be there for location (raw string. Can use double backslashes or forward slashes)

data2 = [
    go.Scatterpolar(
        r = df2['x'],
        theta = df2['y'],
        mode = 'lines',name = 'MP1868',line =  dict(color = 'peru'))]

layout2 = go.Layout(
    title = 'UHF 1 Standard, UHF 2 Standard: Mounting Point 1 @ 868MHz',
    font = dict(family = 'Arial, sans-serif;', size = 12, color = '#000'),showlegend = False,
)

fig2 = go.Figure(data=data2, layout=layout2)
py.offline.plot(fig2, filename='my-graph2.html')

#==============================================================================