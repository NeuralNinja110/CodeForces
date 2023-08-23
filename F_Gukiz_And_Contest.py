n = int(input())
t = list(map(int,input().split()))
q = sorted(t,reverse=True)
d = dict()
res = ""
for i in set(t):
    d[i] = q.index(i)
    
for i in t:
    res += str(int(d[i]) + 1)+" "
res.rstrip()
print(res)