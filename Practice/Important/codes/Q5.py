#function that takes two lists and returns True if they have at least one common member.



def common_data(list1, list2):
    result = False
    for x in list1:
         for y in list2:
                 if x == y:
                    result = True
    return result
