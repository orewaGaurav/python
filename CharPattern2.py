n = 26
p = 65 #ascii value for capital A
for i in range(n):
    for j in range(i,n):

        print(chr(p),end = " ")
    p+=1
    print("\r")
p = 65
for i in range(n):
    for j in range(i+1):

        print(chr(p),end = " ")
    p+=1
    print("\r")