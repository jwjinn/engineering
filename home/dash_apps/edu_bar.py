from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash
import pymysql
from home.models import *
from config import MARIADB_CONFIG

app = DjangoDash('edu')

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
fig02.update_layout(margin=dict(t=10, l=0, r=0, b=0))

app.layout = html.Div(children=[
    dcc.Graph(
        id='example-graph',
        figure=fig02,
        style={'height' : '430px'}
    ),


])






