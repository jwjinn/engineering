from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash
import pymysql
from home.models import *
from config import MARIADB_CONFIG


app = DjangoDash('edu02')

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
db = pymysql.connect(host=MARIADB_CONFIG['host'],user=MARIADB_CONFIG['user'],
                    passwd=MARIADB_CONFIG['password'], db=MARIADB_CONFIG['database'], 
                    charset=MARIADB_CONFIG['charset'])

seoul = SeoulInfo.objects.all().values()
seoul = pd.DataFrame(seoul)
school = School.objects.all().values()
school = pd.DataFrame(school)

gugun = school['gugun_id'].unique()
pop = seoul['population']
stu =[]
tea =[]
bud = []

for i in gugun:
    stu.append(school[school['gugun_id'] == i]["students_number"].sum())

for i in gugun:
    tea.append(school[school['gugun_id'] == i]["teachers_number"].sum())


cursor = db.cursor()

sql = "select * from education_budgets"
cursor.execute(sql)

result = cursor.fetchall()

df = pd.DataFrame(result)

df.columns=['gugun','detail_code','budget','code_name']
df01=df.groupby('gugun').sum().reset_index()
bud =df01['budget']

df_s = pd.DataFrame({'gugun':gugun,'pop':pop
                     ,'stu':stu,'tea':tea,'bud':bud
                     })

fig02 = px.bar(df, x="gugun", y="budget", color="code_name")

app.layout = html.Div([
    dcc.Tabs(id='yaxis-type',value='bud',
             children=[
                dcc.Tab(label= "인구수", value= 'pop'),
                dcc.Tab(label= "학생수", value= 'stu'),
                dcc.Tab(label= "교원수", value= 'tea')]
    ),
    dcc.Graph(
        id='graph',
        style={'height' : '370px'}
        )]
)


@app.callback(
    Output('graph', 'figure'),
    Input('yaxis-type', 'value'),
)
def update_graph(yaxis_type):
    fig = fig = px.scatter(df_s, x='bud', y=yaxis_type, color='gugun',size='bud')
    fig.update_layout(margin=dict(t=20, l=0, r=0, b=0))
    return fig




