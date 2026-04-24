def order(k):
    return [sorted(k).index(c) for c in k]

def enc():
    k=input("Key: ")
    t=open("Plaintext.txt").read().replace("\n","")
    c=len(k); r=(len(t)+c-1)//c
    t+= "X"*(r*c-len(t))

    m=[list(t[i*c:(i+1)*c]) for i in range(r)]
    o=order(k)

    res=""
    for n in range(c):
        col=o.index(n)
        for i in range(r):
            res+=m[i][col]

    open("Cipher.txt","w").write(res)
    print("Done")

def dec():
    k=input("Key: ")
    t=open("Cipher.txt").read()
    c=len(k); r=len(t)//c
    o=order(k)

    m=[[""]*c for _ in range(r)]
    x=0
    for n in range(c):
        col=o.index(n)
        for i in range(r):
            m[i][col]=t[x]; x+=1

    res=""
    for row in m:
        res+="".join(row)

    open("Recover.txt","w").write(res.rstrip("X"))
    print("Done")

ch=input("1-E 2-D: ")
if ch=='1': enc()
else: dec()