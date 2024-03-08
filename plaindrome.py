# Write a program to check if the given number is palindrome or not
#eg 121,333,626

num = int(input("enter the no: "))
temp = num
reverse = 0
while temp > 0:
    remainder = (temp%10)
    reverse = (reverse*10)+remainder
    temp =temp//10
if num == reverse:
    print("plaindrome")
else:
    print("not a plaindrome")

