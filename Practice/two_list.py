
# Function that takes two lists as a parameter and return a new list in which odd elements from list1 and even elements from list2 .

def two_list(lst1,lst2):
    new_list = []
    for i in range(0,len(lst1)):
        if lst1[i] % 2 != 0:
            new_list.append(lst1[i])
    for j in range(0,len(lst2)):
        if lst2[j] % 2 == 0:
            new_list.append(lst2[j])
    return new_list
