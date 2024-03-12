# print this pattern
#          * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 
#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 
# take n = 5

n = int(input("Enter n: "))
for i in range(n):
    for j in range(i,n):
        print(" ",end =" ")
    for j in range(i+1):
        print("*",end = " ")
    for j in range(i):
        print("*",end = " ")
    print("\r")

for i in range(n):
    for j in range(i+1):
        print(" ",end = " ")
    for j in range(i,n):
        print("*",end = " ")
    for j in range(i,n-1):
        print("*",end = ' ')
    print()