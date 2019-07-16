from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
import json
import requests

from dotenv import load_dotenv
load_dotenv()


class Location:
    def __init__(self, url, query):
        self.search_query = query
        self.get_location = (url)
    
    def get_location(self, url):
        result = request.get(url).json()
        self.formatted_query = result['results'][0]['formatted_address']
        self.latitude = result['results'][0]['geometry']['location']['lat']
        self.latitude = result['results'][0]['geometry']['location']['lng']

    def serialize(self):
        return vars(self)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
# get request must have this name:
    def do_GET(self):

        parsed_path = urlparse(self.path)
        # 200 means its all good
        self.send_response(200)
        # need to set which type of content we are sending
        self.send_header('Content-type', 'application/json')
        # when done adding header you you must call end
        self.end_headers()
        
        if parsed_path.path == '/locations':
            parsed_qs = parse_qs(parsed_path.query)
            query = parsed_qs
            url = f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={os.getenv(GEOCODE_API_KEY)'}
            print('url', url)


            result = requests.get(url).json()
            
            formatted_query = result['results'][0]['formatted_address']

            print('fq', formatted_query)

            self.wfile.write(b'tbd')
            return

        self.send_response_only(404)
        self.end_headers()

def create_server():
    return HTTPServer(
        ('127.0.0.1', 3000), SimpleHTTPRequestHandler
    )

def run_forever():
    server = create_server()

    try: 
        print(f'Starting server on port {os.getenv('PORT')}')
        server.serve_forever()

    except KeyboardInterrupt:
        server.server_close()
        server.shutdown()

if __name__ == "__main__":
    run_forever()