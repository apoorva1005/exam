# Public values
p = 23
g = 5

# Private keys
x = int(input("Enter client private key (x): "))
y = int(input("Enter server private key (y): "))

# Public keys
R1 = pow(g, x, p)   # g^x mod p
R2 = pow(g, y, p)   # g^y mod p

print("R1 (Client public):", R1)
print("R2 (Server public):", R2)

# Shared secret key
K1 = pow(R2, x, p)  # (R2)^x mod p
K2 = pow(R1, y, p)  # (R1)^y mod p

print("Client Secret Key:", K1)
print("Server Secret Key:", K2)