# List comprehensions
list_comp = [x**2 for x in range(10)]
print(list_comp)

# Dictionary comprehensions
dict_comp = {x: x**2 for x in range(10)}
print(dict_comp)

#with if condition
list_comp_if_even = [x**2 for x in range(10) if x % 2 == 0]
print(list_comp_if_even)

#with if-else condition using even and odd numbers
list_comp_if_else_even_odd= [x**2 if x % 2 == 0 else x**3 for x in range(10)]
print(list_comp_if_else_even_odd)

#with nested for loop
matrix = [[1,2], [3,4], [5,6]]
flattened = [num for row in matrix for num in row]
print(flattened)

# Defining the generator function
def my_generator(max_limit):
    current = 1
    while current <= max_limit:
        yield current
        current += 1

# Using the generator in a for loop(implicitly calling the __next__() method)
print("Iterating with a for loop:")
for num in my_generator(3):
    print(num)

# Stepping through the generator using the next() function (explicitly calling the __next__() method)
print("\nStepping through manually:")
gen_instance = my_generator(2)


print(next(gen_instance))  # Output: 1
print(next(gen_instance))  # Output: 2