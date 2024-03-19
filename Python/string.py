#indexing
greet = 'hello'
print(greet[1]) #e
print(greet[-1]) #o
#slicing
print(greet[1:4]) #ell

#python strings are immutable but we can assign the variable name to a new string
message = 'hola amigos'
message = 'hello friends'
print(message) #hello friends

#multiline string
message = """
never gonna give you up
never gonna let you down
"""
print(message)

#string operations
#compare two strings
str1 = 'hello world'
str2 = 'I love python'
str3 = 'Hello World'
print(str1 == str2)
print(str1 == str3)

#joining 2 or more strings
greet = 'Hello,'
name = 'Michael'
result = greet + name
print(result)

#iterating through a string using for loop
greet = 'Hello'
for letter in greet:
    print(letter)

#upper and lower case
name = 'kiRstEn'
cap = name.upper()
print(cap)
low = name.lower()
print(low)

#escape sequence - used to escape some of the characters present inside a string
example = "He said, \"What's that?\"" #the compiler would return an error without '\'
print(example)

#f-strings - makes it easier to  print values and variables
name = 'Kirsten'
country = 'Kenya'
print(f'{name} is from {country}')