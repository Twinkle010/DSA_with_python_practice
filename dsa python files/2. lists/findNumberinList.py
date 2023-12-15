#generate a list
my_list = []
for i in range(1,101):
    my_list.append(i)

target = 116
def findNumberinList(my_list, target):
    return True if target in my_list else False

print(findNumberinList(my_list, target))

# do in an algorithmic way
# generate array using numpy module and loop over it i.e linear search to find target