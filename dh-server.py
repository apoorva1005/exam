import socket, random

s = socket.socket()
s.bind(("localhost", 12345))
s.listen(1)

print("Waiting for client...")
c, addr = s.accept()

msg = c.recv(1024).decode()
print("Request Accepted")

# choose small prime and generator (simple for exam)
P = 23
G = 5

# send P and G
c.send(f"{P},{G}".encode())

# choose private key
Y = random.randint(1, P-1)

# calculate R2
R2 = pow(G, Y, P)
c.send(str(R2).encode())

# receive R1
R1 = int(c.recv(1024).decode())
print("Received R1:", R1)

# secret key
key = pow(R1, Y, P)
print("Server Secret Key:", key)

c.close()