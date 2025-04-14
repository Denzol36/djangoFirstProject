line = "Hello"
temp = 3

def copy(line,temp):
    if len(line)<=2:
        return line*temp
    else:
        return line[:2]*temp

print(copy(line,temp))