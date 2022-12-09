from dash import Dash, html, dcc
import plotly.graph_objects as go
import pandas as pd
from django_plotly_dash import DjangoDash
from ..models import *

# DjangoDash app 이름
app = DjangoDash('student_teacher_class')

# db 불러오기 -> dataframe
schools = School.objects.all().values()
df = pd.DataFrame(schools)

# gugun list
gugun = df['gugun_id'].unique()

# gugun별 총 학생수 list
students = []
for i in gugun:
    students.append(df[df['gugun_id'] == i]['students_number'].sum())

# gugun별 총 교사수 list
teachers = []
for i in gugun:
    teachers.append(df[df['gugun_id'] == i]['teachers_number'].sum())

# gugun별 과밀학급수 list
overcrowded = []
for i in gugun:
    overcrowded.append(df[(df['gugun_id'] == i) & (df['students_per_class'] >= 28)]['school_id'].count())

# 총학생수, 총교사수, 과밀학급수 -> dataframe
df_s = pd.DataFrame({'gugun' : gugun, 'sum_students': students, 'sum_teachers' : teachers, 'overcrowded_class' : overcrowded})

# graph 그리기
fig = go.Figure()

fig.add_trace(go.Scatter(x=df_s['gugun'], y=df_s['sum_students'],
                    mode='lines+markers',
                    name='총학생수'))
fig.add_trace(go.Scatter(x=df_s['gugun'], y=df_s['sum_teachers'],
                    mode='lines+markers',
                    name='총교사수' , yaxis="y2"))
fig.add_trace(go.Scatter(x=df_s['gugun'], y=df_s['overcrowded_class'],
                    mode='lines+markers',
                    name='과밀학급수' , yaxis="y3"))

# Create axis objects
# y축 추가
fig.update_layout(
    xaxis=dict(
        domain=[0.05, 1]
    ),
    yaxis=dict(
        title="학생수",
        titlefont=dict(
            color="#1f77b4"
        ),
        tickfont=dict(
            color="#1f77b4"
        )
    ),
    yaxis2=dict(
        title="교사수",
        titlefont=dict(
            color="#1f77b4"
        ),
        tickfont=dict(
            color="#1f77b4"
        ),
        anchor="free",
        overlaying="y",
        side="left",
        position=0
    ),
    yaxis3=dict(
        title="과밀학급수",
        titlefont=dict(
            color="#1f77b4"
        ),
        tickfont=dict(
            color="#1f77b4"
        ),
        anchor="x",
        overlaying="y",
        side="right"
    ),
    margin={"r":0,"t":20,"l":0,"b":0},

)


# app layout
app.layout = html.Div(
    # style={"background-color":"red", "overflow": "auto"},
    children=[
    dcc.Graph(
        id='example-graph',
        figure=fig,
        #style={'width': '1000px', 'height' : '500px'}
    ),
])

