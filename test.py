from stem import Signal
from stem.control import Controller
import requests
import time

def new_ip():
    with Controller.from_port(address="127.0.0.1", port=9051) as c:

        c.authenticate()
        c.signal(Signal.NEWNYM)

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050",
}

new_ip()
time.sleep(5)

print(requests.get("https://api.ipify.org").text)              # Gerçek IP
print(requests.get("https://api.ipify.org", proxies=proxies).text)  # Tor IP

# print("IP:", r.text)
