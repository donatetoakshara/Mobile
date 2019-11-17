import functools
import json
import os
from bson import json_util
import flask
from flask import jsonify
from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import google_auth

from config import client
from bson.json_util import dumps

app=flask.Blueprint('users', __name__)


db = client.akshara_database

collection = db.users

@app.route("/user/")
def user():
    try:
        if google_auth.is_logged_in():
            user_info = google_auth.get_user_info()
            find_user = collection.find({},{"id": int(user_info['id'])})
            print(find_user.count())
            if find_user.count() == 0:
                collection.insert(user_info)
            return json.dumps(user_info, indent=4, default=json_util.default), 200
        
        return 'You are not currently logged in', 401
    except:
        return 'Something went wrong sorry for the inconvienence', 500
        
       
