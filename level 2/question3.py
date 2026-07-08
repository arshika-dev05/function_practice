# create a function that takes number as input and find its factorial. 
def factorial(num):
    result=1
    for x in range(1,num+1):
        result*=x 
        # (result =result * x) means, (result= 1*1 =1)--result=1, then (result= 1*2 =2)--result=2 .....
    return result  


number=int(input("enter number="))
store=factorial(number)
print(f"{number}! = {store}") 
    