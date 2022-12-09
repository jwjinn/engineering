import pandas as pd
import numpy as np
from dash import Dash, html, dcc
import plotly.express as px
from ..models import *
from django_plotly_dash import DjangoDash

# DjangoDash app 이름
app = DjangoDash('school_num')

# db 불러오기 -> dataframe
schools = School.objects.all().values()
df01 = pd.DataFrame(schools)

# 자치구별 전체 학교수
group01 = df01.groupby('gugun_id')['school_id'].count().reset_index()
# 자치구별 초등학교수
group02 = df01.query("school_level in '초등학교'").groupby('gugun_id')['school_id'].count().reset_index()
# 자치구별 중학교수
group03 = df01.query("school_level in '중학교'").groupby('gugun_id')['school_id'].count().reset_index()
# 자치구별 고등학교수
group04 = df01.query("school_level in '고등학교'").groupby('gugun_id')['school_id'].count().reset_index()

# 자치구, 전체학교수, 초등학교수, 중학교수, 고등학교수 -> dataframe
df02 = pd.concat([group01, group02['school_id'], group03['school_id'], group04['school_id']], axis=1)

# 컬럼명 변경
df02.columns = ["gugun", "total", "elementary", "middle", "high"]

# graph 그리기
fig01 = px.bar(df02, x='gugun', y="total", text_auto='.2s')
fig02 = px.bar(df02, x='gugun', y="elementary", text_auto='.2s')
fig03 = px.bar(df02, x='gugun', y="middle", text_auto='.2s')
fig04 = px.bar(df02, x='gugun', y="high", text_auto='.2s')


# app layout
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='전체', children=[
            dcc.Graph(
                figure=fig01
            )
        ]),
        dcc.Tab(label='초등학교', children=[
            dcc.Graph(
                figure=fig02
            )
        ]),
        dcc.Tab(label='중학교', children=[
            dcc.Graph(
                figure=fig03
            )
        ]),
        dcc.Tab(label='고등학교', children=[
            dcc.Graph(
                figure=fig04
            )
        ])
    ])
])
