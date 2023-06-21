

from pickle import TRUE
import socket,json
from datetime import datetime
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

while True:
    filePath=input("Please enter your file directory which you have your files on with \" \\ at the end \" ")
    fileToDownload=input("Please enter the name of the file you want to download with extension.")
    fileName=fileToDownload.split(".")[0]
    reqMsg={"requested_content":fileName}
    reqJson=json.dumps(reqMsg)
    cont=json.loads(open("content_dictionary.txt","r").read())
    DownAddrList=cont[fileToDownload]
    for IPaddr in DownAddrList:
        sock.connect((IPaddr,5000))
        sock.send(bytes(reqJson,"utf-8"))
        incomingFile=open(filePath+fileToDownload,"wb")
       
       
        done=False
        while True:
            dFile=sock.recv(1024)
            print(len(dFile))
            if(len(dFile)<1024):
                
                done=True
                downLog=open("download_log.txt","w")
                date=datetime.now()
                date=str(date)
                downLog.write(date+" " + fileToDownload+" "+IPaddr)
                downLog.close()  
                break
            
            incomingFile.write(dFile)

        if done:
            break
        if(IPaddr==DownAddrList[len(DownAddrList)-1]): 
            print("This file could not be downloaded.")
        incomingFile.close()    
            