"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import Collector_V3.views
