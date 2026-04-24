# gcd
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

# modular inverse
def modinv(e,phi):
    for d in range(1,phi):
        if (e*d)%phi==1:
            return d

# RSA
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

n = p*q
phi = (p-1)*(q-1)

# choose e
e = 2
while gcd(e,phi)!=1:
    e+=1

# find d
d = modinv(e,phi)

print("Public key:", (e,n))
print("Private key:", (d,n))

# encrypt
m = int(input("Enter message (number): "))
c = pow(m,e,n)
print("Cipher:", c)

# decrypt
m2 = pow(c,d,n)
print("Decrypted:", m2)