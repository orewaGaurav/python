# print this pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 


n = 5
p = 1
for i in range(n):
    for j in  range(i+1):
        print(p,end = " ")
    p+=1
    print()
    # finish


print("*"*8)

# print this pattern
# 0 
# 2 2 
# 4 4 4 
# 6 6 6 6 
# 8 8 8 8 8 

n = 5
p = 0
for i in range(n):
    for j in  range(i+1):
        print(p,end = " ")
    p+=2
    print()

print("!"*10)

# print this pattern
# 5 
# 4 4 
# 3 3 3 
# 2 2 2 2 
# 1 1 1 1 1 
# n = 5

p = 5
for i in range(n):
    for j in  range(i+1):
        print(p,end = " ")
    p-=1
    print()
