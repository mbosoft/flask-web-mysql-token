

from datetime import timedelta
import string
from flask import Blueprint, request, jsonify
from security import secur_pass
from models.user import UserModel
from flask_jwt_extended import create_access_token
import random


from database.db import db
auth_router = Blueprint('auth', __name__, url_prefix='/auth')

# create a Random user ID


def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@auth_router.route('/register', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        data = request.get_json()
        user_exist = UserModel.query.filter_by(custid=data['custid']).first()
        current_usr=data['custid']
        if not user_exist:
            # hashed_custid=secur_pass.get_password_hash(create_custid)
            new_user = UserModel(custid=data['custid'], role=data['role'])
            db.session.add(new_user)
            db.session.commit()
        else:
            return "user exist"
        return current_usr
    if request.method == 'GET':
        return "item GET"


@auth_router.route("/token", methods=["POST"])
def create_token():
    custid = request.json.get('custid', None)
    current_user = UserModel.query.filter_by(custid=custid).one_or_none()
    custid = current_user.custid
    role = current_user.role

    # if not custid or not secur_pass.verify_password(custid,custid.custid):
    #     return jsonify("Wrong custid"), 401


    access_token = create_access_token({'custid': custid,'role': role},expires_delta=False)
    return jsonify(access_token=access_token)
