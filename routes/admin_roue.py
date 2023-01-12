
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity


# if need connect to DB instance db
from database.db import db

admin_router = Blueprint('admin', __name__, url_prefix='/admin')


# ####
# # Endpunkte für Kunden
# ####


@admin_router.route('/settings/<custid>', methods=['GET'])
@jwt_required()
def get_settings(custid):
    current_user = get_jwt_identity()
    if (current_user['role'] == "user" and current_user['custid']==custid ):
        return "you are admin"
    return jsonify("Wrong Token"), 401


@admin_router.route('/settings/<custid>', methods=['PATCH'])
@jwt_required()
def update_settings(custid):
    current_user = get_jwt_identity()
    if (current_user['role'] == "user" and current_user['custid']==custid ):
        return "you are admin"
    return jsonify("Wrong Token"), 401


@admin_router.route('/certificate', methods=['GET'])
@jwt_required()
def get_certificate():
    current_user = get_jwt_identity()
    if (current_user['role'] == "admin"):
        return "you are admin"
    return jsonify("Wrong Token"), 401


@admin_router.route('/certificate/check', methods=['POST'])
@jwt_required()
def recheck_certificate():
    current_user = get_jwt_identity()
    if (current_user['role'] == "admin"):
        return "you are admin"
    return jsonify("Wrong Token"), 401


@admin_router.route('/certificate/status', methods=['GET'])
@jwt_required()
def get_status_certificate():
    current_user = get_jwt_identity()
    if (current_user['role'] == "admin"):
        return "you are admin"
    return jsonify("Wrong Token"), 401


