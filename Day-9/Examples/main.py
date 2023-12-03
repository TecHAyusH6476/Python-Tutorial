from grade_calc import *

student1_score = [95, 94, 95, 95, 90]  # max_marks = 50
student2_score = [65, 60, 63, 67, 60]

a = calc_average(student1_score)
b = calc_average(student2_score)


std1_grade = calc_grade(a)
std2_grade = calc_grade(b)


std1_feedback = provide_feedback(a)
std2_feedback = provide_feedback(b)


print("Student 1 Average Score = ", a)
print("Student 1 Grade = ", std1_grade)
print(std1_feedback)
print()
print("Student 2 Average Score = ", b)
print("Student 2 Grade = ", std2_grade)
print(std2_feedback)
