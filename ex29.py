num1=10;num2=50;num3=20

def threIntSum(num1,num2,num3):
    if num1==num2 or num2==num3 or num1==num3: return 0
    else: return num1+num2+num3
    
print(threIntSum(num1,num2,num3))