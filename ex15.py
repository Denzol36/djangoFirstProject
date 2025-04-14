line = "Ishello"

def LineCheck(line):
    pref = line[:2]
    if(pref=="is" or pref=="Is"):
        return line
    else:
        res = "Is"+line
        return res
    
print(LineCheck(line))