from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
import json
import requests
from dotenv import load_dotenv
from locations import Location
from weather import Forecast

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def location():
    print(request.args.get('data'))
    data=Location.fetch('barcelona')

    return data

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
# get request must have this name (BaseHTTPRequestHandler):
    def do_GET(self):

        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)
        
        if parsed_path.path == '/location' and parsed_qs.get('data'):
            
            self.do_json_response()
            location_query = parsed_qs.get('data')[0]
            json_string = Location.fetch(location_query)
            self.wfile.write(json_string.encode())

            return

        elif parsed_path.path == '/weather' and parsed_qs.get('data'):

            self.do_json_response()
            latitude = parsed_qs['data[latitude]'][0]
            longitude = parsed_qs['data[longitude]'][0]
            json_string = Forecast.fetch(latitude, longitude)
            self.wfile.write(json_string.encode())

            return

            self.send_response_only(404)
            self.end_headers()

        def do_json_response(self):
            # 200 means its all good
            self.send_response(200)
            # need to set which type of content we are sending
            self.send_header('Content-type', 'application/json')
            # when done adding header you you must call end
            self.end_headers()


def create_server():
    return HTTPServer(
        ('127.0.0.1', 3000), SimpleHTTPRequestHandler
        # must match the name given to class on line 23
    )

def run_forever():
    server = create_server()

    try: 
        print('starting on port {}'.format(os.environ['PORT']))
        server.serve_forever()

    except KeyboardInterrupt:
        server.server_close()
        server.shutdown()

if __name__ == "__main__":
    run_forever()