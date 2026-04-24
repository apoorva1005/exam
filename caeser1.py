def is_english(t):
    words = [" the ", " and ", " is ", " to ", " of "]
    count = 0
    for w in words:
        if w in t.lower():
            count += 1
    return count >= 2


print("1 Encrypt  2 Decrypt  3 Brute  4 Auto")
ch = int(input("Choice: "))

# -------- ENCRYPT --------
if ch == 1:
    text = open("plain_text.txt").read()
    key = int(input("Key: "))
    
    cipher = ""
    for c in text:
        cipher += chr((ord(c) + key) % 255)
    
    open("cipher.txt","w").write(cipher)
    print("Encrypted")

# -------- DECRYPT --------
elif ch == 2:
    text = open("cipher.txt").read()
    key = int(input("Key: "))
    
    plain = ""
    for c in text:
        plain += chr((ord(c) - key) % 255)
    
    open("recover.txt","w").write(plain)
    print("Decrypted")

# -------- BRUTE FORCE --------
elif ch == 3:
    text = open("cipher.txt").read()
    
    for key in range(4,255):
        result = ""
        for c in text:
            result += chr((ord(c) - key) % 255)
        
        print(result)
        if input("Correct? y/n: ") == "y":
            print("Key =", key)
            break

# -------- AUTO BRUTE --------
elif ch == 4:
    text = open("cipher.txt").read()
    
    for key in range(4,255):
        result = ""
        for c in text:
            result += chr((ord(c) - key) % 255)
        
        if is_english(result):
            print(result)
            print("Key =", key)
            break