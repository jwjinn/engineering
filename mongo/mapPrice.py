import requests
import pandas as pd
import numpy as np
import pymysql
from config import *
from config import Naver_config

"""
지도를 클릭했을때, 1km안 평균 가격이 나오게

"""

class Mariadb:

    def __init__(self, h, u, p, d, c):
        self.host = h
        self.user = u
        self.password = p
        self.database = d
        self.charset = c

    def setCon(self):
        """
        connection create
        :return:
        """
        connection = pymysql.connect(
            host = self.host,
            user = self.user,
            password= self.password,
            database= self.database,
            charset= self.charset
        )

        self.cur = connection.cursor()

    def selectQuery(self, q):
        """
        전체 쿼리문을 string 타입으로 입력을 할 경우.
        :param q: query string
        :return: tuple
        """
        self.cur.execute(q)

        return self.cur.fetchall()

    def selectGu(self, gu):

        """
        구만 입력을 하고 부동산 가격의 정보를 알고 싶은 경우
        :param gu: 구
        :return: (building_name, price) pandas DF type
        """
        query = f"select building_name, price from real_estate where gugun = '{gu}'"
        # query = f"select building_name, price from real_estatewhere where gugun = '{gu}' and EXTRACT(yearfrom contract_date) = '{y}'"

        self.cur.execute(query)

        return pd.DataFrame(self.cur.fetchall(), columns=['building_name','price'])

    def selectGuYear(self, gu, y):

        # query = f"select building_name, price from real_estate where gugun = '{gu}'"
        query = f"select building_name, price from real_estate where gugun = '{gu}' and EXTRACT(year from contract_date) = '{y}'"

        self.cur.execute(query)

        return pd.DataFrame(self.cur.fetchall(), columns=['building_name','price'])





class reverseGeo:
    def __init__(self, coor):
        self.client_id = Naver_config['client_id']
        self.client_secret = Naver_config['client_secret']
        self.endpoint = "https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc?request=coordsToaddr&coords="
        self.back = "&sourcecrs=epsg:4326&output=json"

        self.longitude = coor[0]
        self.latitude = coor[1]

    def request(self):

        url = self.endpoint+str(self.longitude)+","+str(self.latitude)+self.back
        headers = {
            "X-NCP-APIGW-API-KEY-ID": self.client_id,
            "X-NCP-APIGW-API-KEY": self.client_secret,
        }

        res = requests.get(url, headers=headers)

        self.response = res.json()

    def returnGu(self):
        return self.response['results'][0]['region']['area2']['name']

    def returnSi(self):
        return self.response['results'][0]['region']['area1']['name']





if __name__ == "__main__":
    k = reverseGeo([126.9830982, 37.5628708])
    k.request()
    gu = k.returnGu()
    si = k.returnSi()

    print(si)

    # maria = Mariadb(pw.mariadb())
    maria = Mariadb(MARIADB_CONFIG['host'], MARIADB_CONFIG['user'],
                    MARIADB_CONFIG['password'], MARIADB_CONFIG['database'],
                    MARIADB_CONFIG['charset'])
    maria.setCon()

    print(maria.selectGuYear('중구',2020))
