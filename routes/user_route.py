

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity


# if need connect to DB instance db
from database.db import db

user_router = Blueprint('user', __name__, url_prefix='/user')


# ####
# # Endpunkte für Kunden
# ####


@user_router.route('/settings/<custid>', methods=['GET'])
@jwt_required()
def get_settings(custid):
    current_user = get_jwt_identity()
    if (current_user['role'] == "user" and current_user['custid']==custid ):
        return "you are user"
    return jsonify("dont allow to access"), 401


@user_router.route('/settings/<custid>', methods=['PATCH'])
@jwt_required()
def update_settings(custid):
    current_user = get_jwt_identity()
    if (current_user['role'] == "user" and current_user['custid']==custid ):
        return "you are user"
    return jsonify("dont allow to access"), 401


@user_router.route('/certificate', methods=['GET'])
@jwt_required()
def get_certificate():
    current_user = get_jwt_identity()
    if (current_user['role'] == "user"):
        return "you are user"
    return jsonify("dont allow to access"), 401


@user_router.route('/certificate/check', methods=['POST'])
@jwt_required()
def recheck_certificate():
    current_user = get_jwt_identity()
    if (current_user['role'] == "user"):
        return "you are user"
    return jsonify("dont allow to access"), 401


@user_router.route('/certificate/status', methods=['GET'])
@jwt_required()
def get_status_certificate():
    current_user = get_jwt_identity()
    if (current_user['role'] == "user"):
        return "you are user"
    return jsonify("dont allow to access"), 401
