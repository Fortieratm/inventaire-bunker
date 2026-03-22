import http.server, socketserver, os

PORT = int(os.environ.get("PORT", 8080))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("0.0.0.0", PORT), handler)
print(f"Serving on 0.0.0.0:{PORT}")
httpd.serve_forever()
