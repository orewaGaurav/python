# n = int(input("Enter n: "))
# for i in range(1,n+1):
#     print(i,end="")

from __future__ import division
a = int(input())
b = int(input())
print(a//b)
print(a%b)
print(divmod(a,b))

# >>> print divmod(177,10)
# (17, 7)
# Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.