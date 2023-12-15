# find out missing number in the list of 100 integers

#generate a list
my_list = []
for i in range(1,101):
    my_list.append(i)
my_list.pop(49)

def findMissingNumber(my_list, n):
    sum_of_first_100_int = n * (n+1)/2
    print(sum_of_first_100_int)
    sum_of_my_list = sum(my_list)
    missing_number = sum_of_first_100_int - sum_of_my_list
    return missing_number

print(findMissingNumber(my_list,100))