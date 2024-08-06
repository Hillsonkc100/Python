# Like in any other programming language python also has it's set of operators
# operators are the mathematical and logical symbols to perform operation in programming languages

# Operators in python are:-
# 1. Arithmetic operators
# 2. Logical operators
# 3. Relational operators
# 4. Assignment operators
# 5. membership operators
# 6. Identity operators

# 1. Arthmetic operators

# Addition(+)
a = 1 # a is a variable; = is a operator and 1 is a data of integer type
b = 2
print(a+b) # print() is a python built-in function to view the results in a console

# Subtraction (-)
a = 5
b = 3
print(a-b)

# Multiplication (*)
a = 3
b = 5
print(a*b)

# Division (/)
b = 8
a = 2
print(b/a) # '/' operators give the quotient of the division

# Exponent (**)
a = 2
print(a ** 3)

# floor division (//)
a = 10
b = 3
print(a // b)

# Modulus operators (%)
a = 10
b = 3
print(a % b) # % give the remainder of division

# 2. Logical operatoes
# and, or, not are the logical operators
# let's see the truth of each logical operators
# "and", "or", and "not" are the operators itself

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(not True) # False
print(not False) # True

# 3. Relational operators
# >, <, >=, <=, == are relational operators
# Result of relational operator is boolean (True / False)

print(5 > 3) # True
print(5 < 3) # False

print(5 >= 5) # True
print(5 <= 5) # True
print(4 != 2) # True
print(5 == 5) # True

# 4. Assignment operators
# =, +=, -=, *= are assignment operators

a = 1
a = a + 1
print(a) # 2

a += 1
print(a) # 3

a -= 1
print(a) # 2

# 5. Membership operators
# "in" and "not in" are the membership operators
# result of membership operation is in boolean. (True / False)
# checks whether an element is a member of iterable
# Iterable means sequence of data. List, tuplex, etc are the iterables in python

vowels = ["a", "e", "i", "o", "u"]
print("b" in vowels) # False
print("b" not in vowels) # True

print("e" in vowels) # True
print("a" not in vowels) # False

# 6. Identity operators
# 'is' and 'is not' are the identity operators
# They check whether two identities are the same objects or not
a = 1
b = 1
print(a is b) # True
print(a is not b) # False

a = []
b = []
print(a is b) # Both are not same object. False
print( a is not b) # True