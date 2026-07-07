# Make a function that takes a number as input and tells whether it's positive, negative, or zero.
def question8(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

# input
num=float(input("enter number="))
question8(num)