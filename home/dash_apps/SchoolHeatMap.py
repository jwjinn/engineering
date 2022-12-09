from urllib.request import urlopen
from dash import Dash, html, dcc
import json
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from django_plotly_dash import DjangoDash
from ..models import *
from config import mapbox

# DjangoDash app 이름
app = DjangoDash('school_heatmap')

# mapbox token
token = mapbox['key']

# geojson 파일불러오기
with urlopen('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo.json') as response:
    gu = json.load(response)

# db와 연결할 key 설정
for x in gu['features']:
    x['id'] = x['properties']['name']

# db 불러오기 -> dataframe
schools = School.objects.all().values()
schools = pd.DataFrame(schools)

seoul_info = SeoulInfo.objects.all().values()
seoul_info = pd.DataFrame(seoul_info)

subway= Subway.objects.all().values()
subway = pd.DataFrame(subway)

bus = Bus.objects.all().values()
bus = pd.DataFrame(bus)

academy = Academy.objects.all().values()
academy = pd.DataFrame(academy)

real_estate = RealEstate.objects.all().values()
real_estate = pd.DataFrame(real_estate)

# 자치구 list
gugun = schools['gugun_id'].unique()

# 자치구별 평균 학생수 list
mean_student = []
for i in gugun:
    mean_student.append(schools[schools['gugun_id'] == i]['students_number'].mean().round())

# 자치구별 버스정류장 수
count_bus = []
for i in gugun:
    count_bus.append(bus[bus['gugun_id'] == i]['bus_station_id'].count())

# 자치구별 지하철역 수
count_subway = []
for i in gugun:
    count_subway.append(subway[subway['gugun_id'] == i]['subway_station_name'].count())

# 자치구별 학원 수
count_academy = []
for i in gugun:
    count_academy.append(academy[academy['gugun_id'] == i]['academy_name'].count())

# 자치구별 부동산 매매가 평균
mean_price = []
for i in gugun:
    mean_price.append(real_estate[real_estate['gugun_id'] == i]['price'].mean().round())

# 자치구, 학생수, 버스, 지하철, 학원, 부동산, 인구 -> dataframe
df_s = pd.DataFrame({'gugun' : gugun, 'student': mean_student, 'bus' : count_bus, 'subway' : count_subway,
                     'academy' : count_academy, 'real_estate_price' : mean_price, 'population': seoul_info['population']})


# subplot 만들기 (row:2, col:3)
fig = make_subplots(
    rows=2, cols=3, subplot_titles=['평균 학생수', '인구수', '부동산 거래가 평균', '버스정류장수', '지하철역수', '학원수' ],
    specs=[[{"type": "mapbox"}, {"type": "mapbox"}, {"type": "mapbox"}],
        [{"type": "mapbox"}, {"type": "mapbox"}, {"type": "mapbox"}]])

# graph
fig.add_trace(go.Choroplethmapbox(
    geojson=gu,
    locations=df_s.gugun,
    z = df_s.student,
    colorscale="Viridis"),
    row=1, col=1)

fig.add_trace(go.Choroplethmapbox(
    geojson=gu,
    locations=df_s.gugun,
    z = df_s.population,
    colorscale="Viridis"),
    row=1, col=2)

fig.add_trace(go.Choroplethmapbox(
    geojson=gu,
    locations=df_s.gugun,
    z = df_s.real_estate_price,
    colorscale="Viridis"),
    row=1, col=3)

fig.add_trace(go.Choroplethmapbox(
    geojson=gu,
    locations=df_s.gugun,
    z = df_s.bus,
    colorscale="Viridis"),
    row=2, col=1)

fig.add_trace(go.Choroplethmapbox(
    geojson=gu,
    locations=df_s.gugun,
    z = df_s.subway,
    colorscale="Viridis"),
    row=2, col=2)

fig.add_trace(go.Choroplethmapbox(
    geojson=gu,
    locations=df_s.gugun,
    z = df_s.academy,
    colorscale="Viridis"),
    row=2, col=3)

# graph layout
fig.update_layout(mapbox1=dict(style="carto-positron",
                  zoom=8.2, center = {"lat": 37.5453029, "lon": 126.9894348}, accesstoken = token),
                  mapbox2=dict(style="carto-positron",
                               zoom=8.2, center={"lat": 37.5453029, "lon": 126.9894348}, accesstoken=token),
                  mapbox3=dict(style="carto-positron",
                            zoom=8.2, center = {"lat": 37.5453029, "lon": 126.9894348}, accesstoken = token),
                  mapbox4=dict(style="carto-positron",
                               zoom=8.2, center={"lat": 37.5453029, "lon": 126.9894348}, accesstoken=token),
                  mapbox5=dict(style="carto-positron",
                            zoom=8.2, center = {"lat": 37.5453029, "lon": 126.9894348}, accesstoken = token),
                  mapbox6=dict(style="carto-positron",
                            zoom=8.2, center = {"lat": 37.5453029, "lon": 126.9894348}, accesstoken = token),
                  margin={"r":0,"t":20,"l":0,"b":0},
                  )



# app layout
app.layout = html.Div(
    # style={"background-color":"red", "overflow": "auto"},
    children=[
    dcc.Graph(
        id='example-graph',
        figure=fig,
    )
])



