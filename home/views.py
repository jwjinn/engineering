import json
import os.path

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import pandas as pd
import math
from config import MARIADB_CONFIG

from mongo.mapPrice import *
from mongo.mongoConnect import *
#ImportError: attempted relative import beyond top-level package


# 클래스를 사용하고 싶으면 클래스 명을 import에 적으면 되는가?
# 절대경로로 mongo폴더에 mongoConnect.py를 사용하고 싶다.

def index(request):
    return render(request, 'index.html')

def academy(request):
    return render(request, 'academy.html')

def bus(request):
    return render(request, 'bus.html')

def education_budget(request):
    return render(request, 'education_budget.html')

def real_estate(request):
    return render(request, 'real_estate.html')

def school(request):
    return render(request, 'school.html')

def subway(request):
    return render(request, 'subway.html')

def map(request):
    return render(request, 'map.html')

def mapractice(request):
    return render(request, 'mapractice.html')

def ajax(request):
    return render(request, 'ajax.html')

def show_eng(request):
    input_val = request.GET.get('input_val')
    print(input_val)

    if input_val =='사과':
        eng = 'apple'
    elif input_val == '포도':
        eng = 'grape'
    else:
        eng = "과일이 아님 혹은 등록된 과일이 아님."

    context = {'eng' : eng}
    return JsonResponse(context)

def geoInfo(request):
    input_val = request.GET.get('input_val')
    # global meanPrice

    private = []
    bus = []
    real_estate = []
    school = []
    subway = []

    """
    script에서 받은 연도와 거리가 숫자가 아니면, 필터링.
    """

    try:
        input_year = int(request.GET.get('year'))
    except ValueError as e:
        input_year = 2022

    try:
        input_range = int(request.GET.get('range'))
    except ValueError as e:
        input_range = 1000


    print("input_year: "+ str(input_year))
    print("input_range: "+ str(input_range))

    latStart = input_val.find(':') + 1
    longStart = input_val.rfind(':')+1

    sep = input_val.find(',')
    longEnd = input_val.find(')')

    latitude = input_val[latStart : sep]
    longitude = input_val[longStart : longEnd]

    geo = [float(longitude), float(latitude)]

    reverseCor = reverseGeo(geo)


    # print(geo)

    mongo = MongoCon(MongoDB_config['host'], MongoDB_config['port'], input_range)





    private = mongo.private(geo)
    bus = mongo.bus(geo)
    real_estate = mongo.real_estate(geo)
    school = mongo.real_estate(geo)
    subway = mongo.subway(geo)

    try:
        temp = pd.DataFrame(mongo.real_estate(geo)).iloc[:, 1]
        """
        mongo에서 geo쿼리를 통해서 가져온 이름을 컬럼으로 데이터프레임으로 만든다.
        """
        geoBuilding = pd.DataFrame(temp)


        reverseCor.request()
        dbCon = Mariadb(MARIADB_CONFIG['host'], MARIADB_CONFIG['user'],
                    MARIADB_CONFIG['password'], MARIADB_CONFIG['database'],
                    MARIADB_CONFIG['charset'])
        dbCon.setCon()

        result = dbCon.selectGuYear(reverseCor.returnGu(), input_year)

        """
        db에서 리버스 지오로 얻은 구 정보를 이용하여, 쿼리를 보낸 결과를 
        
        이름과 가격 컬럼으로 데이터 프레임을 리턴을 한다.
        """
        # result = dbCon.selectGu(reverseCor.returnGu())

        # print(result)

        dbMerge = pd.merge(left=geoBuilding, right=result, how='inner', left_on='name', right_on='building_name')
        # print(ttt)
        # print(ttt['price'].mean())

        print(len(dbMerge))
        print(dbMerge)


        meanPrice = round(dbMerge['price'].mean())

    except ValueError as e:
        print(e)
        print("해당 연도에 해당 범위에 부동산이 조회되지 않았을 경우")
        meanPrice = -1
        real_estate = []

    except UnboundLocalError as e:
        print(e)
        print("이상값 입력으로 인한, 데이터프레임 조인 안됨.")
        meanPrice = 0

    except IndexError as e:
        # mongoDB가 조회가 안될 경우.
        print(e)
        print("mongo outOfIndex")





    try:
        context = {'private': len(private),
                   'bus': len(bus),
                   'real_estate': len(real_estate),
                   'school': len(school),
                   'subway': len(subway),
                   'meanPrice': meanPrice}
        return JsonResponse(context)

    except UnboundLocalError as e:
        print("unbound")

def projectPlan(request):
    return render(request, 'project.html')


# notion_wireFrame
def subwaybusprivate(request):
    return render(request, 'subwaybusprivate.html')

def jeong(request):
    return render(request, 'jeong.html')

def lee(request):
    return render(request, 'lee.html')