# Armstrong Number - An Armstrong Number is a number that is equal to the sum of its own digits, where each digit is raised to the power of the total number of digits in the number.

# input : 153
# output : Armstrong Number
# reason : 153 = 1*1*1 + 5*5*5 + 3*3*3

# input : 1234
# output : Not Armstrong Number
# reason : 1234 = 1*1*1*1 + 2*2*2*2 + 3*3*3*3 + 4*4*4*4


n= input("Enter a number : ")
sum = 0 

for i in n:
    sum = sum + int(i)**len(n)

if sum == int(n):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")