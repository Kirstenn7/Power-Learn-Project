#numeric data types
num1 = 5
print(num1, 'is of type', type(num1))

num2 = 2.5
print(num2, 'is of type', type(num2))

num3 = 1+2j
print(num3, 'is of type', type(num3))

#list data type
languages = ['Java', 'Python', 'R']
#to access items from a list, we use the index number
print(languages[1])

#tuple data type
product = ('Ps5', 499.99)
print(product[0])

#string data type
name = 'Kirsten Njeri'
print(name)

#set data type
student_id = {100, 111, 122, 123} #create a set named student id
print(student_id) #display student_id elements
print(type(student_id)) 

#dictionary data type
capital_city = {'Nairobi': 'Kenya', 'Dodoma': 'Tanzania'} #this is a dictionary
print(capital_city['Nairobi'])

bob = 'testing'
print(len(bob))