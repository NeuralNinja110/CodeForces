tc = int(input())
for i in range(tc):
    r,b = 0,0
    n = int(input())
    red = input().strip()
    blue = input().strip()
    for j in range(n):
        if red[j] > blue[j]:
            r += 1
        elif red[j] < blue[j]:
            b += 1
    if r > b:
        print("RED")
    elif r < b:
        print("BLUE")
    else:
        print("EQUAL")