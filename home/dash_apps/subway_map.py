import plotly.express as px
import pandas as pd
from dash import html, dcc
from django_plotly_dash import DjangoDash
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "engineering.settings")
django.setup()
from mongo.mongoConnect import *
from home.models import Subway

app = DjangoDash("subway_map")


# df
subway = Subway.objects.all().values()
df = pd.DataFrame(subway)
df = df[['subway_station_name', 'gugun_id']]


# df -> dict
df_dict = df.to_dict()
dict_name = df_dict['subway_station_name'].values()
dict_gugun = df_dict['gugun_id'].values()
name_list = list(dict_name)
gugun_list = list(dict_gugun)
lat_list = []
lon_list = []


# mongo
mongo = MongoCon('34.64.138.45', 27017, 1000)
for i in range(0, len(name_list)) :
    location = mongo.findLocation('subway', name_list[i])
    lon_list.append(location[0])
    lat_list.append(location[1])

subway_dict = {'subway_station_name' : name_list,
               'gugun' : gugun_list,
               'lat' : lat_list,
               'lon' : lon_list}

subway_df = pd.DataFrame(subway_dict)


# figure
fig = px.scatter_mapbox(subway_df, lat='lat', lon='lon', hover_name='subway_station_name',
                        hover_data=['gugun'],
                        color_discrete_sequence=['purple'],
                        zoom=10, height=600).update_layout(mapbox_style='carto-positron').update_layout(margin={'r':0, 't':0, 'l':0, 'b':0})


# html
app.layout = html.Div([
        dcc.Graph(id='map_graph', figure=fig)], style={'width' : '1000px'})
