import socket
ports = [21, 23, 80, 443, 8080]

def scan(target):
	for port in ports:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(0.1)
		code = client.connect_ex((target, port))
		print("|Port:", port, "|Status:", code,)

flag = True
while flag:
	 target	= input("Please type your target, 0 to exit: ")
	 if (target == "0"):
	 		flag = False
	 else:
	 	scan(target)			
