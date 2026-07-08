# make a function that takes a string as input and reverse it.
user=input("enter word=")
stop=len(user)+1
reverse=user[-1:-stop:-1]
print("reverse=",reverse)