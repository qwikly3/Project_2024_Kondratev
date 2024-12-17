import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Configuration
HOST = '0.0.0.0'  # Accessible on the local network
PORT = 8000       # Port number for the server

# Directory containing your website files
WEB_DIR = "site"  # Change to your folder containing the site files (e.g., 'index.html')

# Change the working directory to the web folder
if not os.path.exists(WEB_DIR):
    os.makedirs(WEB_DIR)
os.chdir(WEB_DIR)

class CustomHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Override to remove default server logging (optional)
        return

if __name__ == '__main__':
    print(f"Serving files from {os.getcwd()} on {HOST}:{PORT}")
    with HTTPServer((HOST, PORT), CustomHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down the server.")
            httpd.shutdown()
