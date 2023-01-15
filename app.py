from flask import Flask
from routes.auth_route import auth_router
from routes.user_route import user_router
from routes.pages_route import page_router
from flask_sqlalchemy import SQLAlchemy
from database.db import db
from database import config
from flask_jwt_extended import JWTManager



# instance Flask Claskk
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_SECRET_KEY'] = 'sudsafadsfasdf§"$"§ret'  # Change this!


# instance JWTManager,SQLAlchemy
JWTManager(app)
SQLAlchemy(app)


# instance routes 
app.register_blueprint(auth_router)
app.register_blueprint(user_router)
app.register_blueprint(page_router)


# Init DB
db.init_app(app)
with app.app_context(): 
    db.create_all()

# run app Locally
if __name__ == "__main__":
    app.run()



