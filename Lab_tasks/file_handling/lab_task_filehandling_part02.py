directory = "Desktop"
name = "names.txt"
import os
file = os.path.join(directory,name)  # here first the file names.txt will be created that takes 10 names
with open(file,"w") as f:
    f.write("Hans\nAnna\nVladimir\nMichael\nEd\nSusan\nJanice\nJoy\nkashii\ntariq")
names = []
with open(file) as f:
    for line in f:
        names.append(line.strip().split("\n"))  # and here the 10 names will be assifned one by one to a list named names
        
        
def name_num(x):    # and when we call this function this will print those names whose length will be given in the parameter 
    kash = []
    for lis in names:
        for name in lis:
            kash.append(name)
    for i in kash:
        if len(i) == x:
            print(i)
            
            
            
