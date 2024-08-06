from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from app.models.questions import *
from app.models.responses import *
# from app.models.categories import *
