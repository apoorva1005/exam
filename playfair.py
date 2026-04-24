import string
chars = string.ascii_uppercase + string.digits

def clean(t):
    return "".join(c for c in t.upper() if c in chars)

def matrix(key):
    k = clean(key)
    seen = []
    for c in k + chars:
        if c not in seen:
            seen.append(c)
    return [seen[i:i+6] for i in range(0,36,6)]

def pos(m, ch):
    for i in range(6):
        for j in range(6):
            if m[i][j] == ch:
                return i,j

def pairs(t):
    t = clean(t)
    p=[]; i=0
    while i<len(t):
        a=t[i]
        b=t[i+1] if i+1<len(t) else 'X'
        if a==b:
            p.append(a+'X'); i+=1
        else:
            p.append(a+b); i+=2
    return p

def enc(t,m):
    r=""
    for a,b in pairs(t):
        r1,c1=pos(m,a); r2,c2=pos(m,b)
        if r1==r2: r+=m[r1][(c1+1)%6]+m[r2][(c2+1)%6]
        elif c1==c2: r+=m[(r1+1)%6][c1]+m[(r2+1)%6][c2]
        else: r+=m[r1][c2]+m[r2][c1]
    return r

def dec(t,m):
    r=""
    for i in range(0,len(t),2):
        a,b=t[i],t[i+1]
        r1,c1=pos(m,a); r2,c2=pos(m,b)
        if r1==r2: r+=m[r1][(c1-1)%6]+m[r2][(c2-1)%6]
        elif c1==c2: r+=m[(r1-1)%6][c1]+m[(r2-1)%6][c2]
        else: r+=m[r1][c2]+m[r2][c1]
    return r

ch = input("1-E 2-D: ")
key = input("Key: ")
m = matrix(key)

if ch=='1':
    t=open("plaintext.txt").read()
    open("cipher.txt","w").write(enc(t,m))
    print("Done")

elif ch=='2':
    t=open("cipher.txt").read()
    open("recover.txt","w").write(dec(t,m))
    print("Done")
