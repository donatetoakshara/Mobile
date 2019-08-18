from pymongo import MongoClient
import os

DATABASE = MongoClient()[os.environ.get("DB_NAME",default=False)] # DB_NAME
DEBUG = True
#MongoClient('localhost', 27017)
client = MongoClient(os.environ.get("MONGODB_URL",default=False))