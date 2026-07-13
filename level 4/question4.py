# convert a string to lowercase.
def lowercase(text): 
    word_store=" "
    for x in text:
        if x >='A' and x <='Z':
            char_into_no=ord(x) - 32
            no_into_char=chr(char_into_no)
            word_store += no_into_char
    return word_store        


meassage=input("enter message")   
result=lowercase(meassage)
print(f"{meassage} conver in uppercase, ok \n{result}") 