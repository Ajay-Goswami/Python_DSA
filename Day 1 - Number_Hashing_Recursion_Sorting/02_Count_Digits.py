# input : 4567
# output : 4


n= 4567
ncount = 0
while n> 0:
    n = n //10
    ncount += 1

print("ncount : ",ncount)

# Using len function
x = 456759
print("xcount : ",len(str(x)))

# Using for loop
j = 89876
jcount = 0
for i in str(j):
    jcount += 1
print("jcount : ",jcount)