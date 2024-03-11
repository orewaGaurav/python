#write a program to print this pattern
# * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 
#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 
# n = int(input("Enter n: "))
n = int(input("Enter n: "))
for i in range(n):
    for j in range(i+1):
        print(" ",end =" ")
    for j in range(i,n):
        print("*",end = " ")
    for j in range(i,n-1):
        print("*",end = " ")
    print("\r")

for i in range(n):
    for j in range(i,n):
        print(" ",end = " ")
    for j in range(i+1):
        print("*",end = " ")
    for j in range(i):
        print("*",end = " ")
    print()