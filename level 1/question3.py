#  create a function that takes three number as input and print the largest number.
 
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
    




