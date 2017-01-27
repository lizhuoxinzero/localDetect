import socket

address = ('<broadcast>', 38080)
addlisten = ('', 38081)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR|socket.SO_BROADCAST,1)

s.bind(addlisten)
msg = "IS RASPBERRY!"
s.sendto(msg, address)

s.settimeout(10)
count = 0;
try:
    while True:
        data, addr = s.recvfrom(2048)
        print "received:", data
        count += 1
except Exception as ex:
    print(str(ex))
    if count == 0:
        print "there is no raspberry"

s.close
