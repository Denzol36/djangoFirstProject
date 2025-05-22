UserPIN = "228"

i=0

while i<3:
    InputPIN = input("Enter PIN:")
    if InputPIN.lower() == UserPIN.lower():
        print("Yes")
        break
    i+=1