import os
import cgi
import http.server
import hbcvt
from urllib.parse import urlparse
from urllib.parse import unquote
from dottalk import DotTalk


class DotServer(object):

    HOST = '0.0.0.0'
    PORT = 8000

    def __init__(self):
        super(DotServer, self).__init__()

    def run(self):
        print("DotServer is running on", self.PORT)
        httpd = http.server.HTTPServer((self.HOST, self.PORT), DotTalkHTTPRequestHandler)
        httpd.serve_forever()


class DotTalkHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):

    def set_header(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.set_header()
        name  = "You"
        msg = ""
        hangul = ""
        braille = []
        queries = []

        # Parse URL in req.
        parsed = urlparse(self.path)
        if (parsed.query):
            queries = parsed.query.split("&")
        for query in queries:
            splitted = unquote(query.replace("+", " ")).split("=")
            key = splitted[0]
            val = splitted[1]
            if   key == 'name':
                name = val
            elif key == 'msg':
                msg = val

        if msg != "":
            # Set Hangul and Braille
            hangul = name + ": " + msg
            braille = hbcvt.h2b.text(hangul)
            print(hangul, braille)

            DotTalk.HANGUL, DotTalk.BRAILLE = hangul, braille
            DotTalk.IS_UPDATED = True

        # Open the static file requested and send it
        with open(os.curdir + os.sep + "static" + os.sep + "index.html") as f:
            data = f.read().format(name, hangul, braille)
            resData = bytes(data, 'UTF-8');
            self.wfile.write(resData)

    def do_POST(self):
        # self.set_header()
        length = int(self.headers['content-length'])
        post_param = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        self.do_GET()
