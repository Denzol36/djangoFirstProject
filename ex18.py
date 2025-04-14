from random import randint
list1=[]

def initList(list1,number):
    for i in range(number):
        list1.append(randint(0,9))
    
def countFour(list1):
    count = 0
    for i in list1:
        if i==4:
            count+=1
    return count

initList(list1,10)
print(list1)
print(countFour(list1))