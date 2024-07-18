import http.server
import socketserver

# IP adresi ve port numarası
HOST = "192.168.1.2"  # Kendi IP adresinizi buraya yazın
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print(f"Serving at {HOST}:{PORT}")
    httpd.serve_forever()
