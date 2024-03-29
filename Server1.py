#!/usr/bin/python

# Import all from module socket
from socket import *
#import socket

#Importing all from thread
from thread import *
#import threading

# Defining server address and port
host = ''  #'localhost' or '127.0.0.1' or '' are all same
port = 9999 #Use port > 1024, below it all are reserved

#Creating socket object
sock = socket()
#Binding socket to a address. bind() takes tuple of host and port.
sock.bind((host, port))
#Listening at the address
sock.listen(5) #5 denotes the number of clients can queue

def clientthread(conn, number):
#infinite loop so that function do not terminate and thread do not end.
    while True:
#Receiving from client
        data = conn.recv(1024) # 1024 stands for bytes of data to be received
#Sending message to connected client
        conn.send('Hi! I am server\n') #send only takes string
        print data, number

tdNum = 1

while True:
#Accepting incoming connections
    conn, addr = sock.accept()
    tdNum = tdNum + 1 # tread number 
    print addr
#Creating new thread. Calling clientthread function for this function and passing conn as argument.
    start_new_thread(clientthread,(conn,tdNum,)) #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    

conn.close()
sock.close()

