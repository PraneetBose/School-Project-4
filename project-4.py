# Python3 Program to
# accept marks for 5 subjects and calculate percentage.

# finding the Total marks of examination
marks = int(input("Full marks of the Examination : "))
num = marks * 5
# collecting and storing the data of marks per subject
ENGLISH = float(input("Enter the marks of english: "))
MATHS = float(input("Enter the marks of math: "))
SOCIALSCIENCE = float(input("Enter the marks of Social Science: "))
SCIENCE = float(input("Enter the marks of Science: "))
HINDI = float(input("Enter the marks of Hindi: "))
# finding the total marks
print("Total marks scored =", ENGLISH + MATHS + SOCIALSCIENCE + SCIENCE + HINDI)
# storing the total marks in the variable 'total'
total = ENGLISH + MATHS + SOCIALSCIENCE + SCIENCE + HINDI
# calulating the percentage of marks
percentage = total / num * 100
print("The percentage of all subjects is  = ", percentage)
