#Write a program to find if the given number is prime or not

num = int(input("Enter the No: "))

if num ==1:
    print(num,"is not a prime no.")
elif num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")


# num  = int(input("Enter the no: "))

# if num == 1:
#     print(num,"is not a prime no.")
# elif num > 1:
#     for i in range(2,num):
       

#        if num % i == 0:

#         print(num,"is not a prime no.")
#         break
#     else:
#        print(num,"is a prime no.")
# else:
#    print(num,"not a prime no.")