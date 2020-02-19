from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

config_type = {
    "development":  "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "production": "config.ProductionConfig"
}

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config_type.get(os.getenv('FLASK_ENV', 'production')))
app.config.from_pyfile('config.cfg', silent=True)

db = SQLAlchemy(app)
Migrate(app, db)
