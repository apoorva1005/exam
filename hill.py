def clean(t): return "".join(c for c in t.upper() if c.isalpha())

def mat(key):
    k=clean(key)
    return [[ord(k[0])-65,ord(k[1])-65,ord(k[2])-65],
            [ord(k[3])-65,ord(k[4])-65,ord(k[5])-65],
            [ord(k[6])-65,ord(k[7])-65,ord(k[8])-65]]

def mul(m,v):
    return [(m[i][0]*v[0]+m[i][1]*v[1]+m[i][2]*v[2])%26 for i in range(3)]

def det(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
          - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
          + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))%26

def inv_mod(a):
    for i in range(26):
        if (a*i)%26==1: return i

def inv(m):
    d=det(m); invd=inv_mod(d)
    if invd is None: return None

    adj=[
    [(m[1][1]*m[2][2]-m[1][2]*m[2][1]),
     -(m[0][1]*m[2][2]-m[0][2]*m[2][1]),
     (m[0][1]*m[1][2]-m[0][2]*m[1][1])],

    [-(m[1][0]*m[2][2]-m[1][2]*m[2][0]),
     (m[0][0]*m[2][2]-m[0][2]*m[2][0]),
     -(m[0][0]*m[1][2]-m[0][2]*m[1][0])],

    [(m[1][0]*m[2][1]-m[1][1]*m[2][0]),
     -(m[0][0]*m[2][1]-m[0][1]*m[2][0]),
     (m[0][0]*m[1][1]-m[0][1]*m[1][0])]
    ]

    return [[(adj[i][j]*invd)%26 for j in range(3)] for i in range(3)]

def process(m, inp, out):
    t=clean(open(inp).read())
    while len(t)%3: t+='X'
    r=""
    for i in range(0,len(t),3):
        v=[ord(x)-65 for x in t[i:i+3]]
        x=mul(m,v)
        r+="".join(chr(i+65) for i in x)
    open(out,"w").write(r)
    print("Done")

ch=input("1-E 2-D: ")
k=input("9-letter key: ")
m=mat(k)

if ch=='1':
    process(m,"input.txt","enc.txt")
else:
    im=inv(m)
    if im: process(im,"enc.txt","dec.txt")
    else: print("Invalid key")