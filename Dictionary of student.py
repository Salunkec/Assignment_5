student_name = {'Alice':85,'mark':90,'bob':78}

name = input("Enter student's name: ")

if name in student_name:
    print(f"{name}'s marks: {student_name[name]}")
else:
    print("Student not found")