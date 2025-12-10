import http.server
import socketserver
import os
import socket
import base64
import sys
import argparse
import logging

try:
    import qrcode
except:
    qrcode = None

class Handler(http.server.SimpleHTTPRequestHandler):
    passwd = None
    do_logs = False

    def do_HEAD(self):
        # check if password ok
        if not self.auth_ok():
            self.ask_pass()
            return
        return super().do_HEAD()

    def do_GET(self):
        if not self.auth_ok():
            self.ask_pass()
            return
        if self.do_logs:
            logging.info("got GET " + self.path + " from " + str(self.client_address[0]))
        return super().do_GET()

    def auth_ok(self):
        # if no password set then just allow
        if not self.passwd:
            return True
        auth_header = self.headers.get("Authorization")
        if not auth_header:     # if no passwd
            return False
        try:    # check passwd
            parts = auth_header.split(" ")
            if parts[0].lower() != "basic":
                return False
            decoded = base64.b64decode(parts[1]).decode("utf-8")    # decodes passwd from base64
            pw = decoded.split(":", 1)[1]
            if pw == self.passwd:
                return True
            else:
                return False
        except:
            return False

    def ask_pass(self):
        # tell browser to show popup password thing
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="files"')
        self.end_headers()

class HTML(Handler):
    def list_directory(self, path):
        try:
            lst = os.listdir(path)
        except:
            self.send_error(404, "cant open dir???")
            return None
        lst.sort()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b"<!DOCTYPE html><html><head>")
        self.wfile.write(b"<meta charset='utf-8'>")
        self.wfile.write(("<title>Index of " + self.path + "</title>").encode("utf-8"))

        # fancy css
        self.wfile.write(b"""
        <style>
            body { font-family: sans-serif; font-size:18px; padding: 1rem; max-width:600px; margin:auto; }
            h3 { text-align:center; }
            ul { list-style:none; padding:0; }
            li { margin:10px 0; background:#f2f2f2; padding:12px; border-radius:8px; }
            a { text-decoration:none; color:#007bff; font-weight:500; }
            a:hover { text-decoration:underline; }

            @media (prefers-color-scheme: dark) {
                body { background:#121212; color:#eee; }
                li { background:#1f1f1f; }
                a { color:#4da3ff; }
            }
        </style>
        """)

        self.wfile.write(b"</head><body>")

        self.wfile.write(b"<h3>Index of: ")

        # add parent directory link if not root
        parent = os.path.dirname(self.path.rstrip("/"))
        if parent != self.path:
            if parent == "":
                parent = "/"
            self.wfile.write(b'<a href="%s">Parent folder</a><br><br>' % parent.encode("utf-8"))

        self.wfile.write(self.path.encode("utf-8"))
        self.wfile.write(b"</h3><hr><ul>")

        for name in lst:
            fullp = os.path.join(path, name)
            if os.path.isdir(fullp):
                name2 = name + "/"
            else:
                name2 = name
            self.wfile.write(("<li><a href=\"" + name2 + "\">" + name2 + "</a></li>").encode("utf-8"))

        self.wfile.write(b"</ul><hr></body></html>")
        return None

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))  # google dns
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"
    s.close()
    return ip

def show_qr(x):
    if not qrcode:
        print("no qr code thing installed")
        return
    qr = qrcode.QRCode(border=1)
    qr.add_data(x)
    qr.make()
    qr.print_ascii(invert=True)

def start_server(port, dirr, pw, logs):
    os.chdir(dirr)
    HTML.passwd = pw
    HTML.do_logs = logs

    handler = HTML
    serv = socketserver.TCPServer(("", port), handler)

    ip = get_ip()
    url = "http://" + ip + ":" + str(port) + "/"

    print("\n🌉 LocalBridge is running!")
    print(f"📂 Serving directory: {dirr}")
    print(f"📱 Access on network: {url}")

    if pw:
        print(f"🔐 Password enabled: {pw}")

    if logs:
        logging.basicConfig(level=logging.INFO, format="%(message)s")
        print("📝 Logging enabled")

    print("\n📸 Scan this on your phone:")
    show_qr(url)
    print("Press Ctrl+C to stop.\n")

    serv.serve_forever()

def main():
    # args parser
    prsr = argparse.ArgumentParser(description="share files i guess")
    prsr.add_argument("-p", "--port", type=int, default=8000)
    prsr.add_argument("-d", "--directory", default=".")
    prsr.add_argument("--password")
    prsr.add_argument("--log", action="store_true")
    args = prsr.parse_args()

    start_server(args.port, args.directory, args.password, args.log)

main()