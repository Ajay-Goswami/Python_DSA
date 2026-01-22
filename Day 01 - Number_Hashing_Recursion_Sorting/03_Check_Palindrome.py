# input : 34543
# output : Palindrome

#input : 1234
#output : Not Palindrome

#input : Hello
#output : Not Palindrome

#input : madam
#output : Palindrome

# if input is number
n = int(input("Enter a number : "))
num = n
rev = 0
while n>0:
    rem = n % 10 
    rev = rev * 10 + rem
    n = n // 10

if num == rev: 
    print("Palindrome")
else:
    print("Not Palindrome")

# if input is string
str = input("Enter a string : ")
if str == str[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")