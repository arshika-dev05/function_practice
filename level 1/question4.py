# function banao jo number input lekar Even ya Odd number print kare
def question4(number):
    if number % 2==0:
        return("even")
    else:
        return("odd")  


num=int(input("enter no="))
result=question4(num)
print(result)  
