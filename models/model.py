from app import db

class LocationModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    formatted_query = db.Column(db.String(1024))
    search_query = db.Column(db.String(256), unique = True)
    latitude = db.Column(db.Float(10.7))
    longitude = db.Column(db.Float(10.7))

    def to_dict(self):
        return {
            'formatted_query':self.formatted_query,
            'search_query':self.search_query,
            'latitude':self.latitude,
            'longitude':self.longitude
        }