#!/usr/bin/env python3
import http.server
import socketserver
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Check the requested endpoint and respond accordingly.
        if self.path == '/':
            # Root endpoint: return a simple text greeting.
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode())
        elif self.path == '/data':
            # /data endpoint: send a JSON response.
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            # /status endpoint: return API status.
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        elif self.path == '/info':
            # /info endpoint: return API information.
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode())
        else:
            # For all undefined endpoints, return 404 Not Found.
            self.send_error(404, "Endpoint not found")

def run(server_class=http.server.HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)  # Bind to all interfaces.
    httpd = server_class(server_address, handler_class)
    print("Starting http server on port", port)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
