import plotly.express as px
import pymysql.cursors
import pandas as pd
import dash
from dash import Dash, html, dcc, Output, Input
from django_plotly_dash import DjangoDash
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "engineering.settings")
django.setup()


app = DjangoDash("bus_scatter_map")


# pymysql
connect = pymysql.connect(host='34.64.138.45',port=3306,user='shin',
    passwd='asdf1234!!',db='education',charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)
cursor = connect.cursor()


# query
sql = "select bus_station_id, bus_station_name, latitude, longitude from bus_location"
cursor.execute(sql)
result = cursor.fetchall()
connect.close()
df = pd.DataFrame(result)


# figure
fig = px.scatter_mapbox(df, lat='latitude', lon='longitude', hover_name='bus_station_name',
                        hover_data=['bus_station_id','bus_station_name'],
                        color_discrete_sequence=['LightSalmon'],
                        zoom=10, height=600, opacity=0.3).update_layout(mapbox_style='carto-positron').update_layout(margin={'r':0, 't':0, 'l':0, 'b':0})


# html
app.layout = html.Div([
        dcc.Graph(id='map_graph', figure=fig)], style={'width' : '800px'})

