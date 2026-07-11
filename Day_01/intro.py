
message = "Hello World! "
message_1 = 'Hillson\'s World'  #(using \ helps the program to understand that it doesn't close in 's  )

print(message)
print(message_1)


message_2 = 'Hello World!'
print(len(message_2)) # This code provide the length of our code.
print(message_2[4])
print(message_2[0:9])
print(message_2.lower())
print(message_2.upper())
print(message_2.count("Hello"))
print(message_2.find("Hello"))
print(message_2.replace("Hello", "Universe"))


greeting = "Hello"
name = "Hillson"

message_3 = greeting + ',' + name + '. welcome!'
message_3 = "{}, {}. Welcome!".format(greeting, name )
message_3 = f"{greeting}, {name.upper()}. Welcome!"
print(message_3)



greeting = "Hello"
name = "Hillson"

print(dir(name))
print(help(str))
print(help(str.lower))