from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Globally accessible extensions

db = SQLAlchemy()
migrate = Migrate()
