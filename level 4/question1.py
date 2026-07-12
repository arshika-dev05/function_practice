# create a function and take a string as input and check if a string is a palindrome.
def reverse(copy):
        reverse=copy[::-1]
        return reverse

def palindrome(change,user):
    if user==reverse(change):
        print("palindrome")
    else:
        print("not palindrome")    


user=input("enter word=")
copy=user
palindrome(copy,user)

 
