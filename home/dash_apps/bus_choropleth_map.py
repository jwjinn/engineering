import pandas as pd
import requests
import json
import plotly.express as px
from dash import Dash, html, dcc
from django_plotly_dash import DjangoDash
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "engineering.settings")
django.setup()
from home.models import Bus

app = DjangoDash("bus_choropleth_map")


# df
bus = Bus.objects.all().values()
df = pd.DataFrame(bus)
df = df.groupby('gugun_id').size().to_frame(name='count').reset_index()
df = pd.DataFrame(df)


# geojson
r = requests.get('https://github.com/Luna252/southKorea_geojson/raw/main/southKorea.zip.geojson')
c = r.content
seoul_geo = json.loads(c)


# figure
fig = px.choropleth_mapbox(df, geojson=seoul_geo, locations='gugun_id', color='count',
                           color_continuous_scale="Agsunset", range_color=(200,1000),
                           mapbox_style="carto-positron", featureidkey="properties.SIG_KOR_NM",
                           zoom=9.5, center={'lat' : 37.56421, "lon" :127.00169 },
                           opacity=0.8, labels={'cnt_station' : '자치구별 버스정류장수'})


fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


# html
app.layout = html.Div([
        dcc.Graph(id='map_graph', figure=fig)], style={'width' : '98%'})
