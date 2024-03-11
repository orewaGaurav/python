#writ the program to print this pattern
          # 
        # # 
      # # # 
    # # # # 
  # # # # # 

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end = " ")
    for j in range(i+1):
        print("#",end = " ")
    print()
print("---------------")
#program used 
#  * 
# * * 
# * * * 
# * * * * 
# * * * * * 
n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end = " ")
    print()
#program used
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
for i in range(n):
    for j in range(i,n):
        print("*",end = " ")
    print( )