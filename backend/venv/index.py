from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from src import Account as A
from src import Restaurant as R
from src import RestaurantAddress as RA
from src import Reservation as RE

Account = A.Account()
Restaurant = R.Restaurant()
RAddress = RA.RAddress()
Reservation = RE.Reservation()

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'This is backend'
    

# Create Account
@app.route('/account',methods=["POST"])
@cross_origin()
def createAccount():
    ssn = request.form['ssn']
    fname = request.form['fname']
    lname = request.form['lname']
    username = request.form['username']
    password = request.form['password']
    address = request.form['address']
    email = request.form['email']
    phoneNumber = request.form['phoneNumber']
    birthDay = request.form['birthDay']

    log = Account.create(ssn, fname, lname, username, password, address, email, phoneNumber, birthDay)
    return jsonify(log)

# Read Account
@app.route('/account/<ssn>',methods=["GET"])
@cross_origin()
def readAccount(ssn=None):
    if ssn != None:
        log = Account.read(ssn)
        return jsonify(log)

# Get All Account
@app.route('/account',methods=["GET"])
@cross_origin()
def getAllAccount():
    log = Account.getAllAccount()
    return jsonify(log)

# Update Account
@app.route('/account',methods=["PUT"])
@cross_origin()
def updateAccount():
    ssn = request.form['ssn']
    fname = request.form['fname']
    lname = request.form['lname']
    username = request.form['username']
    password = request.form['password']
    address = request.form['address']
    email = request.form['email']
    phoneNumber = request.form['phoneNumber']
    birthDay = request.form['birthDay']

    log = Account.update(ssn, fname, lname, username, password, address, email, phoneNumber, birthDay)
    return jsonify(log)

# Delete Account
@app.route('/accountDel/<ssn>',methods=["DELETE"])
@cross_origin()
def deleteAccount(ssn):
    log = Account.delete(ssn)
    return jsonify(log)

# Register
@app.route('/register', methods=["POST"])
@cross_origin()
def register():
    ssn = request.form['ssn']
    fname = request.form['fname']
    lname = request.form['lname']
    username = request.form['username']
    password = request.form['password']
    address = request.form['address']
    email = request.form['email']
    phoneNumber = request.form['phoneNumber']
    birthDay = request.form['birthDay']

    log = Account.register(ssn, fname, lname, username, password, address, email, phoneNumber, birthDay)
    return jsonify(log)

# Login
@app.route('/login', methods=["POST"])
@cross_origin()
def login():
    username = request.form['username']
    password = request.form['password']

    log = Account.login(username, password)
    return jsonify(log)

# Create restaurant
@app.route('/restaurant', methods=["POST"])
@cross_origin()
def createRestaurant():
    rid = request.form['rid']
    detail = request.form['detail']
    promotion = request.form['promotion']
    tableRemain = request.form['tableRemain']
    name = request.form['name']

    log = Restaurant.create(rid, detail, promotion, tableRemain, name)
    return jsonify(log)

# Read restaurant
@app.route('/restaurant/<rid>', methods=["GET"])
@cross_origin()
def readRestaurant(rid=None):
    if rid != None:
        log = Restaurant.read(rid)
        return jsonify(log)

# Get all restaurant
@app.route('/restaurant', methods=["GET"])
def getAllRestaurant():
    log = Restaurant.getAllRestaurant()
    return jsonify(log)

@app.route('/getRemainTable/<rid>', methods=["GET"])
def getRemainTable(rid):
    if rid != None:
        log = Restaurant.getTableRemaiByRid(rid)
        return jsonify(log)

# Update restaurant
@app.route('/restaurant', methods=["PUT"])
@cross_origin()
def updateRestaurant():
    rid = request.form['rid']
    detail = request.form['detail']
    promotion = request.form['promotion']
    tableRemain = request.form['tableRemain']
    name = request.form['name']

    log = Restaurant.update(rid, detail, promotion, tableRemain, name)
    return jsonify(log)

# Delete restaurant
@app.route('/restaurantDel/<rid>', methods=["DELETE"])
@cross_origin()
def deleteRestaurant(rid):
    log = Restaurant.delete(rid)
    return jsonify(log)


# Create address restaurant
@app.route('/raddress', methods=["POST"])
@cross_origin()
def createRestaurantAddress():
    rid = request.form['rid']
    street = request.form['street']
    province = request.form['province']
    country = request.form['country']
    zip = request.form['zip']

    log = RAddress.create(rid, street, province, country, zip)
    return jsonify(log)

# Read address restaurant
@app.route('/raddress/<rid>', methods=["GET"])
@cross_origin()
def readRestaurantAddress(rid=None):
    if rid != None:
        log = RAddress.read(rid)
        return jsonify(log)

# Get all address restaurant
@app.route('/raddress', methods=["GET"])
@cross_origin()
def getAllRestaurantAddress():
    log = RAddress.getAllRestaurant()
    return jsonify(log)

# Update address restaurant
@app.route('/raddress', methods=["PUT"])
@cross_origin()
def updateRestaurantAddress():
    rid = request.form['rid']
    street = request.form['street']
    province = request.form['province']
    country = request.form['country']
    zip = request.form['zip']

    log = RAddress.update(rid, street, province, country, zip)
    return jsonify(log)

# Delete address restaurant
@app.route('/raddressDel/<rid>', methods=["DELETE"])
@cross_origin()
def deleteRestaurantAddress(rid):
    log = RAddress.delete(rid)
    return jsonify(log)

# Create reservation
@app.route('/reservation', methods=["POST"])
@cross_origin()
def createreservation():
    ssn = request.form['ssn']
    rid = request.form['rid']
    createDate = request.form['createDate']
    tableAmount = request.form['tableAmount']
    detail = request.form['detail']

    log = Reservation.create(ssn, rid, createDate, tableAmount, detail)
    return jsonify(log)

# Get all reservation
@app.route('/reservation', methods=["GET"])
@cross_origin()
def getAllreservation():
    log = Reservation.getAllReservation()
    return jsonify(log)

# Read reservation 
@app.route('/getreservation', methods=["GET"])
@cross_origin()
def readreservation():
    rid = request.args.get('rid')
    ssn = request.args.get('ssn')
    if rid != None:
        log = Reservation.read(rid, ssn)
        return jsonify(log)

# Update reservation
@app.route('/reservation', methods=["PUT"])
@cross_origin()
def updatereservation():
    ssn = request.form['ssn']
    rid = request.form['rid']
    createDate = request.form['createDate']
    tableAmount = request.form['tableAmount']
    detail = request.form['detail']

    log = Reservation.update(ssn, rid, createDate, tableAmount, detail)
    return jsonify(log)

# Delete reservation
@app.route('/reservationDel/<rid>', methods=["DELETE"])
@cross_origin()
def deletereservation(rid):
    rid = request.args.get('rid')
    ssn = request.args.get('ssn')

    log = Reservation.delete(rid, ssn)
    return jsonify(log)

if __name__ == '__main__':
    app.run(debug=True)