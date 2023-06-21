import os,socket,json,time
from socket import SOL_SOCKET


sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET,socket.SO_BROADCAST,1)
filesPath=input("Please enter the path of the directory which you have your files on.-Without quotation marks-")
while True:
    inHost=input("Please enter the name of the file you initially want to host with the extension") 
    inHost=filesPath+"\\"+inHost
    if(os.path.isfile(inHost)):
        print("Initial file has been found. Starting to announce...")
        break
    else:
        print("That file could not be found in your file directory.")
fileList={"chunks":os.listdir(filesPath)}
fListJson=json.dumps(fileList)
with open("contents.json", "w") as outfile:
    outfile.write(fListJson)
    outfile.close()
while True:
    sock.sendto(bytes(fListJson,"utf-8"),("255.255.255.255",5001))
    print("An announcement has been done")
    time.sleep(60)
