
# This function will take the input from the user and then tell us either it is a armstrong number or not 


               #Armstrong Numbers
               
               #A number is called Armstrong number if it is equal to the sum of the cubes of its own digitss



x = int(input("Enter any Num : "))
def armstrong_num(x):
    y = str(x)
    summ = 0
    lst = []
    for i in y:
        i = int(i)
        lst.append(i**3)
    for i in lst:
        summ += i
    if (summ==x):
        print("It is an Armstrong Num :",x)
    elif (summ!=x):
        print("It is not an Armstrong Num :",x)
armstrong_num(x)
