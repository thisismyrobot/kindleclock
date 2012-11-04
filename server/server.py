import BaseHTTPServer


# Settings
PORT_NUMBER = 8000


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """ Handles GET and HEAD requests.
    """
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        filename = s.path[1:]
        if filename == "":
            filename = "dashboard.html"
        with open(filename) as f:
            s.wfile.write(f.read())


if __name__ == '__main__':
    httpd = BaseHTTPServer.HTTPServer(("", PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()