from utils.crossdomain import *
import json
from . import routes


# http://0.0.0.0:8080/api/restaurant/recommend/
@routes.route('/api/restaurant/recommend', methods=['GET', 'POST'])
@crossdomain(origin='*')
def recommend():
    if request.method == 'POST':
        try:
            lat = request.args.get('lat')
            lng = request.args.get('lng')
            uid = request.args.get('uid')
            # db = get_db_connection()
            # restaurant_collection = db.restaurant
            # query_results = restaurant_collection.find_one({"rid": rid})

            # get several rids here by recommend algorithm.

            rids = [1, 2, 3]
            restaurant_infos = []
            for rid in rids:
                # search in db and get detailed info of restaurant
                restaurant_info = {}
                restaurant_infos.append(restaurant_info)
            ret = {"status": True}
            restaurant_infos = {
                {
                    "rid": "A",
                    "name": "restaurant A",
                    "location": "local A",
                    "lat": 1,
                    "lng": 2,
                    "description": "description A"
                },
                {
                    "rid": "B",
                    "name": "restaurant B",
                    "location": "local B",
                    "lat": 3,
                    "lng": 4,
                    "description": "description B"
                },
            }
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
            uid = request.args.get('uid')
            keyword = request.args.get('keyword')
            # recommend logic
            ret = {}
            ret["recommend_rid"] = ""
            print ret
            return json.dumps(ret)
        except Exception, e:
            print e
            ret = {"status": False}
            return json.dumps(ret)
