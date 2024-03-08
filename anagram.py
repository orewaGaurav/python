# Write a program to check if the given strings are anagram or not.
#A word or phrase formed by reordering the letters of another word or phrase, such as satin to stain.

#working of sorted

# a = ("listen")
# b = ("silent")
# x = sorted(a)
# y = sorted(b)
# print(x)
# print(y)
# print(x==y)



def anagram(s1,s2):
    if sorted(s1) == sorted(s2):
        print(f"{s1} and {s2} are anagrams")
    else:
        print(f"{s1} & {s2} are not anagrams")
s1 = input("enter the string 1: ")
s2 = input("enter the string 2: ")
anagram(s1,s2)