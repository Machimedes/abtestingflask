from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from confluent_kafka import Producer
import socket

hostName = "localhost"
serverPort = 8087
conf = {'bootstrap.servers': "host1:9092,host2:9092",
        'client.id': hostName}

producer = Producer(conf)

def produce(topic):
    producer.produce(topic, key="key", value="value")

class extractRequestBody(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("received get request")

    def do_POST(self):
        """Reads post request body"""
        self._set_headers()
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        self.wfile.write(bytes("received post request:<br>{}".format(post_body), "utf-8"))

    def do_PUT(self):
        self.do_POST()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), extractRequestBody)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
