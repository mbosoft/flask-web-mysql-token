

from flask import Blueprint, render_template, jsonify, make_response, url_for,redirect
from flask_jwt_extended import (get_jwt_identity,jwt_required)
from models.user import UserModel



user_router = Blueprint('user', __name__, url_prefix='/api')


# Wirite your protect endpoint here ---------------------

