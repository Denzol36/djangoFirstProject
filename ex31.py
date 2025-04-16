num1=2;num2=3

def TwoSum(num1,num2):
    sum = num1+num2
    diff = num1-num2
    if num1==num2 or sum == 5 or diff == 5:
        return True
    else:
        return False
    
if TwoSum(num1,num2):
    print("Yes")
else:
    print("No")

