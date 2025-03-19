my_list = []
# append 
my_list.extend([10, 20, 30, 40])
my_list[1] = 15
# extend 
my_list.extend([50, 60, 70])
# remove last index
my_list.pop(-1)
# sorting in ascending order
my_list.sort()
# find the value 30 and print
if 30 in my_list:
    print(30)