import plotly as py
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/polar_dataset.csv")
df1 = pd.read_excel(r'C:\Users\Hans-PC\Desktop\New folder\Testing.xlsx', sheetname='Sheet1')        #r needs to be there for location (raw string. Can use double backslashes or forward slashes)

data = [
    go.Scatterpolar(
        r = df['x1'],
        theta = df['y'],
        mode = 'lines',name = 'Figure8',line =  dict(color = 'peru')),
                    
    go.Scatterpolar(
        r = df['x2'],
        theta = df['y'],
        mode = 'lines',name = 'Cardioid',line =  dict(color = 'darkviolet')),
                    
    go.Scatterpolar(
        r = df['x3'],
        theta = df['y'],
        mode = 'lines',name = 'Hypercardioid',line =  dict(color = 'deepskyblue')),
                    
    go.Scatterpolar(
        r = df['x4'],
        theta = df['y'],
        mode = 'lines',name = 'orangered', line =dict(color = 'orangered')),
                    
    go.Scatterpolar(
        r = df['x5'],
        theta = df['y'],
        mode = 'lines',name = 'Supercardioid',line =  dict(color = 'green'))
    ]

layout = go.Layout(
    title = 'Mic Patterns',
    font = dict(family = 'Arial, sans-serif;', size = 12, color = '#000'),showlegend = False)

fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig)

