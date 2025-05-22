list1 = [x for x in range(1,11)]

for i in list1:
    for x in range(1,11):
        res = i*x
        print("{}*{}={}" .format(i,x,res))
    print()