#  function that takes a list as a parameter and calculates the number of prime numbers present in
#  the list. This function also must find the index of each prime number





def prime_count(lst):
    counter = 0        # This counter variable is used for to count the number of prime from a given list
    lst_index_prime = []     # this empty list is for to store the indexes of prime numbers .
    for i in lst:          #   this loop will take each element in each iteration in the list
        for j in range(2,i):  #  this loop is for to check whether a number is prime or not .
            if i%j == 0:      #   if this condition become True than the number is not a prime
                break      
        else:               # if the above condition become False than this condition will execute
            lst_index_prime.append(str(lst.index(i)))   # take index of prime number from list change type in string and 									append the lst_index_prime
            counter += 1         # this will add one in the counter in every iteration which is the condition of prime number
    print("number of primes ",counter,"and their indexes are",",".join(lst_index_prime))
    
    # in this line first it will print the counter that how many primes are there in the list and then their indexes (but it will join the index on commas for clear out put .
