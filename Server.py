from threading import Thread
import socket
import sys
from PyQt5 import QtWidgets , uic,QtGui
def Send(client):
    while True:
        msg=input()
        msg = msg.encode("utf-8")
        client.send(msg)
def Reception(client):
    while True:
        requete_client = client.recv(500)
        requete_client = requete_client.decode('utf-8')
        out="Client :"+requete_client
        if not requete_client : #Si on pert la connexion
            out="CLOSE"
            break
        print(out) 
Host = "127.0.0.1"
Port = 6390
#Création du socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((Host,Port))
socket.listen(1)

#Le script s'arrête jusqu'a une connection
client, ip = socket.accept()
print("Le client d'ip",ip,"s'est connecté")

envoi = Thread(target=Send,args=[client])
recep = Thread(target=Reception,args=[client])
#App=QtWidgets.QApplication(sys.argv)
#sc=uic.loadUi("IPC.ui")
#sc.setWindowTitle("Server")
#sc.send_2.clicked.connect(send)
#sc.show()
#App.exec_()
#App.exit()
envoi.start()
recep.start()

recep.join()

client.close()
socket.close()
