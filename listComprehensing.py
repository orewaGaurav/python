numbers = [1, 2, 3, 4, 5]
squares = [i**2 for i in numbers]
print(squares)  # [1, 4, 9, 16, 25]


numbers = [1, 2, 3, 4, 5]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16]

