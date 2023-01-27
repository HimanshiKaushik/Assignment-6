def student_data(student_id, student_name=None, student_class=None):
    print("student ID:", student_id)
    if student_name is not None and student_class is not None:
        print("Student Name:", student_name)
        print("Student Class:", student_class)

a = input("enter data=")
print(student_data(a))