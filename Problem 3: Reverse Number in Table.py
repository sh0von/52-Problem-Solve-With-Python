lst = [i for i in zip(*[iter(range(100,-1,-1))]*10)] ##print all number in list
for i in lst:
    for j in i:
        print(j, end=" ")
    print()
