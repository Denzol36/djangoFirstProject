num1 = 54; num2 = 24

def countGCD(num1,num2):
    while(num2):
        num1,num2 = num2, (num1%num2)
    return num1

def countLCM(num1,num2):
    if num1>num2:greatest=num1
    else:greatest=num2
    while True:
        if greatest%num1==0 and greatest%num2==0:
            lcm = greatest
            break
        greatest = greatest+1
    return lcm

