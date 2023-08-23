x = int(input())
for i in range(x):
    k = input()
    a,fg = 0,1
    for i in k:
        if i == "B" and a==0:
            fg = 0
            break
        elif i == "B" and a>0:
            a-=1
        else:
            a+=1
    if fg == 1 and k[-1] == "B":
        print("YES")
    else:
        print("NO")