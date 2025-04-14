number = int(input("Enter the number:"))

def Check(num):
    if num%2==0:
        return True
    else:
        return False
    
if(Check(number)):
    print("Even")
else:
    print("Odd")