import os

def findfile(fname,path):
    
    for f in os.listdir(path):
        absp = os.path.join(path,f)

        if f[:1] == ".":
            continue
        elif os.path.isfile(absp):
            if f == fname:
                return absp
        else:
            return findfile(fname,absp)


p = os.path.abspath(".")
print(findfile("test.txt",p))
