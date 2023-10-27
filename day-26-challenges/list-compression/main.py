number = [1, 2, 3, 4, 5, 6, 7, 8]

# List comprehension
new_list = [letter for letter in "Prakash"]
print(new_list)
double_number = [i * 2 for i in range(1, 5)]
print(double_number)

names = ["Alex", "Beth", "Prakash", "Angela"]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
square_numbers = [i * i for i in numbers]
print(square_numbers)

nbs = [9, 0, 32, 8, 2, 8, 64, 29, 42, 99]
even_numbers = [i for i in nbs if i % 2 == 0]
print(even_numbers)
