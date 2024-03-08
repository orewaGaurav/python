# Write a program to check if the given number is Armstrong or not.
#e.g -- 153 = (1)^3 + (5)^3 + (3)^3
#1634 = [1]^4 + [6]^4 + [3]^4 + [4]^4

num = int(input("enter the no: "))
string = str(num)
length = len(string)
temp = num 
sum = 0
while temp > 0:
    reminder = temp % 10
    sum += reminder ** length
    temp //= 10
if num == sum :
    print(num,"is armstrong no.")
else:
    print(num,"is not a armstrong")


