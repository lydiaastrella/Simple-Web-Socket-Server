import socket
import base64
import hashlib

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8080        # Port to listen on (non-privileged ports are > 1023)
MAGIC_STRING = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11" #string to concatenate to key

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            dataDecoded = data.decode()
            headers = dataDecoded.split("\r\n")
            if "Connection: Upgrade" in dataDecoded and "Upgrade: websocket" in dataDecoded :
                for x in headers :
                    if "Sec-WebSocket-Key:" in x:
                        key = x.split(" ")[1]
                        key = key + MAGIC_STRING
                        key = key.encode()
                
                responseKey = base64.b64encode(hashlib.sha1(key).digest()).decode()
                response = "HTTP/1.1 101 Switching Protocols\r\n" + \
                            "Upgrade: websocket\r\n" + \
                            "Connection: Upgrade\r\n" + \
                            "Sec-WebSocket-Accept: %s\r\n\r\n"%(responseKey)
                response = response.encode()
                conn.sendall(response)