num1 = 2;num2 = 2

def Validator(num1,num2):
    if isinstance(num1,int) and isinstance(num2,int):return num1+num2
    else:return 0
    
print(Validator(num1,num2))