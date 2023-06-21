import json
import socket
from datetime import datetime
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("",5000))
sock.listen(1)
while True:
    dSock,addr=sock.accept()
    requestedJson=dSock.recv(1024)
    requestedFile=json.loads(requestedJson)
    filePath=input("Please enter your file directory which you have your files on with \" \\ at the end \" ")
    fName=requestedFile["requested_content"]
    fName=filePath+fName+".png" #extension can be changed for different types of file usages
    uFile=open(fName,"rb")
    data=uFile.read()
    dSock.send(data)
    upLog=open("upload_log.txt","w")
    currentTime=datetime.now()
    currentTime=str(currentTime)
    upLog.write(currentTime+" "+ fName + " "+addr[0])
    uFile.close()
    upLog.close()