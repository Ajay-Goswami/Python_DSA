# Input : 3456
# Output : 6 5 4 3


n = 3456

# Using for loop
for i in range(len(str(n))):
    print(n%10)
    n=n//10

# Using while loop
# num = n
# while num>0:
#     print(num%10)
#     num = num//10

