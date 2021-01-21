
# Function that takes list as a parameter and calculates the square of every number in the list and return a list in which   # square of all numbers is available 



def square_member_list(lst):
    lst2 = []
    for i in lst:
        lst2.append(i**2)
    return lst2
