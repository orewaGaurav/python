# def max(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c :
#         return b
#     elif c>a and c>b:
#         return c
#     else:
#         print(f"{a},{b} & {c} are equal")

# a = int(input("enter a: "))
# b = int(input("enter b: "))
# c = int(input("enter c: "))

# print("max of a,b,c:",max(a,b,c))



def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c :
        return b
    elif c>a and c>b:
        return c
    else:
        print(f"{a},{b} & {c} are equal")
x = 2
while x != 0:

    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = int(input("enter c: "))

    print("max of a,b,c:",max(a,b,c))
