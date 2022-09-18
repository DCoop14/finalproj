from distutils.log import Log
from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager

from .auth.routes import auth
from .models import User
from .shop.routes import shop

app = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.register_blueprint(auth)
app.register_blueprint(shop)



app.config.from_object(Config)

from .models import db 


db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)



from . import routes
from . import models