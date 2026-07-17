# take student names ande marks as input and create a dictionary
def student_dic():
    student_info={}
    total_student=int(input("enter total student="))
    for x in range(total_student):
        student_name=input("enter name=")
        marks=int(input("enter marks="))
        student_info[student_name]=marks
    return(student_info)

result=student_dic()
print(result)