# update(), pop(), get(), keys(), values(), items(), clear()

# pop()
student = {"name": "jon", "age": 21, "address": "KTM"}
name = student.pop("name")
print(student)  # {'age': 21, 'address': 'KTM'}
print(name) # jon

# roll = student.pop("roll") # KeyError

# get()
student = {"name": "jon", "age": 21, "address": "KTM"}

roll = student.get("roll", 30)
print(roll) # 30

name = student.get("name", "jane")
print(name) # jon

# keys()
student = {"name": "jon", "age": 21, "address": "KTM"}

print(student.keys()) # dict_keys(["name", "age", "address"])
print(list(student.keys())) # ["name", "age", "address"]

# values()
print(student.values()) # dict_keys(["jon", 21, "KTM"])
print(list(student.values()))

# items()
print(student.items()) # dict_items([("name", "jon"), ("age", 21), ("address, "KTM")]}

# clear()
student.clear()
print(student) # {}  # empty dictionary
