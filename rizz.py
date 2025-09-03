from http.server import HTTPServer, SimpleHTTPRequestHandler

class WASMRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Allow CORS for all origins
        self.send_header("Access-Control-Allow-Origin", "*")
        # Required for SharedArrayBuffer
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        return super().end_headers()

if __name__ == "__main__":
    httpd = HTTPServer(("0.0.0.0", 8080), WASMRequestHandler)
    print("Serving at http://localhost:8080")
    httpd.serve_forever()
