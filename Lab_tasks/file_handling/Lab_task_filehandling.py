directory = "Desktop"
name = "names.txt"
import os
file = os.path.join(directory,name)

## here the file names.txt is created at the Desktop 

with open(file,"w") as f:  # here file is opened as f
    f.write("Hans\nAnna\nVladimir\nMichael\nEd\nSusan\nJanice\nJoy\nkashii\ntariq") # here these names are write into the file named names.txt
names = []      # here this will take names from file one by one
with open(file) as f: 
    for line in f:    # here this list takes name from file and append one by one to names list
        names.append(line.strip().split("\n"))
        
length = []    
for line in names: # this means take a line from names becz names is nested list
    for name in line: # in this line it will take name from the list of names in line
        length.append(len(name))   # and the length of names is now append to the length named list


for name in names:
    for nam in name:
        print(nam[0:4])  # here this will print the first four character of each name from the file
ss = length.index(min(length))   # and in this line first it will take index of minimum value from list and assign it into the ss
print("the shortest name in the names.txt is :",names[ss],"and its length is",len(names[ss][0])) # here in this line first it will print the shortest name from the list ad also the length of that name will be printed
                
i = 0
for summ in length:     # here this loop will take the length of one name and add to i and this process will continue till the sum of all named will complete
    i = i + summ 
print("the sum of names in the names.txt is :",i)   # here in i there is sum of all lengths of elements
average = i / len(names)   # in this line it will calculate the average becouse first in i there is the sum of all the names of lengths in the list and divided by the num of names in the list this average 
print("the average of names is :",average) # and in this line this will print the value of average

name = "name_sub.txt"    # here the new file name_sub.txt will be created
import os
fil = os.path.join(directory,name)    


with open(fil,"w") as k:   # here  new file will open as a write mode
    for name in names:     # here name will take one list and in this list there is simply a name
        out_line = ",".join(name)   # and in this line the name will joined at coomaa and assigned to thr variable out_line
        k.write(out_line+" Programing Fundamentals lab ,programing fundamental , English Composition,Calculas-1"+"\n")
        # and in above line the name will be write to the new file and also with the name of subject 
