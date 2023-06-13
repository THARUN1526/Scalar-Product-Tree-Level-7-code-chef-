from sys import stdout as out
from sys import stdin as inp
mod=2**32

class parent:
    def __init__(self,curr,parval):
        self.curr=curr
        self.parval=parval

n,q=list(map(int,inp.readline().split()))
arr=list(map(int,inp.readline().split()))
d={}
k={}
# for i in range(1,n+1):
#     d[i]=[]
for _ in range(n-1):
    x,y=list(map(int,inp.readline().split()))
    if x not in k:
        k[x]=[]
    k[x].append(y)
    if y not in d:
        d[y]=[]
    d[y].append(x)
# print('d',d)
# print('k',k)

m=[0]*n
l=[parent(1,0)]
while len(l)>0:
    x=l.pop()
    a=x.curr
    b=x.parval
    c=(b+ (arr[a-1]**2)%mod)%mod
    m[a-1]=c
    if a in k:
        for item in k[a]:
            l.append(parent(item,c))
# print('m',m)

# print(m)

for _ in range(q):
    u,v=list(map(int,inp.readline().split()))
    ans=0
    z,y=[u],[v]
    while len(z)>0:
        x=z.pop()
        x1=y.pop()
        if x1==x:
            # print('break',ans)
            ans+=m[x-1]%mod
            break
        else:
            ans+=(arr[x1-1]*arr[x-1])%mod
            if x in d:
                for item in d[x]:
                    z.append(item)
            if x1 in d:
                for item in d[x1]:
                    y.append(item)

    out.write(str(ans%mod)+"\n")
                
