# gcd
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

# modular inverse
def modinv(a):
    for i in range(26):
        if (a*i)%26==1:
            return i

# encrypt
def enc(t,a,b):
    r=""
    for c in t:
        if c.isalpha():
            x=ord(c)-65
            r+=chr((a*x+b)%26 + 65)
        else:
            r+=c
    return r

# decrypt
def dec(t,a,b):
    r=""
    a_inv = modinv(a)
    for c in t:
        if c.isalpha():
            x=ord(c)-65
            r+=chr((a_inv*(x-b))%26 + 65)
        else:
            r+=c
    return r

# main
t = input("Text: ").upper()
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if gcd(a,26)!=1:
    print("Invalid key")
else:
    c = enc(t,a,b)
    print("Cipher:", c)
    print("Decrypted:", dec(c,a,b))