# function banao jo 3 numbers input lekar sabse bada number print kare

# def question3(no1):
#     largest=no1[0]
#     for x in no1:
#         if x > largest:
#             largest = x
#     return largest        

# store=[]
# for x in range(0,3):    
#     num1=int(input("enter no 1="))   
#     store.append(num1)
# print(store)    
# result=question3(store)
# print(result)

 
def question3(no1,no2,no3):
    if no1>=no2 and no1>=no3:
        return no1
    elif no2>=no1 and no2>=no3:
        return no2
    else:
        return no3

num1=int(input("enter no 1=")) 
num2=int(input("enter no 1=")) 
num3=int(input("enter no 1=")) 
result=question3(num1,num2,num3)
print(result)
    




