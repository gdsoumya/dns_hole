import socketserver as SocketServer, threading, time
import socket
from ast import literal_eval
import binascii
from dnslib import *
import sys
from colorama import Fore, init
from time import sleep


ag=False # aggressive mode flag

'''
ThreadedUDPRequestHandler: Handles DNS Requests according to Blocklist and User Preferences
'''
class ThreadedUDPRequestHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):
        block=False
        global ag
        data = self.request[0]
        sock = self.request[1]
        sockOut = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        decode = DNSRecord.parse(data)
        query = str(decode.get_q())
        query = query[1:query.rindex('.')]
        ids = int(decode.header.id)
        decode.header = DNSHeader(id=ids,qr=1,aa=1,ra=1)

        if ag and ("ad" in query or query in blockList):
            block=True
        elif not ag and query in blockList:
            block=True
    
        if block:
            decode.add_answer(RR(query,QTYPE.A,rdata=A("0.0.0.0")))
            sock.sendto(bytes(decode.pack()), self.client_address)
            print(Fore.RED+"Blocked"+Fore.YELLOW+" || "+Fore.RED+"SOURCE IP : "+self.client_address[0]+Fore.YELLOW+" || "+Fore.RED+"QUERY : "+query,end="\n",flush=True)
        else :
            sockOut.sendto(data, ('8.8.8.8', 53))
            data, addr1 = sockOut.recvfrom(512)
            sock.sendto(data, self.client_address)
            print(Fore.GREEN+"ALLOWED"+Fore.YELLOW+" || "+Fore.GREEN+"SOURCE IP : "+self.client_address[0]+Fore.YELLOW+" || "+Fore.GREEN+"QUERY : "+query,end="\n",flush=True)

        return
        

class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass

'''
setup() : Loads the Blocklist
'''
def setup():
    global blockList
    file=open("BlockList.txt","r")
    blockList=file.readlines()
    file.close()
    blockList=[i.strip() for i in blockList]



if __name__ == "__main__":
    setup()
    init(autoreset=True)
    HOST, PORT = "0.0.0.0", 53
    logo='''

  _____  _   _  _____   _    _  ____  _      ______ 
 |  __ \| \ | |/ ____| | |  | |/ __ \| |    |  ____|
 | |  | |  \| | (___   | |__| | |  | | |    | |__   
 | |  | | . ` |\___ \  |  __  | |  | | |    |  __|  
 | |__| | |\  |____) | | |  | | |__| | |____| |____ 
 |_____/|_| \_|_____/  |_|  |_|\____/|______|______|
                                                    
                                                    
'''
    print(Fore.YELLOW + logo)
    while True:
        print("Use Aggressive Mode (Blocks all urls with keyword \"AD\") [y/n]",end=' : ')
        ag= input()[0]
        if ag in "yY":
            print(Fore.GREEN+"\n** AGGRESSIVE MODE ON **\n")
            ag=True
            break
        elif ag in "nN":
            ag=False
            print(Fore.BLUE+"\n** AGGRESSIVE MODE OFF **\n")
            break
        else:
            print(Fore.RED+"\n**Please Enter y/Y for yes and n/N for No**\n")
    try:
        server = ThreadedUDPServer((HOST, PORT), ThreadedUDPRequestHandler)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
    except PermissionError:
        print(Fore.RED+"!! RUN AS ROOT !!\n")
        exit()
    except OSError as e:
        if "Address already in use" in str(e):
            print(Fore.RED+"!! Port 53 is already in use !!\n")
        else:
            print(Fore.RED+e.message)
        exit()
    except Exception as e:
        print(Fore.RED+e.message)
        exit()

    try:
        server_thread.start()
        print(Fore.YELLOW + "Server started at {} port {}\n".format(HOST, PORT))
        while True: time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        print(Fore.BLUE+"\n\n!! SHUTTING DOWN !!\n")
        sys.stdout = open(os.devnull, "w")
        sys.stderr = open(os.devnull, "w")
        server.shutdown()
        server.server_close()
        sleep(3)
        exit()
