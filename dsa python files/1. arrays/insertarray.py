from array import *
# first arg is typecode, i for int , d for decimals
array1 = array('i', [1,2,3,4,5])
#insert(index, value)
array1.insert(5, 10)
print(array1)

#insert at index1, but index1 is full, all the ele moves to right by 1
array1.insert(0,11)
print(array1)

# if the array is full, inserting new element ??
# create a larger array and move all the elements to it 

#disadv: time consuming operation(moving one by one to right)

# timecomplexity
#inserting an element in the beginning of the array-> o(n)
# inserting elements at the end of the array -> o(1)
# inserting elements when an array is full -> o(n)
# space complexity is contant since array size is predefined

#deleting an eleemnt from an array
# ex: [1,2,3,4,5]
# to remove 1 , move 2 to index 0 and so on
# so time compls =o(n) and space=o(1)