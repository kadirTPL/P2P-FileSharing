import socket,json 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 5001))
#sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
contentDictionary={"files":"addresses"}
while True:
    data,address=sock.recvfrom(2048)
    inContDict=json.loads(data)
    IPaddr=address[0]
    contNameList=inContDict["chunks"]
  
    for cont in contNameList:
      if cont in contentDictionary.keys():
          addrList=list(contentDictionary[cont])
          if IPaddr not in addrList:
              addrList[len(addrList)]=IPaddr
      else:
          addrList=[IPaddr]
      contentDictionary[cont]=addrList  

    contDictJson=json.dumps(contentDictionary)
    with open("content_dictionary.txt", "w") as outfile:
        outfile.write(contDictJson)
        outfile.close()
    print({IPaddr:contNameList})


