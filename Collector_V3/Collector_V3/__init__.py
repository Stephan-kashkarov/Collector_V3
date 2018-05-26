"""
The flask application package.
"""

from flask import Flask
from flask_login import login_manager

app = Flask(__name__)
login_manager(app)


import Collector_V3.views
