import BaseHTTPServer


# Settings
PORT_NUMBER = 8000
PAGE = "dashboard.html"


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
        with open(PAGE) as f:
            s.wfile.write(f.read())


if __name__ == '__main__':
    httpd = BaseHTTPServer.HTTPServer(("", PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()