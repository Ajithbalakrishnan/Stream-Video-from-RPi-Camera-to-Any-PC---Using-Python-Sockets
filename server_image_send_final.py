import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import zlib
import subprocess

HOST='192.168.43.176'
PORT=8484

bashCommand ='lsof -nti:'+str(PORT)+' | xargs kill -9'

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

server_socket.bind((HOST,PORT))
print('Socket bind complete')
server_socket.listen(10)
print('Socket now listening')
connection,fff = server_socket.accept()

img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 80]
print("start")
while True:
    input1 = input('Enter the IMG number: ') 
    print(input1)
    if input1 == 5:
        connection.close()
        server_socket.shutdown()
        server_socket.close()
        break
    img = cv2.imread('/home/ajith/vijnalabs/Assignments/RPI_live_stream/python-video-stream/sending_image/'+input1+'.jpg')
    result, frame = cv2.imencode('.jpg', img, encode_param)
    data = pickle.dumps(frame, 0)
    size = len(data)

    print("Almost")
    print("{}: {}".format(img_counter, size))
    connection.sendall(struct.pack(">L", size) + data)

connection.close()
server_socket.close()
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()