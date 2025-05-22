UserNumber = "9193992931"
reversNumber = ""
i=1
while i<len(UserNumber)+1:
    reversNumber = reversNumber+UserNumber[-i]
    i+=1

print(reversNumber)