n = int(input())
cd = list(map(int, input().split()))
sp,dp = 0,0
flag = 1
while(cd):
    if flag:
        sp += max(cd[0],cd[-1])
        cd.remove(max(cd[0],cd[-1]))
        flag = 0
        continue
    else:
        dp += max(cd[0],cd[-1])
        cd.remove(max(cd[0],cd[-1]))
        flag = 1
        continue
print(sp,dp)