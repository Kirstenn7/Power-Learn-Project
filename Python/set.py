student_id = {110, 111, 112, 113, 114, 115, 116, 117}
print(type(student_id)) #class 'set'
print(student_id)

#creating an empty set
empty_set = set()
#creating an empty dictionary
empty_dictionary = {}

#duplicate items in a set
numbers = {2, 4, 6, 6, 2, 8}
print(len(numbers)) #4
print(numbers) #{8, 2, 4, 6}  the items are in a diff order bc a set has no particular order
#a set cannot contain duplicates

#adding items to a set
nambari = {10, 20, 30, 40}
print('Initial set:', nambari)
nambari.add(50)
print('Updated set:', nambari)

#updating a set w items from another set
companies = {'Lacoste', 'Gucci'}
tech_companies = {'apple', 'google'}
companies.update(tech_companies)
print(companies)

#removing an element from a set
languages = {'Swift', 'Java', 'Python'}
print('Initial set:', languages)
removeValue = languages.discard('Java')
print('Set after remove:', languages)

#iterating over a set
fruits = {'Mango', 'Peaches', 'Lime'}
#for loop to access each fruit
for fruit in fruits:
    print(fruit)

#set operations
#union - joinin
A = {1, 3, 5}
B = {0, 2, 4}
print('Union using |:', A|B)
print('Union using union():', A.union(B))

#intersection - common elements
C = {1, 3, 5}
D = {1, 2, 3}
# print('Intersection using &:', C&D)
print('Intersection using intersection():', C.intersection(D))

#difference
E = {2, 3, 5}
F = {1, 2, 6}
print('Difference using -:', E-F)
print('Difference using difference():', E.difference(F))

#symmetric difference
G = {2, 3, 5}
H = {1, 2, 6}
print('using ^:', G ^ H)
print('using symmetric_difference():', G.symmetric_difference(H))

#check if 2 sets are equal
I = {1, 3, 5}
J = {3, 5, 1}
if I == J:
    print('Set I and J are equal')
else:
    print('Set I and J are not equal')