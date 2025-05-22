i=0
userNumber = 56
list1 = [1,1]

while i<userNumber:
    res = list1[-1]+list1[-2]
    list1.append(res)
    print(res)
    i+=1