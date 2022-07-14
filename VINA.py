import sys
sys.dont_write_bytecode = True

from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler
from Sourcer import Sourcer
from NewsBuffer import NEWS_BUFFER

class VINA_Server(BaseHTTPRequestHandler):

	def do_GET(self):
		if len(NEWS_BUFFER):
			self.send_response(200)
			self.send_header("Content-type", "application/json")
			self.end_headers()
			self.wfile.write(bytes(NEWS_BUFFER.pop().toJson(),"utf-8"))


print("\n\nVINA online")
print("---"*10,end="\n\n")

HOST = "raspberrypi.local"
PORT = 1234
sourcer = Sourcer()

print("Searching for articles...")
sourcer_thread = Thread(target=sourcer.start)
sourcer_thread.setDaemon(True)
sourcer_thread.start()

# print(f"Found {len(NEWS_BUFFER)} articles\n\n")

# if len(NEWS_BUFFER) == 0:
#     print("Terminating...")
#     exit(1)

print("Starting server...")

server = HTTPServer((HOST, PORT), VINA_Server)
server_thread = Thread(target=server.serve_forever)
server_thread.setDaemon(True)
server_thread.start()
print(f"Server listening at {HOST} on port: {PORT}...",end="\n\n")
print("---"*10,end="\n\n")


server_thread.join()
server.server_close()
print("Server stopped")
