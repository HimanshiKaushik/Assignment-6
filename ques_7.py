class student:
    pass

class marks:
    pass

student_1 = student()
student_2 = student()
marks_1 = marks()
marks_2 = marks()

print(isinstance(student_1, student))
print(isinstance(student_2, student))
print(isinstance(marks_1, marks))
print(isinstance(marks_2, marks))

print(issubclass(student, object))
print(issubclass(student, object))