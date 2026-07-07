# Make a function that takes a number as input and prints whether it's even or odd
def question4(number):
    if number % 2==0:
        return("even")
    else:
        return("odd")  


num=int(input("enter no="))
result=question4(num)
print(result)  
