def fun(lst):
    sum = 0
    for i in lst:
        sum += i
    lst.append(sum)
    
nums = [1, 2, 5, 11]
fun(nums)
print(nums)