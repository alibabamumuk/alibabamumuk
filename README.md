https://alibabamumuk.github.io/mumukai/

import http.server
import socketserver
import webbrowser

# Sunucu ayarları
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Sunucuyu başlatma
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    webbrowser.open(f"http://localhost:{PORT}")
    httpd.serve_forever()
