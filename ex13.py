number = 102

def numberCheck(number):
    if number>100 and number < 1000:
        return True
    else:
        return False
    
if(numberCheck(number)):
    print("Yes")
else:
    print("No")