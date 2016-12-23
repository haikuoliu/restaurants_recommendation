from utils.crossdomain import *
import json
from . import routes
from utils.recommendation import *
from utils.DaoLayer import *


# http://0.0.0.0:8080/api/restaurant/recommend/
@routes.route('/api/restaurant/recommend', methods=['GET', 'POST'])
@crossdomain(origin='*')
def recommend():
    try:
        lat = request.form['latitude']
        lng = request.form['longitude']
        uid = request.form['uid']
        # print lat
        # print lng
        # print uid
        ret = {"status": True}
        if uid == "empty_uid":
            ret["restaurant_infos"] = []
            return json.dumps(ret)
        # restaurant_infos = [
        #     {
        #         "rid": "reyes-deli-and-grocery-brooklyn",
        #         "name": "Reyes Deli & Grocery",
        #         "address": "addr A",
        #         "latitude": 40.75033,
        #         "longitude": -73.98531,
        #         "picUrl": "https://www.omnihotels.com/-/media/images/hotels/homrst/restaurants/homrst-omni-homestead-resort-jeffersons-restaurant-2.jpg",
        #         "overallRating": 4.5
        #     },
        #     {
        #         "rid": "coffee-project-new-york-new-york",
        #         "name": "Coffee Project New York",
        #         "address": "local B",
        #         "latitude": 40.7274823,
        #         "longitude": -73.9902387,
        #         "picUrl": "http://assets.sheratonseattle.com/lps/assets/u/she460re-119596-Daily-Grill-Restaurant.jpg",
        #         "overallRating": 5.0
        #     }
        # ]
        items = getUser2ItemRecommendation(uid, 2)
        items = json.loads(items)["recommendedItems"]
        # print items
        restaurant_infos = []
        for item in items:
            item["items"][0]["id"]
            restaurant_info = getByRestaurant_id(item["items"][0]["id"])
            restaurant_infos.append(restaurant_info)
            # print restaurant_info
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
            uid = request.form['uid']
            print uid
            print keyword
            # recommend logic
            ret = {"status": True}
            restaurant_infos = [
                {
                    "rid": "reyes-deli-and-grocery-brooklyn",
                    "name": "Reyes Deli & Grocery",
                    "address": "addr A",
                    "latitude": 40.75033,
                    "longitude": -73.98531,
                    "picUrl": "https://www.omnihotels.com/-/media/images/hotels/homrst/restaurants/homrst-omni-homestead-resort-jeffersons-restaurant-2.jpg",
                    "overallRating": 4.5
                },
                {
                    "rid": "coffee-project-new-york-new-york",
                    "name": "Coffee Project New York",
                    "address": "local B",
                    "latitude": 40.7274823,
                    "longitude": -73.9902387,
                    "picUrl": "http://assets.sheratonseattle.com/lps/assets/u/she460re-119596-Daily-Grill-Restaurant.jpg",
                    "overallRating": 5.0
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
            if uid == "empty_uid":
                ret["restaurant_info"] = {}
                return json.dumps(ret)
            restaurant_info = {
                "rid": "coffee-project-new-york-new-york",
                "name": "Coffee Project New York",
                "address": "local B",
                "latitude": 40.7274823,
                "longitude": -73.9902387,
                "picUrl": "http://assets.sheratonseattle.com/lps/assets/u/she460re-119596-Daily-Grill-Restaurant.jpg",
                "overallRating": 5.0
            }
            ret["restaurant_info"] = restaurant_info
            print ret
            return json.dumps(ret)
    except Exception, e:
        print e
        ret = {"status": False}
        return json.dumps(ret)
