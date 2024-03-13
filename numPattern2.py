# print this 
# 1 
# 2 2 
# 1 1 1 
# 2 2 2 2 
# 1 1 1 1 1 

n = 5
p =1
for i in range(n):
    for j in range(i+1):
        if i%2 ==0:
           print(p,end = " ")
        else:
            print("2",end = ' ')
    print()   

