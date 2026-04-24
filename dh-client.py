# Public values
p = 23
g = 5

# Client private key
x = int(input("Enter client private key (x): "))

# Client public key
R1 = pow(g, x, p)
print("Client public key (R1):", R1)

# Receive server public key
R2 = int(input("Enter server public key (R2): "))

# Shared secret key
K = pow(R2, x, p)
print("Client Secret Key:", K)