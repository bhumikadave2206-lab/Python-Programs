# (25) Return Multiple Values from Function
def student_details():
 name = "Bhumika"
 age = 19
 course = "BCA"
 return name, age, course
# Receiving multiple values
n, a, c = student_details()
print("Your Name Is:", n)
print("Your Age Is:", a)
print("Your Course Is:", c)