q = int(input())
while(q):
    q-=1
    t = input()
    x = input()
    y = ""
    z = ""
    for i in x:
        y+=str(int(i)+1)
    y = list(y)
    for i in range(len(y)-1):
        if(y[i]==y[i+1]):
            y[i+1] = str(int(y[i+1])-1)
    x = int("".join(y)) - int(x)
    print(x)