# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('192.168.43.176', port)) #server ip 
  
# receive data from the server 
print s.recv(1024) 
print s.recv(1024) 
s.send(b'its working')
# close the connection 
s.close() 
