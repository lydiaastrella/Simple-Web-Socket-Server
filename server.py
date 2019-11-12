import socket
import base64
import hashlib

def handShake(key):
    key = key + MAGIC_STRING
    key = key.encode()

    responseKey = base64.b64encode(hashlib.sha1(key).digest()).decode()
    response = "HTTP/1.1 101 Switching Protocols\r\n" + \
            "Upgrade: websocket\r\n" + \
            "Connection: Upgrade\r\n" + \
            "Sec-WebSocket-Accept: %s\r\n\r\n"%(responseKey)
    return (response.encode())

def decodeFrame(frame, data) :
    byte2 = frame[1]
    mask = byte2 >> 7
    payload_len = byte2 & 0x7F

    if ((payload_len ^ 0) <= 125):
        maskingKey = frame[2:6]
        startPayload = 6
    elif ((payload_len ^ 0) ==  126):
        maskingKey = frame[4:8]
        startPayload = 8
    elif ((payload_len ^ 0 ) == 127):
        maskingKey = frame[10:14]
        startPayload = 14

    for i in range (startPayload, len(frame)):
        data += bytes([frame[i] ^ maskingKey[(i - startPayload)%4]])
    return data

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
                        
                conn.sendall(handShake(key))

                i = 1
                while True:
                    frame = bytearray(conn.recv(65536))
                    while True:
                        byte1 = frame[0]
                        fin = byte1 >> 7
                        opcode = byte1 & 0x0F
                        
                        if (opcode == 0x8):
                            break
                        if (opcode == 0x1):
                            isText = True
                            data = b''
                        elif (opcode == 0x2):
                            isText = False
                            data = b''

                        data += decodeFrame(frame, data)
                        if (fin == 1):
                            break

                    if (isText):
                        print(data)
                        decoded_data = data.decode()
                        if (decoded_data.find("!echo ",0,6)==0):
                            phrase = decoded_data.replace("!echo ", "")
                            

                            conn.sendall(phrase.encode())
                        elif ("!submission"):
                            print("!submission")
                            #kirim source code
                    else:
                        print("!bukan text")
                        #cek cheksum 
                    
