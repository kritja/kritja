# List comprehension
print('List comprehension')
squares = [x**2 for x in range(10)]
print(squares)

# Dictionary comprehension
print('Dictionary comprehension')
square_dict = {x: x**2 for x in range(5)}
print(square_dict)


# Set comprehension
print('comprehension')
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)
