def enc(t,k):
    if k==1: return t
    r=[""]*k; i=0; d=1
    for c in t:
        r[i]+=c
        if i==0: d=1
        elif i==k-1: d=-1
        i+=d
    return "".join(r)

def dec(t,k):
    if k==1: return t
    p=[]; i=0; d=1
    for _ in t:
        p.append(i)
        if i==0: d=1
        elif i==k-1: d=-1
        i+=d

    r=[[] for _ in range(k)]
    x=0
    for j in range(k):
        for i in range(len(t)):
            if p[i]==j:
                r[j].append(t[x]); x+=1

    res=""; idx=[0]*k
    for j in p:
        res+=r[j][idx[j]]
        idx[j]+=1
    return res

ch=input("1-E 2-D: ")
k=int(input("Key: "))

if ch=='1':
    t=open("Plaintext.txt").read()
    open("Cipher.txt","w").write(enc(t,k))
    print("Done")

else:
    t=open("Cipher.txt").read()
    open("Recover.txt","w").write(dec(t,k))
    print("Done")