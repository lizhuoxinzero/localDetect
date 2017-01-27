import socket
import netifaces
import json

address =('', 38080)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR|socket.SO_BROADCAST,1)
s.bind(address)

while True:
    data, addr = s.recvfrom(2048)
    if not data:
        print "client has exist"
        break
    if data == "IS RASPBERRY!":
        print "received:", data, "from", addr
        #get ip and name
        hostname = socket.gethostname()
        results = []
        for i in netifaces.interfaces():
            info = netifaces.ifaddresses(i)
            if netifaces.AF_INET not in info:
                continue
            results.append(info[netifaces.AF_INET][0]['addr'])
        msg = "%s %s"%(hostname, json.dumps(results))
        print(msg)
        s.sendto(msg, addr)

s.close()
