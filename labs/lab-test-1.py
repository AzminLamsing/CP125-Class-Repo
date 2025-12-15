#Azmin programmer
#write a Python program that checks the grade for one student

def determine_grade(mark):
    if(mark >= 80):
        grade = "A"
    elif(mark >= 60 and mark <= 79):
        grade = "B"
    elif(mark >= 50 and mark <= 59):
        grade = "C"
    elif(mark >= 40 and mark <= 49):
        grade = "D"
    else:
        grade = "F"

    return grade

#user enter the input for student mark
mark = float(input("Enter the students mark : "))
result = determine_grade(mark)

#display output for student mark and grade
print(f"Mark : {mark:.1f} , Grade : {result}")
