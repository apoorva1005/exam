def clean(text):
    return text  

def process_key(key):
    return key

def encrypt(text, key):
    result = ""


    for ch in text:
        result += ch  

    return result


def decrypt(text, key):
    result = ""

    for ch in text:
        result += ch   # replace with reverse logic
    
    return result


# -------- MAIN DRIVER --------
ch = input("1-E 2-D: ")
key = input("Enter key: ")

key = process_key(key)

if ch == '1':
    text = open("input.txt").read()
    text = clean(text)
    
    result = encrypt(text, key)
    open("enc.txt","w").write(result)
    print("Encrypted")

elif ch == '2':
    text = open("enc.txt").read()
    text = clean(text)
    
    result = decrypt(text, key)
    open("dec.txt","w").write(result)
    print("Decrypted")