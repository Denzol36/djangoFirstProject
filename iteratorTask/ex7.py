list1 = [x for x in range(1,6)]

for i in list1:
    res = 1
    for x in range(1,i+1):
        res*=x
    print(res)