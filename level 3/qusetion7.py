# find smallest number in the list, but without using min().
def smallest_num(my_lsit):
    smallest=my_lsit[0]
    for i in my_list:
        if i < smallest:
            smallest = i
    return smallest

my_list=[25,65,34,78,21,20,45]
result=smallest_num(my_list)
print(f"{my_list}\nSmallest num = {result}")


