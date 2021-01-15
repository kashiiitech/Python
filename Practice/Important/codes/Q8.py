#  Write a function that takes a list as a parameter and reverses the list without using the built-in reverse
#  function.




def reverse_list(x):
    k = []
    for i in range(len(x)-1,-1,-1):
        k.append(x[i])
    x.clear()
    for j in k:
        x.append(j)
    return x
    
