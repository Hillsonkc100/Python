# True and False are the boolean data in python
# True and False are also keywords
# Boolean are the immutable datatypes

# Operations that give boolean data
# 1. Logical operations
# 2. Relational operations
# 3. Membership operations
# 4. Identity operations

# Boolean type are the subclass of integer type in python
# True represents 1 and False represents 0
a = True + True
print(a)  # Output: 2

b = True + False
print(b) # 1

print(70*False) # 0

# Concept of Truthy and Falsy in python

# Truthy
# All the non-empty data(list, tuple, set etc) including non-zero numbers and True itself are the Truthy data
a = 12
b = -1
c = 12.2
d = [1, 2, 3]
e = {1, 2, 3}
f = (3, 4, 5)
g = {'name':'jon'}
h = True
i = "Hello"

# bool() is a python built-in function to check whether a data is truthy or falsy
print(bool(a)) # True
print(bool(b)) # True
print(bool(c)) # True
print(bool(d)) # True
print(bool(e)) # True
print(bool(f)) # True
print(bool(g)) # True
print(bool(h)) # True
print(bool(i)) # True

# Falsy
# All the empty data (list, tuple, set etc) including zero, None and False itself are the falsy data

a = 0
b = 0.0
c = []
d = ()
e = set()
f = {}
g = ""
h = None
i = False

print(bool(a)) # False
print(bool(b)) # False
print(bool(c)) # False
print(bool(d)) # False
print(bool(e)) # False
print(bool(f)) # False
print(bool(g)) # False
print(bool(h)) # False
print(bool(i)) # False

a = 5
if a:
    print("a is non zero")
a = []
if a:
    print("The list is non-empty")
else:
    print("The list is empty")


