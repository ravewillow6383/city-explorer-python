from flask import Flask
from flask import request, jsonify
from dotenv import load_dotenv
from app.locations import Location
from app.weather import Forecast
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask(__name__)
# CORS(app)app.config.from_object(Config)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/location')
def fetch_location():
# #  looking in the search query column which has the value of the value that coorsponds with the data keyword
    cached_location = LocationModel.query.filter_by(search_query = request.args.get('data')).first()
# #    convert cached location to a dictionary
    if cached_location:
        return jsonify(cached_location.to_dict())
    fresh_location = Location.fetch(request.args.get('data'))
    resource = LocationModel(
        search_query = fresh_location.search_query,
        formatted_query = fresh_location.formatted_query,
        latitude = fresh_location.latitude,
        longitude = fresh_location.longitude
    )

    db.session.add(resource)
    db.session.commit()

    return jsonify(resource.to_dict())
# @app.route('/weather', methods=['GET', 'POST'])
# def fetch_weather():
#     latitude = request.args['data[latitude]']
#     longitude = request.args['data[longitude]']
#     return Forecast.fetch(latitude, longitude)

# @app.route('/events', methods=['GET'])
# def fetch_events():
#     address = request.args['data[formatted_query]']
#     result = Events.event_results(query)
#     return Event.fetch_as_json(address)

from app.models.model import LocationModel
