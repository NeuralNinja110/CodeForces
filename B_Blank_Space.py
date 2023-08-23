for i in range(int(input())):
    x = input()
    d = input().split(" ")
    e = "".join([str(j) for j in d])
    e = e.split("1")
    print(len(max(e)))