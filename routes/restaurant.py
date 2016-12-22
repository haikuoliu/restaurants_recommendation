from utils.crossdomain import *
import json
from . import routes


# http://0.0.0.0:8080/api/restaurant/recommend/
@routes.route('/api/restaurant/recommend', methods=['GET', 'POST'])
@crossdomain(origin='*')
def recommend():
    try:
        lat = request.form['latitude']
        lng = request.form['longitude']
        uid = request.form['uid']
        print lat
        print lng
        print uid
        # db = get_db_connection()
        # restaurant_collection = db.restaurant
        # query_results = restaurant_collection.find_one({"rid": rid})
        # get several rids here by recommend algorithm.

        rids = [1, 2, 3]
        restaurant_infos = []
        # for rid in rids:
        #     # search in db and get detailed info of restaurant
        #     restaurant_info = {}
        #     restaurant_infos.append(restaurant_info)
        ret = {"status": True}
        if uid == "EMPTY_UID":
            ret["restaurant_infos"] = []
            return json.dumps(ret)
        restaurant_infos = [
            {
                "rid": "A",
                "name": "restaurant A",
                "address": "addr A",
                "latitude": 1,
                "longitude": 2,
                "picUrl": "http://A1"
            },
            {
                "rid": "B",
                "name": "restaurant B",
                "address": "local B",
                "latitude": 3,
                "longitude": 4,
                "picUrl": "description B"
            }
        ]
        ret["restaurant_infos"] = restaurant_infos
        print ret
        return json.dumps(ret)
    except Exception, e:
        print e
        ret = {"status": False}
        return json.dumps(ret)


@routes.route('/api/restaurant/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        try:
            keyword = request.form['keyword']
            print keyword
            # recommend logic
            ret = {"status": True}
            restaurant_infos = [
                {
                    "rid": "A",
                    "name": "restaurant A",
                    "address": "addr A",
                    "latitude": 1,
                    "longitude": 2,
                    "picUrl": "http://A1"
                },
                {
                    "rid": "B",
                    "name": "restaurant B",
                    "address": "local B",
                    "latitude": 3,
                    "longitude": 4,
                    "picUrl": "description B"
                }
            ]
            ret["restaurant_infos"] = restaurant_infos
            print ret
            return json.dumps(ret)
        except Exception, e:
            print e
            ret = {"status": False}
            return json.dumps(ret)


@routes.route('/api/restaurant/recommend_realtime', methods=['GET', 'POST'])
@crossdomain(origin='*')
def recommend_realtime():
    try:
        if request.method == 'POST':
            lat = request.form['latitude']
            lng = request.form['longitude']
            uid = request.form['uid']
            print lat
            print lng
            print uid
            # db = get_db_connection()
            # restaurant_collection = db.restaurant
            # query_results = restaurant_collection.find_one({"rid": rid})
            # get several rids here by recommend algorithm.

            rids = [1, 2, 3]
            # for rid in rids:
            #     # search in db and get detailed info of restaurant
            #     restaurant_info = {}
            #     restaurant_infos.append(restaurant_info)
            ret = {"status": True}
            if uid == "EMPTY_UID":
                ret["restaurant_info"] = {}
                return json.dumps(ret)
            restaurant_info = {
                "rid": "B",
                "name": "restaurant B",
                "address": "local B",
                "latitude": 3,
                "longitude": 4,
                "picUrl": "description B"
            }
            ret["restaurant_info"] = restaurant_info
            print ret
            return json.dumps(ret)
    except Exception, e:
        print e
        ret = {"status": False}
        return json.dumps(ret)
