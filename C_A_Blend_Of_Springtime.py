k = input()
for i in ["ABC","CBA","BAC","CAB","ACB","BCA"]:
    if i in k:
        print("Yes")
        break
else:
    print("No")