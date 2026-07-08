# make a function that takes a string as input and reverse it.
def reverse_string(text):   
    stop=len(user)+1
    reverse=text[-1:-stop:-1]
    print("reverse=",reverse)

user=input("enter word=")
reverse_string(user)