# from utils.connect_db import *
from utils.constants_funcs import *
from utils.time_format import *
from utils.crossdomain import *
import json
from . import routes
from utils.connect_db import *


# Register a new user.
# http://127.0.0.1:8080/api/users/register
@routes.route('/api/users/register', methods=['GET', 'POST'])
@crossdomain(origin='*')
def user_register():
    if request.method == 'GET':
        try:
            user_name = request.args.get('name')
            user_email = request.args.get('email')
            user_pwd = request.args.get('pwd')
            user = {"user_name": user_name,
                    "user_email": user_email,
                    "user_pwd": user_pwd,
                    "register_date": datetime.datetime.utcnow()}
            db = get_db_connection()
            user_collection = db.user
            user_collection.insert_one(user).inserted_id
            ret = {"Status": "OK"}
            print ret
            return json.dumps(ret)
        except Exception, e:
            print e
            return default_error_msg(e.message)


# User login
# http://127.0.0.1:8080/api/users/login
@routes.route('/api/users/login', methods=['GET', 'POST'])
@crossdomain(origin='*')
def user_login():
    if request.method == 'GET':
        try:
            user_email = request.args.get('email')
            user_pwd = request.args.get('pwd')
            db = get_db_connection()
            user_collection = db.user
            query_results = user_collection.find_one({"user_name": user_email, "user_pwd": user_pwd})
            ret = {"Status": "OK"}
            if query_results != None:
                ret["login"] = True
            else:
                ret["login"] = False
            return json.dumps(ret)
        except Exception, e:
            print e
            return default_error_msg(e.message)
