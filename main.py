from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

memory = []
form = '''<!DOCTYPE html>
  <title>Udacian</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="name">name</textarea>
    <br>
    <textarea name="city">city</textarea>
    <br>
    <textarea name="enrollment">enrollment</textarea>
    <br>
    <textarea name="nanodegree">nanodegree</textarea>
    <br>
    <textarea name="status">status</textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):

      length = int(self.headers.get('Content-length', 0))
      body = self.rfile.read(length).decode()
      params = parse_qs(body) 

      # Send the "message" field back as the response.
      self.send_response(200)
      self.send_header('Content-type', 'text/plain; charset=utf-8')
      self.end_headers()
      self.wfile.write("my name is {} in {} studing {} nanodegree with Ms {} , she is {}".format(params["name"][0],params["city"][0],params["enrollment"][0], params["nanodegree"][0],params["status"][0]).encode())
      # self._set_headers()

    def do_GET(self):
      self.send_response(200)
      self.send_header('Content-type', 'text/html; charset=utf-8')
      self.end_headers()
		  # Send the html message
      self.wfile.write(form.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()