from flask import Flask
from config import Config
from flask_migrate import Migrate


from .auth.routes import auth


app = Flask(__name__)


app.register_blueprint(auth)


app.config.from_object(Config)

from .models import db 


db.init_app(app)
migrate = Migrate(app, db)



from . import routes
from . import models