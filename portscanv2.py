import socket 
import sys

def is_port_open(host, port): #return boolean
	try:
		sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		sock.settimeout(0.05)
		sock.connect((host, port))
	except socket.error:
		return False
	return True	
print("Please wait...")
for port in range(20, 85):
	if is_port_open(sys.argv[1], port):
		print("{} is OPEN".format(port))
