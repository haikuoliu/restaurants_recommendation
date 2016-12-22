from utils.crossdomain import *
import json
from . import routes
from utils.connect_db import *


# Register a new user.
# http://127.0.0.1:8080/api/users/register
@routes.route('/api/users/register', methods=['GET', 'POST'])
@crossdomain(origin='*')
def user_register():
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            print username
            print email
            print password
            user = {
                    "username": username,
                    "email": email,
                    "password": password
            }
            # db = get_db_connection()
            # user_collection = db.user
            # return uid and profile.
            # user_collection.insert_one(user).inserted_id

            is_exists = False
            if is_exists:
                ret = {"status": False}
            else:
                user_profile = {
                    "uid": "123",
                    "username": "liuhaikuo",
                    "password": "pwd",
                    "tag": ["food catagory1", "food catagory2"],
                    "search_history": ["keyword1", "keyword2"]
                }
                ret = {"status": True}
                ret["user_profile"] = user_profile
            print ret
            return json.dumps(ret)

        except Exception, e:
            print e
            ret = {"status": False}
            return json.dumps(ret)


# User login
# http://127.0.0.1:8080/api/users/login
@routes.route('/api/users/login', methods=['GET', 'POST'])
@crossdomain(origin='*')
def user_login():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            db = get_db_connection()
            user_collection = db.user
            query_results = user_collection.find_one({"email": email, "password": password})
            is_success = True
            if is_success:
                user_profile = {
                    "uid": "123",
                    "username": "liuhaikuo",
                    "password": "pwd",
                    "tag": ["food catagory1", "food catagory2"],
                    "search_history": ["keyword1", "keyword2"]
                }
                ret = {"status": True}
                ret["user_profile": user_profile]
            else:
                ret = {"status": False}
            print ret
            return json.dumps(ret)
        except Exception, e:
            print e
            ret = {"status": False}
            return json.dumps(ret)
