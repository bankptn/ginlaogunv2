from .model import *
from .helper import *

session = initDatabase()

class Reservation():
    def create(self, ssn, rid, createDate, tableAmount, detail):
        reservation = RESERVATION(ssn=ssn, rid=rid, createDate=createDate, tableAmount=tableAmount, detail=detail)
        session.add(reservation)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log
    
    def read(self, rid, ssn):
        reservation = session.query(RESERVATION)
        reservation = reservation.filter(RESERVATION.rid==str(rid), RESERVATION.ssn==str(ssn))
        if reservation.scalar() is not None :
            reservation = self.serialize(reservation.one())
            log = {
                "result":reservation,
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

    def update(self, ssn, rid, createDate, tableAmount, detail):
        reservation = session.query(RESERVATION)
        reservation = reservation.filter(RESERVATION.rid==rid, RESERVATION.ssn==ssn)
        if reservation.scalar() is not None :
            reservation = reservation.one()
            reservation.createDate = createDate
            reservation.tableAmount = tableAmount
            reservation.detail = detail
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

    def delete(self, ssn, rid):
        reservation = session.query(RESERVATION)
        reservation = reservation.filter(RESERVATION.rid==rid, RESERVATION.ssn==ssn)
        if reservation.scalar() is not None :
            session.delete(reservation.one())
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

    def getAllReservation(self):
        reservations = session.query(RESERVATION).all()
        reservations = [self.serialize(reservation) for reservation in reservations]
        log = {
            "result":reservations,
            "msg":"",
            "status":"1"
        }
        return log

    def serialize(self, object):
        return {
            'ssn': object.ssn,
            'rid': object.rid,
            'createDate': object.createDate,
            'tableAmount': object.tableAmount,
            'detail': object.detail,
        }