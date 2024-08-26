# Dictionary is a mutable datatype in python
# They are the key-value pairs enclosed withing curly braces

# Creating an empty dictionary
a = {}
b = dict()

# Creating an non-empty dictionary
student = {"name": "hillson", "age": 21, "address": "KTm"}
print(student)

student = dict(name="hillson", age=21, address="KTm")
print(student)

# Rule for dictinoary keys and values
# 1. Values of a Dictionary can be of any datatype
# 2. Keys of a Dictionary must be immutable datatype

d = {"": 12}
print(d) # valid dictionary

# d = {"message": "Hello", [1,2]: 12} # Invalid dictionary
d = {"message": "Hello", (1,2): 12} # valid dictionary
# d = {"message": "Hello", {1,[2,3]}: 12} # Invalid dictionary

e = {1: "Hello", 2: "world"} # valid

# Accesssing dictionary values
student = {"name": "hillson", "age": 21, "address": "KTm"}
a1 = [1,2,3]
print(a1[1]) # 2
print(a[10]) # IndexError

print(student["address"]) # "KTm"
print(student.get("name")) # "hillson"

d = {"": 12}
print(d[""]) # 12

d = {"message": "hillson", (1,2): 12}
print(d[(1,2)]) # 12
e = {1: "hello", 2: "world"}
print(e[2]) # world

student = {"name": "hillson", "age": 21, "address": "KTm"}
print(student["rool"]) # KeyError

# .get() method
name = student.get("name")
print(name) # hillson

roll = student.get("roll")
print(roll) # None


# Updating dictionary elements
student = {"name": "hillson", "age": 21, "address": "KTM"}
student["roll"] = 22

print(student)  # {'name': 'hillson', 'age': 21, 'address': 'KTM", "roll": 22}

student["name"] = "don"
print(student)  # {'name': 'don', 'age': 21, 'address': "KTM", "roll": 22}

# Updating method
student = {"name": "jon", "age": 22}

student.update({"roll": 23, "address": "Jhapa"})
print(student)  # {'name': 'jon', 'age': 22, "roll":23, "address": "jhapa"}

student.update(email="hillsonkc100@gmail.com", classroom= 2)
print(student) # {'name': 'jon', 'age': 22, "roll":23, "address": "jhapa", "email": "hillsonkc100@gmail.com", "classroom": 2}

