# Write a program to print the following pattern.
# *
# * *
# * * *
# * * * *
# * * * * *


# def myfunc(n):
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             print("* ",end="")
#         print("\r")
# n = int(input("enter value of n: "))
# myfunc(n)


# for i in range(1,6):
#     print("* "*i)


# n=5
# print("*\n"*n)



for i in range(1,6):
    for j in range(1,i+1):
        print("*",end = " ")
    print("\r")