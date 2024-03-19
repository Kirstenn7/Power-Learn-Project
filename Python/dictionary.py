#Italy is the key and Rome is the value
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
print(capital_city)

numbers = {1: 'One', 2: 'Two', 3: 'Three'}
print(type(numbers)) #class 'dict'

#adding elements
capital_city['Japan'] = 'Tokyo' #japan = key, tokyo = value
print('Updated Dictionary:', capital_city)

#change value
student_id = {111: 'Eric', 112: 'Kyle', 113:'Bob'}
print('Initial dictionary:', student_id)
del student_id[111]
print('Updated dictionary:', student_id)

student_id[112] = 'Stan' #change the value Kyle to Stan
print(student_id)

#membership test for dictionary keys
squares = {1:1, 3:9, 5:25, 7:49, 9:81}
print(1 in squares)
print(2 not in squares)
print(4 in squares)
print(49 in squares) #prints false bc membership tests are for keys only

#iterating through a dictionary
for i in squares:
    print(squares[i]) #here, we have iterated through each key in the squares dictionary using the for loop
