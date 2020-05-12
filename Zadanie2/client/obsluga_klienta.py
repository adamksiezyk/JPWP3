import socket
import json
import time as t


class Siec:
    def __init__(self, nazwa):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 8000
        self.adres = (self.server, self.port)
        self.nazwa = nazwa
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.adres)
            self.client.sendall(self.nazwa.encode())
            return json.loads(self.client.recv(2048))
        except Exception as e:
            self.disconnect(e)

    def send(self, data):
        try:
            self.client.send(json.dumps(data).encode())

            d = ""
            while 1:
                last = self.client.recv(1024).decode()
                d += last
                try:
                    if d.count(".") == 1:
                        break
                except:
                    pass

            try:
                if d[-1] == ".":
                    d = d[:-1]
            except:
                pass

            keys = [key for key in data.keys()]
            return json.loads(d)[str(keys[0])]
        except socket.error as e:
            self.disconnect(e)

    def disconnect(self, msg):
        print("[EXCEPTION] Rozłączono z serwerem:", msg)
        self.client.close()
