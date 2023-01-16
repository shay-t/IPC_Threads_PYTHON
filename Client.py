from threading import Thread
import socket
import sys
from PyQt5 import QtWidgets , uic,QtGui
def Send(socket):
    while True:
        msg = input()
        msg2 = msg.encode('utf-8')
        socket.send(msg2)
def Reception(socket):
    while True:
        requete_server = socket.recv(1024)
        requete_server = requete_server.decode("utf-8")
        print("Server :"+str(requete_server))             
Host = "127.0.0.1"
Port = 6390
#Création du socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((Host,Port))

envoi = Thread(target=Send,args=[socket])
recep = Thread(target=Reception,args=[socket])
envoi.start()
recep.start()
