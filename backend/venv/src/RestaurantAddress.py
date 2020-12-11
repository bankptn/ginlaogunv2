
from .model import *
from .helper import *


session = initDatabase()

class RAddress():
    def create(self, rid, street, province, country, zip):
        address = RESTAURANT_ADDRESS(rid=rid, street=street, province=province, country=country, zip=zip)
        session.add(address)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log
    
    def read(self, rid):
        address = session.query(RESTAURANT_ADDRESS)
        address = address.filter(RESTAURANT_ADDRESS.rid==rid)
        if address.scalar() is not None :
            address = self.serialize(address.one())
            log = {
                "result":address,
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

    def update(self, rid, street, province, country, zip):
        address = session.query(RESTAURANT_ADDRESS)
        address = address.filter(RESTAURANT_ADDRESS.rid==rid)
        if address.scalar() is not None :
            address = address.one()
            address.street = street
            address.province = province
            address.country = country
            address.zip = zip
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
        address = session.query(RESTAURANT_ADDRESS)
        address = address.filter(RESTAURANT_ADDRESS.rid==rid)
        if address.scalar() is not None :
            session.delete(address.one())
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

    def getAllRestaurantAddress(self):
        addresss = session.query(RESTAURANT_ADDRESS).all()
        addresss = [self.serialize(addresss) for address in addresss]
        log = {
            "result":addresss,
            "msg":"",
            "status":"1"
        }
        return log

    def serialize(self, object):
        return {
            'rid': object.rid,
            'street': object.street,
            'province': object.province,
            'country': object.country,
            'zip': object.zip,
        }
