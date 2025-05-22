from random import randint

randomNumber = randint(1,10)
userNumber = None
while userNumber!=randomNumber:
    userNumber = int(input("Enter number: "))
    if userNumber>randomNumber:
        print("Your number bigger than guess")
    elif userNumber<randomNumber:
        print("Your number smoler than guess")
    else:
        print("You win!!!!!!")