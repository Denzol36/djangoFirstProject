list1 = [1, 5, 8, 3]

def listChecker(list1,number):
    if number in list1:
        return True
    else:
        return False
    
if listChecker(list1,6):
    print("Yes")
else:
    print("NO")