
import time
from socketserver import ThreadingMixIn
from http import server

class RequestHandler(server.SimpleHTTPRequestHandler):

    def do_GET(self):
        start_time = time.time()
        time.sleep(5)
        end_time = time.time()

        self.send_response(200, "OK")
        self.end_headers()

        response = (
                "Started {}, ended {}".format(
                    start_time, end_time)
                )

        self.wfile.write(response.encode('utf-8'))

        return

class ThreadedHTTPServer(ThreadingMixIn, server.HTTPServer):
	daemon_threads = True

with ThreadedHTTPServer(
        ('localhost', 8000), RequestHandler
) as http_server:
        http_server.serve_forever()
