from stem import Signal
from stem.control import Controller
import subprocess
import requests
import time
from colorama import Fore, Style
from symbols import *

class Guide:
    def __init__(self, address="127.0.0.1", port=9051):
        self.address = address
        self.port = port
    
    def log(self, msg, msg_type=0):
        print(f"{LOG.get(msg_type, '[?] ')}{msg}")
        
    def create_identity(self):
        with Controller.from_port(address=self.address, port=self.port) as c:
            self.log("Creating Tor Identity", 0)
            c.authenticate()
            c.signal(Signal.NEWNYM)
        self.log("NEWNYM signal sent", 0)

    


proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050",
}

#Session
session = requests.Session()
session.proxies.update(proxies)
session.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    )
})

def cmd():
    guide = Guide()

    while True:
        shell = input("Guide> ").strip()

        parts = shell.split()

        if not parts:
            continue
        #TOR
        if parts[0] == "tor":
            if len(parts) > 1 and parts[1] == "start":
                guide.create_identity()
            elif len(parts) > 1 and parts [1] == "check":
                result = subprocess.run(
                    "netstat -ano | findstr 9050",
                    shell=True,
                    capture_output=True,
                    text=True
                )
                if result.stdout:
                    guide.log("TOR SOCKS is opened", 0)
                    print(result.stdout)  
            else:
                guide.log("USE WITH : tor start", 0)
            

cmd()




