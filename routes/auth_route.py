

from flask import Blueprint, request, jsonify, render_template, make_response, redirect, url_for
from security import secur_pass
from models.user import UserModel

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)

from database.db import db


auth_router = Blueprint('auth', __name__, url_prefix='/auth')


@auth_router.route('/register', methods=['GET'])
def get_register():
    return render_template('/auth/register.html')


@auth_router.route('/login', methods=['GET'])
def get_login():
    return render_template('/auth/login.html')




@auth_router.route('/register', methods=['POST'])
def create_user():

    email = request.form['email']
    password = request.form['password']
    user_exist = UserModel.query.filter_by(email=email).first()
    if not user_exist:
        try:
            hashed_custid = secur_pass.get_password_hash(password)
            new_user = UserModel(
                email=email, password=hashed_custid, role="user")
            db.session.add(new_user)
            db.session.commit()
        except:
            return "some error"

        return render_template('/auth/register.html', contacts="Your account created successfuly!")
    else:
        return render_template('/auth/register.html', contacts="Email or password ist not correct!!")


# @auth_router.route("/login", methods=["POST"])
# def create_token():
#     email = request.form['email']
#     password = request.form['password']
#     user_exist = UserModel.query.filter_by(email=email).first()

#     if not user_exist.email or not secur_pass.verify_password(password, user_exist.password):
#         print('not found')
#         return jsonify("Wrong password"), 401

#     access_token = create_access_token(identity=email)
#     refresh_token = create_refresh_token(identity=email)
#     resp = jsonify({'login': True})
#     set_access_cookies(resp, access_token)
#     set_refresh_cookies(resp, refresh_token)
#     return resp, 200

@auth_router.route("/login", methods=["POST"])
def create_token():
    email = request.form['email']
    password = request.form['password']
    user_exist = UserModel.query.filter_by(email=email).first()

    if not user_exist.email or not secur_pass.verify_password(password, user_exist.password):
        print('not found')
        return jsonify("Wrong password"), 401

    access_token = create_access_token(
        identity={"email": user_exist.email, "role": user_exist.role})
    # refresh_token = create_refresh_token(identity=user_exist.email)
    resp = make_response(redirect(url_for('page.index')))

    set_access_cookies(resp, access_token)
    # set_refresh_cookies(resp, refresh_token)
    return resp
