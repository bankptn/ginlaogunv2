from .model import ACCOUNT
from .helper import *
from sqlalchemy import func 

session = initDatabase()

class Account():
    def create(self, ssn, fname, lname, username, password, address, email, phoneNumber, birthDay, profilePic):
        account = ACCOUNT(ssn=ssn, fname=fname, lname=lname, username=username, password=password, address=address, email=email, phoneNumber=phoneNumber, birthDay=birthDay, profilePic=profilePic)
        session.add(account)
        session.commit()
        log = {
            "result":"",
            "msg":"",
            "status":"1"
        }
        return log
    
    def read(self, ssn):
        account = session.query(ACCOUNT)
        account = account.filter(ACCOUNT.ssn==ssn)
        if account.scalar() is not None :
            print(account.one())
            account = self.serialize(account.one())
            log = {
                "result":account,
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

    def update(self, ssn, fname, lname, username, password, address, email, phoneNumber, birthDay, profilePic):
        account = session.query(ACCOUNT)
        account = account.filter(ACCOUNT.ssn==ssn)
        if account.scalar() is not None :
            account = account.one()
            account.fname = fname
            account.lname = lname
            account.username = username
            account.password = password
            account.address = address
            account.email = email
            account.phoneNumber = phoneNumber
            account.birthDay = birthDay
            account.profilePic = profilePic
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

    def delete(self, ssn):
        account = session.query(ACCOUNT)
        account = account.filter(ACCOUNT.ssn==ssn)
        if account.scalar() is not None :
            session.delete(account.one())
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

    def getAllAccount(self):
        accounts = session.query(ACCOUNT).all()
        result = [self.serialize(account) for account in accounts]
        log = {
            "result":result,
            "msg":"",
            "status":"1"
        }
        return log

    def register(self, ssn, fname, lname, username, password, address, email, phoneNumber, birthDay, profilePic):
        account = session.query(ACCOUNT)
        accountSSN = account.filter(ACCOUNT.ssn==ssn)
        accountUSERNAME = account.filter(ACCOUNT.username==username)

        if accountSSN.scalar() is None:
            if accountUSERNAME.scalar() is None:
                logs =  self.create(ssn, fname, lname, username, password, address, email, phoneNumber, birthDay, profilePic)
                return logs
            else:
                log = {
                "result":"",
                "msg":"Username is already exsit",
                "status":"1"
            }
            return log
                
        else:
            log = {
                "result":"",
                "msg":"SSN is already exsit",
                "status":"1"
            }
            return log
    
    def login(self, username, password):
        account = session.query(ACCOUNT)
        account = account.filter(ACCOUNT.username==username)
        if account.scalar() is not None :
            account = self.serialize(account.one())
            if account['password'] == password:
                log = {
                    "result":account['ssn'],
                    "msg":"",
                    "status":"1"
                }
                return log
            else:
                log = {
                    "result":"",
                    "msg":"Password is wrong",
                    "status":"100"
                }
                return log
        else:
            log = {
                "result":"",
                "msg":"User not found",
                "status":"100"
            }
            return log

    def serialize(self,customer):
        return {
            'ssn': customer.ssn,
            'fname': customer.fname,
            'lname': customer.lname,
            'username': customer.username,
            'password': customer.password,
            'address': customer.address,
            'email': customer.email,
            'phoneNumber': customer.phoneNumber,
            'birthDay': customer.birthDay,
            'pic': customer.profilePic
        }