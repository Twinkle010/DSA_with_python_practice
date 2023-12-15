# Permutation

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        list1.sort()
        list2.sort()
        if list1 == list2:
            return True
        else:
            return False

list1 = [1,2,3,4]
list2 = [2,3,4,1]
list3 = [12,34,56,7]

print(permutation(list1, list2))
print(permutation(list1, list3))
print(permutation(list2, list3))
print("***")
str1 = ['a', 'b', 'c']
str2 = ['b', 'c', 'a']
str3 = ['d','e','f']

print(permutation(str1, str2))
print(permutation(str1, str3))


