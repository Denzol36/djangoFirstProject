import os.path as os

def fileExist(path):
    return os.isfile(str(path))
        
if fileExist('ex31.py'):
    print("Yes")
else:
    print("No")