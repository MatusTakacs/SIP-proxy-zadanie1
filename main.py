import Sip_Proxy_lib 
import socket
import re
import socketserver
import string
import socket
#import threading
import sys
import time
import logging





if __name__ == "__main__": 

    handler = Sip_Proxy_lib.UDPHandler

    HOST, PORT = "192.168.1.131", 5060

    Sip_Proxy_lib.registrar = {}
    Sip_Proxy_lib.recordroute = ""
    Sip_Proxy_lib.topvia = ""


    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',level=logging.INFO,datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    ipaddress = socket.gethostbyname(socket.gethostname())
    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[1]
    logging.info(ipaddress)
    Sip_Proxy_lib.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress,PORT)
    Sip_Proxy_lib.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress,PORT)
    server = socketserver.UDPServer((ipaddress, PORT), handler)
    print("Proxy server started at <%s:%s>" % (ipaddress, PORT))
    server.serve_forever()