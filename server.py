import socket
import base64
import hashlib
import threading

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

def build_frame(data, isText):
    listFrame = []
    frame = b''
    mask = 0x0

    if (isText):
        opcode = 0x1
    else :
        opcode = 0x2
    
    if (len(data)//125 == 0):
        fin = 0x1
        payload_len = len(data)
        byte1 = fin << 7 | opcode
        byte2 = mask << 7 | payload_len
        frame = bytes(byte1 + byte2) + data
        listFrame.append(frame)
    else :
        for i in range(len(data)//125):
            if ((i == len(data)//125 -1)  and (len(data) % 125 == 0)):
                fin = 0x1
            else :
                fin = 0x0
            payload_len = 125
            byte1 = fin << 7 | opcode
            byte2 = mask << 7 | payload_len
            frame = bytes(byte1 + byte2) + data[i*125 : (i+1) *125]
            listFrame.append(frame)
        if (len(data) % 125 != 0):
            fin = 0x1
            payload_len = len(data) % 125
            byte1 = fin << 7 | opcode
            byte2 = mask << 7 | payload_len
            frame = bytes(byte1 + byte2) + data[(len(data)//125)*125 :]
            listFrame.append(frame)
    return listFrame

def mainThread(conn, addr):
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

            #j = 1
            while True:
                #print(j)
                #j = j + 1
                while True:
                    frame = bytearray(conn.recv(65536))
                    byte1 = frame[0]
                    fin = byte1 >> 7
                    opcode = byte1 & 0x0F

                    if (opcode == 0x8):
                        return 
                        #kirim close
                    if (opcode == 0x1):
                        isText = True
                        data = b''
                    elif (opcode == 0x2):
                        isText = False
                        data = b''

                    data += decodeFrame(frame, data)
                    if (fin == 1):
                        #print("fin " + str(j))
                        break

                if (isText):
                    #print(data)
                    decoded_data = data.decode()
                    if ("!echo " in decoded_data):
                        #print("masuk !echo")
                        phrase = decoded_data.replace("!echo ", "")
                        listFrame = build_frame(data, isText)
                        for i in listFrame :
                            conn.sendall(i)
                    elif ("!submission" in decoded_data):
                        #print("masuk !submission")
                        try:
                            file = open("Simple-Websocket-Server.zip",'rb')
                        except IOError:
                            print('Unable to open', filename)
                            return    
                        bytes_from_file = file.read()
                        listFrame = build_frame(bytes_from_file,False) #isText is False
                        for i in listFrame :
                            conn.sendall(i)
                        #print("beres !submission")
                else:
                    print("!bukan text")
                    #cek cheksum 
                        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            threading.Thread(target=mainThread, args=(conn, addr), daemon=True).start()