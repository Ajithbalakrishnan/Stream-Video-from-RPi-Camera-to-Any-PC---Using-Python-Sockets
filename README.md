# Stream-Video-from-RPi-Camera-to-Any-PC---Using-Python-Sockets
Live video straming from any RPI camera to pc which is connected in same network.

# Server Side Requirements.


1. pip install pillow


2.pip install matplotlib

3.install ffmpeg

4.install opencv


# Steps

1.Connect both devices in same wifi network.


2.find ip addresss of both devices.


3.copy the ip address of server in both code.


4.Run server code first


  python server.py
  
  
5.Then run client code.


  python client.py
  
  
  # Using RTSP
1. run the below code in RPI


 $raspivid -o - -t 0 -n -w 320 -h 240 -fps 30| cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8000/}' :demux=h264
 
 
2. run the below code at server


ffplay rtsp://192.168.43.85:8000/



for more ref: https://raspberry-projects.com/pi/pi-hardware/raspberry-pi-camera/streaming-video-using-vlc-player



