# Public values
p = 23
g = 5

# Server private key
y = int(input("Enter server private key (y): "))

# Server public key
R2 = pow(g, y, p)
print("Server public key (R2):", R2)

# Receive client public key
R1 = int(input("Enter client public key (R1): "))

# Shared secret key
K = pow(R1, y, p)
print("Server Secret Key:", K)