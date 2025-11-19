import sys

if len(sys.argv) != 5:
    print("usage: student_validate.py <name> <reg_no> <email> <dept>")

    name = sys.argv[1]
    reg_no = sys.argv[2]
    email = sys.argv[3]
    dept = sys.argv[4]
else:
    name= "deeksha"
    reg_no=" 62"
    email= "deeksha@11"
    dept= "bca"

print("Registration successful")
print("Student Name:", name)
print("Student Register Number:", reg_no)
print("Email:", email)
print("Department:", dept)
