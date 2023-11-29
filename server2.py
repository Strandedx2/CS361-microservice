# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        # Set CORS headers to allow all origins 
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS') 
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        f = open('../../budget-app/server/pipline.txt', 'r+')
        number = f.readline()
        f.truncate(0)
        f.close
        # print(number)

        print('read this: ', number, "type: ",type(number))
        newnum = float(number)

        roundednumber = round(newnum, 2)

        f = open('../../budget-app/server/pipline.txt', 'r+')
        # f = open('pipline.txt', 'r+')
        f.write(str(roundednumber))
        f.close()

        response_data = {"number": str(roundednumber)}
        response_json = json.dumps(response_data)
        # self.wfile.write(bytes(str(roundednumber), "utf-8"))
        self.wfile.write(response_json.encode("utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")