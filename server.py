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

def build_close_frame(frame):
    data = decodeFrame(frame)
    fin= 0x1
    opcode = 0x8
    mask = 0x0
    if(len(data)<=125):
        payload_len = len(data)
        byte1 = fin << 7 | opcode
        byte2 = mask << 7 | payload_len
        frame = bytes([byte1]) + bytes([byte2]) + data
    else:
        payload_len = 125
        byte1 = fin << 7 | opcode
        byte2 = mask << 7 | payload_len
        frame = bytes([byte1]) + bytes([byte2]) + data[0:125]
    return frame

def decodeFrame(frame) :
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

    frame_data=b''
    for i in range (startPayload, len(frame)):
        frame_data += bytes([frame[i] ^ maskingKey[(i - startPayload)%4]])
    return frame_data

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8080        # Port to listen on (non-privileged ports are > 1023)
MAGIC_STRING = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11" #string to concatenate to key

def build_frame(data, data_type):
    listFrame = []
    frame = b''
    mask = 0x0

    if (data_type == 'text'):
        opcode = 0x1
    elif(data_type == 'binary') :
        opcode = 0x2
    else:
        opcode = 0xA

    if (len(data)//125 == 0):
        fin = 0x1
        payload_len = len(data)
        byte1 = fin << 7 | opcode
        byte2 = mask << 7 | payload_len
        frame = bytes([byte1]) + bytes([byte2]) + data
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
            frame = bytes([byte1]) + bytes([byte2]) + data[i*125 : (i+1) *125]
            listFrame.append(frame)
            opcode = 0x0
        if (len(data) % 125 != 0):
            fin = 0x1
            payload_len = len(data) % 125
            byte1 = fin << 7 | opcode
            byte2 = mask << 7 | payload_len
            frame = bytes([byte1]) + bytes([byte2]) + data[(len(data)//125)*125 :]
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

            while True:
                while True:
                    frame = bytearray(conn.recv(65536))
                    if(frame):
                        byte1 = frame[0]
                        fin = byte1 >> 7
                        opcode = byte1 & 0x0F

                        if (opcode == 0x8):
                            frame_close = build_close_frame(frame)
                            conn.sendall(frame_close)
                            conn.close()
                            return 
                            #kirim close
                        elif (opcode == 0x1):
                            data_type = 'text'
                            data = b''
                        elif (opcode == 0x2):
                            data_type = 'binary'
                            data = b''
                        elif (opcode == 0x9):
                            data_type = 'ping'

                        if(data_type != 'ping'):
                            data += decodeFrame(frame)
                            if (fin == 1):
                                break
                        else:
                            ping_data = decodeFrame(frame)
                            pong_frame = build_frame(ping_data,data_type)
                            conn.sendall(pong_frame[0])

                if (data_type == 'text'):
                    decoded_data = data.decode()
                    if ("!echo " in decoded_data):
                        phrase = decoded_data.replace("!echo ", "")
                        listFrame = build_frame(phrase.encode(), data_type)
                        for i in listFrame :
                            conn.sendall(i)
                    elif ("!submission" in decoded_data):
                        try:
                            file = open("Simple-Websocket-Server.zip",'rb')
                        except IOError:
                            print('Unable to open file')
                            return    
                        bytes_from_file = file.read()
                        file.close()
                        original_checksum = hashlib.md5(bytes_from_file).hexdigest()
                        listFrame = build_frame(bytes_from_file,'binary')
                        for i in listFrame :
                            conn.sendall(i)
                elif(data_type == 'binary'):
                    #cek cheksum 
                    returned_checksum = hashlib.md5(data).hexdigest()
                    try:
                        file = open("Simple-Websocket-Server.zip",'rb')
                    except IOError:
                        print('Unable to open file')
                        return    
                    bytes_from_file = file.read()
                    file.close()
                    original_checksum = hashlib.md5(bytes_from_file).hexdigest()
                    if(returned_checksum.lower() == original_checksum.lower()):
                        response_frame = build_frame('1'.encode(),'text')
                    else:
                        response_frame = build_frame('0'.encode(),'text')
                    conn.sendall(response_frame[0]) 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            threading.Thread(target=mainThread, args=(conn, addr), daemon=True).start()