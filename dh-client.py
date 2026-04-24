import socket

s = socket.socket()
s.connect(("localhost", 12345))

# send request
s.send("Request".encode())

# receive P and G
data = s.recv(1024).decode()
P, G = map(int, data.split(","))
print("P:", P, "G:", G)

# receive R2
R2 = int(s.recv(1024).decode())

# choose private key
X = int(input("Enter private key X: "))

# calculate R1
R1 = pow(G, X, P)
s.send(str(R1).encode())

print("Received R2:", R2)

# secret key
key = pow(R2, X, P)
print("Client Secret Key:", key)

s.close()