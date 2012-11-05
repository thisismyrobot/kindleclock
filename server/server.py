import BaseHTTPServer
import sources


# Settings
PORT_NUMBER = 8000
SOURCES = {"TEMPERATURE": sources.temperature,
           "FORECAST": sources.forecast,
           "AGENDA": sources.agenda,
           "UNREADGMAIL": sources.unreadgmail}


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
        if filename == "favicon.ico":
            return
        with open(filename) as f:
            if filename == "dashboard.html":
                template =  f.read()
                tempdict = {}
                for k,func in SOURCES.items():
                    tempdict[k] = func()
                statichtml = template % tempdict
                s.wfile.write(statichtml)
            else:
                s.wfile.write(f.read())

    def log_message(self, format, *args):
        return

if __name__ == '__main__':
    httpd = BaseHTTPServer.HTTPServer(("", PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()