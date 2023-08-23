t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    m = a + c/2 + c%2
    n = b + c/2
    if m>n:
        print('First')
    else:
        print('Second')