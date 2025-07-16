import http.server
import socketserver
import json

# Create a subclass of http.server.BaseHTTPRequestHandler
class MyCustomHandler(http.server.BaseHTTPRequestHandler):
    # The do_GET method handles all GET requests
    def do_GET(self):
        # Get the requested URL path
        requested_path = self.path

        # Handle different endpoints
        if requested_path == "/":
            # For the root endpoint, send a simple text response
            self.send_response(200)  # HTTP Status: 200 OK
            self.send_header("Content-type", "text/plain") # Content type: plain text
            self.end_headers()
            response_message = "Hello, this is a simple API!"
            self.wfile.write(response_message.encode('utf-8'))
            print(f"GET request handled: {requested_path}")

        elif requested_path == "/data":
            # For the '/data' endpoint, serve JSON data
            data = {"name": "John", "age": 30, "city": "New York"}
            # Convert Python dictionary to a JSON string
            json_response = json.dumps(data, ensure_ascii=False, indent=4)

            self.send_response(200)  # HTTP Status: 200 OK
            self.send_header("Content-type", "application/json") # Content type: JSON
            # It's good practice to send Content-Length for accurate transfer
            self.send_header("Content-Length", str(len(json_response.encode('utf-8'))))
            self.end_headers()
            self.wfile.write(json_response.encode('utf-8'))
            print(f"JSON data served for: {requested_path}")

        elif requested_path == "/status":
            # For the '/status' endpoint, return a simple "OK"
            self.send_response(200)  # HTTP Status: 200 OK
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            response_message = "OK"
            self.wfile.write(response_message.encode('utf-8'))
            print(f"Status request handled: {requested_path}")

        else:
            # Handle undefined endpoints with a 404 Not Found error
            status_code = 404
            error_message = "Not Found"
            # Crucially, we manually craft the response body to match test expectations
            response_body = "The requested endpoint does not exist."

            self.send_response(status_code)
            self.send_header("Content-type", "text/plain") # Error messages
