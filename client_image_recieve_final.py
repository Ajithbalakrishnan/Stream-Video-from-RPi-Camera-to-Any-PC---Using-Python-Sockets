import cv2
import io
import socket
import struct
import time
import pickle
import zlib
import subprocess

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST='192.168.43.176'
PORT=8484
client_socket.connect((HOST, PORT))
#connection = client_socket.makefile('rb')
bashCommand ='lsof -nti:'+str(PORT)+' | xargs kill -9'
data = b""
payload_size = struct.calcsize(">L")
print("payload_size: {}".format(payload_size))
while True:
    frame_1=cv2.imread('/home/pi/ajith/sending_img/default.jpg')
    frame_1=cv2.resize(frame_1, (500,300))
    cv2.imshow('ImageWindow',frame_1)
    cv2.waitKey(1000)
    while len(data) < payload_size:
        print("Recv: {}".format(len(data)))
        data += client_socket.recv(4096)

    print("Done Recv: {}".format(len(data)))
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    print("msg_size: {}".format(msg_size))
    while len(data) < msg_size:
        data += client_socket.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    frame=cv2.resize(frame, (500,300)) 
    cv2.imshow('ImageWindow',frame)
    cv2.imwrite('cam/'+'one'+'.jpg',frame)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    
client_socket.shutdown()
client_socket.close()
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()




