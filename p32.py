# (32) Armstrong Number Check
num = int(input("Enter a number: "))
sum = 0
temp = num

# the sum of its digits each raised to the power of 3 equals 153
# . Initial values: num = 153, sum = 0, 
# number of digits n =3

while temp > 0:
 digit = temp % 10
 sum += digit ** 3
 temp //= 10

#if number is equal equal to the sum of number then it is an armstrong number
if num == sum:
 print(num, "is an Armstrong number.")
else:
 print(num, "is not an Armstrong number.")