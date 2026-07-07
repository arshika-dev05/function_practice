# Make a function that takes 2 numbers as input and gives the largest number.
def largest(number1,number2):
    if number1 > number2 :
        return number1
    else:
        return number2
    
num1=float(input("enter no 1="))
num2=float(input("enter no 2=")) 
result=largest(num1,num2)
print(result)   