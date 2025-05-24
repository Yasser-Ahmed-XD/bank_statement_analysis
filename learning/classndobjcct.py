# class Student:
#     name = "yasser"
#     age = 18

# s1=Student ()
# print(s1.age)

# class factory:
#     color = "red"
#     body = "sports"
#     gear = 7

# fac = factory()
# print(fac.gear)

# b = 0
# a = 0
# if b==0:
#     if a==1:
#         print("good")
#     else:
#         print("bad")

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}
for keys in student_scores:
    score =student_scores[keys]
    if score>=91:
        student_grades[keys]="Outstanding"
    if 81<score<=90:
        student_grades[keys]="Exceeds"
    if 71<=score<=80:
        student_grades[keys]="Acceptable"
    if score<=70:
        student_grades[keys]="Fail"

print(student_grades)