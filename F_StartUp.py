d = {'A','H','I','M','O','T','U','V','W','X','Y'}
x = input()
if x[::-1] == x:
    if set(x) <= set(d):
        print('YES')
    else:
        print('NO')
else:
    print('NO')