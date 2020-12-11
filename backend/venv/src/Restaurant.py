from .model import *
from .helper import *


session = initDatabase()

class Restaurant():
    def create(self, rid, detail, promotion, tableRemain, name):
        restaurant = RESTAURANT(rid=rid, detail=detail, promotion=promotion, tableRemain=int(tableRemain), name=name)
        session.add(restaurant)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log
    
    def read(self, rid):
        print(type(rid))
        restaurant = session.query(RESTAURANT)
        restaurant = restaurant.filter(RESTAURANT.rid==rid)
        print(restaurant)
        if restaurant.scalar() is not None :
            restaurant = self.serialize(restaurant.one())
            log = {
                "result":restaurant,
                "msg":"",
                "status":"1"
            }
            return log
        else:
            log = {
                "result":"",
                "msg":"Not found",
                "status":"100"
            }
            return log

    def update(self, rid, detail, promotion, tableRemain, name):
        restaurant = session.query(RESTAURANT)
        restaurant = restaurant.filter(RESTAURANT.rid==rid)
        if restaurant.scalar() is not None :
            restaurant = restaurant.one()
            restaurant.detail = detail
            restaurant.promotion = promotion
            restaurant.tableRemain = int(tableRemain)
            restaurant.name = name
            session.commit()
            log = {
                "result":"",
                "msg":"",
                "status":"1"
            }
            return log
        else:
            log = {
                "result":"",
                "msg":"User not found",
                "status":"100"
            }
            return log

    def delete(self, rid):
        restaurant = session.query(RESTAURANT)
        restaurant = restaurant.filter(RESTAURANT.rid==rid)
        if restaurant.scalar() is not None :
            session.delete(restaurant.one())
            session.commit()
            log = {
                "result":"",
                "msg":"",
                "status":"1"
            }
            return log
        else:
            log = {
                "result":"",
                "msg":"User not found",
                "status":"100"
            }
            return log

    def getAllRestaurant(self):
        restaurants = session.query(RESTAURANT).all()
        restaurants = [self.serialize(restaurant) for restaurant in restaurants]
        log = {
            "result":restaurants,
            "msg":"",
            "status":"1"
        }
        return log

    def serialize(self, object):
        return {
            'rid': object.rid,
            'detail': object.detail,
            'promotion': object.promotion,
            'tableRemain': object.tableRemain,
            'name': object.name,
        }