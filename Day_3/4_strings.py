# Strings are the immutable datatypes in python
# They are sequence of characters enclosed inside single, double or triple quotes

# Creating an empty string
a = str()
# str() is a built-in function to create string in python
print(a) # ""

a = ""
print(a) # empty string

a = ''
print(a) # empty string

a = """"""
print(a) # empty string

a = ''''''
print(a) # empty string

print(bool(a)) # False

# Creating  non-empty strings
a = "Hello"
b = 'Hello world'
c = """Hello world"""
d = '''Hello world'''

print(bool(d)) # True

# Accessing string elements
# Accessing string elements are similar to accessing list elements i.e. Indexing and Slicing

# Indexing
# Forward indexing starts from 0 and reverse from -1
data = "Hello World. I am learning python"

print(data[7]) # o
print(data[0]) # H
print(data[100]) # Error

print(data[-1]) # n
print(data[-10]) # I
print(data[-100]) # Error

# Slicing
data = "Hello World. I am learning python"

print(data[0:5]) # Hello
print(data[7:15]) # World
print(data[0:100]) # Hello World. I am learning python
print(data[:5]) # Hello
print(data[7:]) # World. I am learning python