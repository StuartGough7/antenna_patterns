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
py.offline.plot(fig, filename='StandMP1_2.4G.html')


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
py.offline.plot(fig2, filename='StandMP1_868.html')

#==============================================================================

df3 = pd.read_excel(r'C:\Users\Hans-PC\Desktop\Stuart\Companies\Schauenburg\09.03.18\Schauenburg Graphs\Excels\Second Mounting 2.4G.xlsx', sheetname='Sheet1')        #r needs to be there for location (raw string. Can use double backslashes or forward slashes)

data3 = [
    go.Scatterpolar(
        r = df3['x'],
        theta = df3['y'],
        mode = 'lines',name = 'MP224G',line =  dict(color = 'peru'))]

layout3 = go.Layout(
    title = 'UHF 1 Standard, UHF 2 Standard: Mounting Point 2 @ 2.4GHz',
    font = dict(family = 'Arial, sans-serif;', size = 12, color = '#000'),showlegend = False,
)

fig3 = go.Figure(data=data3, layout=layout3)
py.offline.plot(fig3, filename='StandMP2_2.4G.html')

#==============================================================================

df4 = pd.read_excel(r'C:\Users\Hans-PC\Desktop\Stuart\Companies\Schauenburg\09.03.18\Schauenburg Graphs\Excels\Second Mounting 868.xlsx', sheetname='Sheet1')        #r needs to be there for location (raw string. Can use double backslashes or forward slashes)

data4 = [
    go.Scatterpolar(
        r = df4['x'],
        theta = df4['y'],
        mode = 'lines',name = 'MP2868',line =  dict(color = 'peru'))]

layout4 = go.Layout(
    title = 'UHF 1 Standard, UHF 2 Standard: Mounting Point 2 @ 868MHz',
    font = dict(family = 'Arial, sans-serif;', size = 12, color = '#000'),showlegend = False,
)

fig4 = go.Figure(data=data4, layout=layout4)
py.offline.plot(fig4, filename='StandMP2_868.html')

#==============================================================================