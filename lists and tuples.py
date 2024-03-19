#Lists
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)

languages = ['English', 'Swahili','Dutch', 'French', 'German', 'Dutch']
print(languages[2]) #French is index 2 on the list
print(languages[-1]) #Dutch (negative indexing)
#the list index always starts with 0

#list slicing
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(my_list[2:5]) #items from index 2 to index 4
print(my_list[5:]) #items from index 5 to end
print(my_list[:]) #all items in the list

#adding elements to a python list
#append()
Numbers = [11,12,13,14,15,16,17,18,19]
print('Before Append:', Numbers)
Numbers.append(20) #adds a number to the end of the list
print('After Append:', Numbers)

#extend()
prime_numbers = [2,3,5]
even_numbers = [4,6,8]
prime_numbers.extend(even_numbers) #extend joins the two lists
print('List after extend:', prime_numbers)

#changing list items
Languages = ['Python', 'Java', 'C++']
Languages[2] = 'C' #changes the third item to C
print(Languages)

#removing an item from a list
#using del
lang = ['Python', 'Java', 'Dart', 'C++']
del lang[0] #removes the first item
print(lang)
del lang[0:2] #removes first 2 items
print(lang)

#using remove()
Lang = ['Python', 'Java', 'Dart', 'C++']
Lang.remove('Dart')
print(Lang)

#iterating through the list
lan = ['Python', 'Java', 'Dart', 'C++']
for langu in lan:
    print(lan)

#making a list
num = [num*num for num in range(1,7)] #ie: 1*1, 2*2, etc
print(num) 
#here, we have used list comprehension to make a list w each item being increased by power of 2


#Tuples 
#A tuple is immutable, cannot be changed, while a list is mutable
var1 = ('hello')
print(type(var1)) #class 'str'

var2 = ('hello',)
print(type(var2)) #class 'tuple'

var3 = 'hello',  #parentheses is optional
print(type(var3))

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(letters[0]) #first item 'a'
print(letters[-1]) #last item 'g'

fruit = 'a', 'p', 'p', 'l', 'e'
print(fruit.count('p')) #counts number of p's
print(fruit.index('l')) #shows index value of l
