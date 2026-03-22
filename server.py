import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8080))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
httpd = socketserver.TCPServer(("0.0.0.0", PORT), http.server.SimpleHTTPRequestHandler)
print("Serving port " + str(PORT), flush=True)
httpd.serve_forever()
