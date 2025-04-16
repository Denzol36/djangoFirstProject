number1 = 12
number2 = 17

def gcd(num1,num2):
    gcd = 1
    if num1%num2==0: return num2
    for i in range(int(num2/2),0,-1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
            break
    return gcd

print(gcd(number1,number2))