import time

from pymongo import MongoClient
import pprint
from bson.son import SON
import pandas as pd
import json

class MongoCon:
    def __init__(self, h, p,m):
        self.host = h
        self.port = p
        self.maxRange = m
        self.db = 'location'

        client = MongoClient(host=self.host, port=self.port)

        self.db = client['location']  # 이건 고정


    def findLocation(self, c, n):
        """

        :param c: 검색을 원하는 collection
        :param n: collection 내부에서 검색을 원하는 name
        :return: 좌표를 리스트로 return, 버스정류장은 2개 이므로 둘중 하나만 리턴 된다.
        """

        collection = self.db[c]  # 내가 무슨 컬렉션에서 좌표를 가져올 것인가? 변하는 것

        query = {"name": n}  # 해당 이름도 변하는 것.

        mydoc = collection.find(query)

        for x in mydoc:
            t = x['location']['coordinates']

        return t

    def private(self, l, min = 0):

        listing = list()

        query = {'location': {
            '$near': {'$geometry': {'type': "Point", 'coordinates': l},'$minDistance': min ,'$maxDistance': self.maxRange}}}

        for doc in self.db.private.find(query):
            listing.append(doc)

        return listing


    def bus(self, l, min = 0):

        listing = list()

        query = {'location': {
            '$near': {'$geometry': {'type': "Point", 'coordinates': l},'$minDistance': min ,'$maxDistance': self.maxRange}}}

        for doc in self.db.bus.find(query):
            listing.append(doc)

        return listing

    def real_estate(self, l, min = 0):

        listing = list()

        query = {'location': {
            '$near': {'$geometry': {'type': "Point", 'coordinates': l},'$minDistance': min ,'$maxDistance': self.maxRange}}}

        for doc in self.db.real_estate.find(query):
            listing.append(doc)

        return listing

    def school(self, l, min = 0):

        listing = list()

        query = {'location': {
            '$near': {'$geometry': {'type': "Point", 'coordinates': l},'$minDistance': min ,'$maxDistance': self.maxRange}}}

        for doc in self.db.school.find(query):
            listing.append(doc)

        return listing

    def subway(self, l, min = 0):

        listing = list()

        query = {'location': {
            '$near': {'$geometry': {'type': "Point", 'coordinates': l},'$minDistance': min ,'$maxDistance': self.maxRange}}}

        for doc in self.db.subway.find(query):
            listing.append(doc)

        return listing

    def getAllSchool(self):

        listing = list()

        for doc in self.db.school.find():
            listing.append(doc)

        return listing



# if __name__ == "__main__":
#
#
#
#     k = mongo.getAllSchool()
#
#     print(k)
    # location = mongo.findLocation('real_estate', '디엠씨엘가')
    #
    # k1 = mongo.real_estate(location, 1000)
    #
    # # print(k1)
    # # print(len(k1))
    # # 이렇게 좌표를 받고 구를 리턴을 받아야 한다.
    #
    # name = list()
    #
    # for i in range(0, len(k1)):
    #     # print(k1[i]['name'])
    #     name.append(k1[i]['name'])
    #
    # print(name)