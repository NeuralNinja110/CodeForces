tc = int(input())
for i in range(tc):
    tc1 = int(input())
    sl = map(int,input().split())
    if sum(sl)%2:
        print("NO")
    else:
        print("YES")