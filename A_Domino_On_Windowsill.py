tc = int(input())
for i in range(tc):
    n, k1, k2 = map(int, input().split())
    w, b = map(int, input().split())
    wc = k1 + k2
    bc = 2 * n - wc
    if (w <= (wc // 2) and b <= (bc // 2)):
        print("YES")
    else:
        print("NO")