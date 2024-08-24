# capotalize()
# title()
# upper()
# lower()
# split()
# join()

# title()
a = "hello world"
result = a.title()
print(result) # Hello World

# capitalize()
a = "hello world"
result = a.capitalize()
print(result) # HELLO WORLD

# upper()
result = a.upper()
print(result) # HELLO WORLD

# lower()
a = "Hello World"
result = a.lower()
print(result) # hello world

# split()
a = "hello world"
result = a.split()
print(result) # ['hello', 'world']

result = a.split("o")
print(result) # ['hell', ' w', 'rld']

# join()
data = ["python", "is", "high", "level", "languages"]
result = " ".join(data)
# result = data.join("") # This is wrong because list doesn't join method
print(result) # python is high level languages

result = " + ".join(data)
print(result)

d = "Hello world"
print(d[::-1])

data = [1,2,3,4]

data[2] = 9
print(data) # [1,2,9,4] # Here list is mutable so we can replace one of the element

data = 'hello'
data[2] = "L" # We are not allow to replace a string element as strings is immutable
print(data) # hLllo
