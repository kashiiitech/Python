
# Calculate prime numbers between two ranges input from the user

# this will work for both positive and negative numbers 
# negative numbers can not be considered as prime numbers so it is neglected 

""" but if user input is negative than this program still work but this program skip the negative numbers and give positive primes as output"""





start = int(input("Enter your starting num : "))

end = int(input("Enter your ending num : "))

if start<0 and end < 0:

    print("Sorry ! Both are negative ")
    
elif start > end:

    list1 = []
    
    for i in range(start,end,-1):
    
        if i == 1 or i == 0 or i < 1:
        
            continue
            
        list1.append(i)
        
    for num in list1:
    
        for divisor in range(2,num):
        
            if num % divisor == 0:
            
                break
        else:
        
            print(num)
            
else:

    list1 = []
    
    for i in range(start,end+1):
    
        if i == 1 or i == 0 or i < 1:
        
            continue
            
        list1.append(i)
        
    for num in list1:
    
        for divisor in range(2,num):
        
            if num % divisor == 0:
            
                break
                
        else:
        
            print(num)
            

