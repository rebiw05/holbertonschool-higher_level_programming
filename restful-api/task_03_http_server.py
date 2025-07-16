import http.server
import socketserver
import json # JSON məlumatlarını işləmək üçün

# BaseHTTPRequestHandler sinfindən öz server handler sinfimizi yaradırıq
class MyCustomHandler(http.server.BaseHTTPRequestHandler):
    # do_GET metodu GET sorğularını idarə edir
    def do_GET(self):
        # Sorğu olunan URL yolunu əldə edirik
        requested_path = self.path

        # Müxtəlif endpointləri idarə edirik
        if requested_path == "/":
            # Əsas endpoint üçün sadə mətn cavabı
            self.send_response(200) # OK status kodu
            self.send_header("Content-type", "text/plain") # Məzmun növü: sadə mətn
            self.end_headers()
            response_message = "Hello, this is a simple API!"
            self.wfile.write(response_message.encode('utf-8'))
            print(f"GET sorğusu işləndi: {requested_path}")

        elif requested_path == "/data":
            # '/data' endpointi üçün JSON məlumatı
            data = {"name": "John", "age": 30, "city": "New York"}
            json_response = json.dumps(data, ensure_ascii=False, indent=4)

            self.send_response(200) # OK status kodu
            self.send_header("Content-type", "application/json") # Məzmun növü: JSON
            self.send_header("Content-Length", str(len(json_response.encode('utf-8')))) # Məzmun uzunluğu
            self.end_headers()
            self.wfile.write(json_response.encode('utf-8'))
            print(f"JSON sorğusu işləndi: {requested_path}")

        elif requested_path == "/status":
            # '/status' endpointi üçün sadə "OK" cavabı
            self.send_response(200) # OK status kodu
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            response_message = "OK"
            self.wfile.write(response_message.encode('utf-8'))
            print(f"Status sorğusu işləndi: {requested_path}")

        else:
            # Təyin olunmamış endpointlər üçün 404 Not Found xətası
            self.send_error(404, "Not Found", "The requested endpoint does not exist.")
            print(f"Xəta: Təyin olunmamış sorğu - {requested_path}")

# Serverin dinləyəcəyi portu təyin edirik
PORT = 8000

# Serveri işə salırıq
# Boş string ('') bütün mövcud şəbəkə interfeyslərində dinləmək deməkdir (məsələn, localhost)
with socketserver.TCPServer(("", PORT), MyCustomHandler) as httpd:
    print(f"Server {PORT} portunda işləyir...")
    print(f"Test etmək üçün brauzerinizdə aşağıdakı ünvanlara daxil olun:")
    print(f"  - Əsas səhifə: http://localhost:{PORT}")
    print(f"  - JSON məlumatı: http://localhost:{PORT}/data")
    print(f"  - API statusu: http://localhost:{PORT}/status")
    print(f"  - Xəta testi: http://localhost:{PORT}/undefined_endpoint")

    # Serveri daimi olaraq gələn sorğuları dinləməyə başlayır
    httpd.serve_forever()
