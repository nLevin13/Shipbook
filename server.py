from http.server import HTTPServer, BaseHTTPRequestHandler
from mapstest import mapstest
from io import BytesIO

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    coords = {'lat':0,'lon':0}
    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        pts = SimpleHTTPRequestHandler.coords
        res = str(mapstest(pts['lat'], pts['lon'])).encode('utf-8')
        self.wfile.write(res)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        b = str(body)
        b = b[b.index('=')+1:]
        lat = b[:b.index('&')]
        lon = b[b.index('=')+1:-1]
        SimpleHTTPRequestHandler.coords['lat'] = float(lat)
        SimpleHTTPRequestHandler.coords['lon'] = float(lon)
        
        a = str(lat+','+lon).encode('utf-8')
        self.wfile.write(a)


httpd = HTTPServer(('localhost', 8001), SimpleHTTPRequestHandler)
httpd.serve_forever()
