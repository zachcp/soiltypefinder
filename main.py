"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
from google.appengine.ext import ndb


app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500



####################
class SoilFeature(ndb.Model):
    """Models a Soil Feature."""
    soil = ndb.StringProperty(required=True)
    suborder = ndb.StringProperty(required=True)
    maxlat = ndb.FloatProperty(required=True)
    minlat = ndb.FloatProperty(required=True)
    maxlon = ndb.FloatProperty(required=True)
    minlon = ndb.FloatProperty(required=True)
    polygon = ndb.listProperty(value=GeoPt)

