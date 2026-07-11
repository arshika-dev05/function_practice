# function prectice
# print odd even both number from the list 
def odd_num(my_list):
    even_list=[]
    odd_list=[]
    for x in my_list:
        if x % 2==0:
            even_list.append(x)
        else:
            odd_list.append(x)  
          
    print("Even num=",even_list)
    print("Odd num=",odd_list)       


my_list=[1,2,3,4,5,6,7,8,9,10]
print(my_list)
odd_num(my_list)
   