from pymongo import MongoClient
import os

DATABASE = MongoClient()['akshara_database'] # DB_NAME
DEBUG = True
#MongoClient('localhost', 27017)
client = MongoClient('localhost', 27017)