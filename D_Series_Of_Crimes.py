x,y = input().split()
x,y = int(x),int(y)
a,b = [],[]
for i in range(x):
    k = input()
    for j in range(y):
        if k[j] == "*":
            a.append(i)
            b.append(j)
for i in set(a):
    if a.count(i) == 1:
        print(i+1,end=" ")
        break
for i in set(b):
    if b.count(i) == 1:
        print(i+1)
        break