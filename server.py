import http.server, socketserver, os, sys

PORT = int(os.environ.get("PORT", 3000))
print(f"PORT from env: {PORT}", flush=True)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(format % args, flush=True)

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Serving on 0.0.0.0:{PORT}", flush=True)
    sys.stdout.flush()
    httpd.serve_forever()
```

Commit — puis dans Railway Agent tapez :
```
Remove the PORT variable override and redeploy inventaire-bunker
