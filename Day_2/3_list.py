# List are the mutable datatypes in python
# They are the sequence of data enclosed within big brackets
# Unlike array, The elements in list can be of heterogeneous datatype

# Creating an empty list
a = list() # empty list
print(a)
a = []
print(a) # []

a = [1,2,3]
print(a)
b = ["hello" , "world"]
print(b)
c = [1,2, "hello", [4,5]] # List of mixed datatypes
print(c)

# Accessing the list elements
# List elements can be accessed using indexing and slicing

# Indexing
# Forward(positive) indexing
vowels = ['a','e','i','o','u']
print(vowels[3]) # "o"
print(vowels[0]) # 'a'
print(vowels[4]) # 'u'
#print(vowels[10]) # Indexerror. list index out of range

# Negative(backward) indexing
print(vowels[-1]) # 'u'
print(vowels[4] == vowels[-1]) # True
print(vowels[-3]) # 'i'
# print(vowels[-10]) # Indexerror. list index out of range

# Slicing
data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(data[2:7]) # ['c', 'd', 'e', 'f', 'g', 'h']
print(data[:4]) # ['a', 'b', 'c', 'd']
print(data[5:]) # ['f', 'g', 'h', 'i', 'j']
print(data[1:9:2]) # [ 'b', 'd', 'f', 'h']
print(data[9:1]) # []
print(data[9:-1]) # []

print(data[-8:-2]) # ['c', 'd', 'e', 'f', 'g', 'h']
print(data[:-3]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(data[-4:]) # ['g', 'h', 'i', 'j']
print(data[-3:-9]) # []

data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(data[2:8]) # ['c', 'd', 'e', 'f', 'g', 'h', 'i']
print(data[9:3]) # []
print(data[7:]) # ['h', 'i', 'j']
print(data[:4]) # ['a', 'b', 'c', 'd',]
print(data[-5:-9]) # []
print(data[-4:-8]) # []
print(data[3:-1]) # ['d', 'e', 'f', 'g', 'h', 'i']


