number1=17
number2=30

def checkNumber(number1,number2):
    if number1>number2:
        return number1-number2
    else:
        return (number2-number1)*2
    
print(checkNumber(number1,number2))