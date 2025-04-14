list1=["a","e","i","o","u"]
letter="C"
letter.lower


def check(word,list):
    if word in list:
        return True
    else:
        return False
    
if(check(letter,list1)):
    print("Yes")
else:
    print("No")