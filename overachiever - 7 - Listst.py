def overachiever(complete_list):
    greatest = 0
    student_name = ""
    for student in complete_list:
        if student[1] > greatest:
            greatest = student[1]
            student_name = student[0]
    return print(student_name)


overachiever([["Maria", 91.5],["George", 47.3],['Aquan', 94],["Lucia", 89]])


    
    