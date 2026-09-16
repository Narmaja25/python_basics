#slicing
numbers = [10, 20 ,30 , 40, 50, 60]

print(numbers[1:4])
# Output: [20, 30, 40]

print(numbers[:3])
# Output: [10, 20, 30]  

print(numbers[3:])
# Output: [40, 50, 60]

print(numbers[-2:])
# Output: [50, 60]

print(numbers[::2])
# Output: [10, 30, 50]

print(numbers[::-1])
# Output: [60, 50, 40, 30, 20, 10]

# Formatting f-strings
name = "Narmaja"
age = 30
# f-strings approach (Recommended)
print(f"Hello, my name is {name} and I am {age} years old.")
# .format() approach
print("Hello, my name is {} and I am {} years old.".format(name, age))