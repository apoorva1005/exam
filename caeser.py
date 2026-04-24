t = open(input("Input file: ")).read()
k = int(input("Key: "))

c = ""
for ch in t:
    if ch.isalpha():
        c += chr((ord(ch)-65+k)%26 + 65)
    else:
        c += ch

open("cipher.txt","w").write(c)

# decrypt
k2 = int(input("Decrypt key: "))
r = ""
for ch in c:
    if ch.isalpha():
        r += chr((ord(ch)-65-k2)%26 + 65)
    else:
        r += ch

open("recovery.txt","w").write(r)