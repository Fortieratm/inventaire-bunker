import http.server, socketserver, os
PORT = int(os.environ.get("PORT", 8080))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
