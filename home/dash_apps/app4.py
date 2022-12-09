import pandas as pd
from dash import Dash, html, dcc, Input, Output
from django_plotly_dash import DjangoDash
import plotly.express as px
from home.models import *
from mongo.mongoConnect import *
from config import mapbox

# DjangoDash app 이름
app = DjangoDash('school_map')

# db불러오기 -> dataframe
schools = School.objects.all().values()
school = pd.DataFrame(schools)

# 위도, 경도
mongo = MongoCon('34.64.138.45', 27017, 1000)
k = mongo.getAllSchool()

name = []
latitude = []
longitude = []
for i in range(len(k)):
    name.append(k[i]['name'])
    latitude.append(k[i]['location']['coordinates'][1])
    longitude.append(k[i]['location']['coordinates'][0])
df = pd.DataFrame({'school_name': name, 'latitude': latitude, 'longitude' : longitude})

# school_name 으로 join
schools = school.merge(df, on='school_name', how='inner')
print(schools)
schools.columns = ["school_id", "gugun_id", "학교명", "school_level", "학생수",
                   "교사수", "학급당 학생수", "school_address", "latitude", "longitude"]
# mapbox token set
px.set_mapbox_access_token(mapbox['key'])

# graph 그리기
fig = px.scatter_mapbox(schools, lat="latitude", lon="longitude", color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                    hover_data={"학교명":True, '학생수':True, '교사수':True, '학급당 학생수':True,
                                "school_level":False, "latitude":False, "longitude":False}, width=800, height=600, color='school_level')

# graph layout
fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0})

# app layout
app.layout = html.Div(
    # style={"background-color":"red", "overflow": "auto"},
    children=[
    dcc.Graph(
        id='example-graph',
        figure=fig,
        style={'width': '300px', 'height' : '500px'}
    ),
])


