from flask import Flask
from routes.auth_route import auth_router
from routes.user_route import user_router
from routes.admin_roue import admin_router
from flask_sqlalchemy import SQLAlchemy
from database.db import db
from database import config
from flask_jwt_extended import JWTManager



# instance Flask Claskk
app=Flask(__name__)

app.config["JWT_SECRET_KEY"] = "sufgsdfgsdfgdfs34534534t"  
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# instance JWTManager,SQLAlchemy
JWTManager(app)
SQLAlchemy(app)


# instance routes 
app.register_blueprint(auth_router)
app.register_blueprint(user_router)
app.register_blueprint(admin_router)


# Init DB
db.init_app(app)
with app.app_context(): 
    db.create_all()

# run app Locally
if __name__ == "__main__":
    app.run(debug=True)