# search for character
import random
list =["arshika","ravina","count","ravi"]
randoms=random.choice(list)
print(randoms)
guess=input("guess character=")
for x in randoms:
    if guess == x:
        print("true")
    else :
        print("False")    

   