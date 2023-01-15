

from flask import Blueprint, request, jsonify,render_template




page_router = Blueprint('page', __name__,)



@page_router.route('/')
def index():
    return render_template('/pages/index.html')


@page_router.route('/contact')
def contact():
    return render_template('/pages/contact.html')