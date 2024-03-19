#number 1
user_input = input('Please enter numbers separated by spaces: ')
input_list = user_input.split() #splitting the user input into a list of strings
integer_list = [int(num) for num in input_list] #converting the list of strings into a list of integers
total_sum = sum(integer_list) #adding the integers in the list
print(f'The sum of the numbers is: {total_sum}')

#number 2
apps = {'Whatsapp', 'Tiktok', 'Twitter', 'Instagram', 'Pinterest'}
for app in apps:
    print(app)

#number 3
info = {} #empty dictionary
name = input('\nPls enter your name: ')
age = input('Pls enter your age: ')
color = input('Pls enter your fav color: ')

#store information in the dictionary
info['name'] = name
info['age'] = age
info['color'] = color

#print the dictionary
print('\nYour information:')  #\n adds a new line before printing the message
for key, value in info.items():  #loops over the info dictionary, 'items() returns a view object that displays a list of a dict key-value pairs
    print(key.capitalize() + ':', value.capitalize())


#number 4
input1 = input('\nEnter numbers separated by spaces for set 1: ')
set1 = set(map(int, input1.split()))    
input2 = input('Enter numbers separated by spaces for set 2: ')
set2 = set(map(int, input2.split()))

#creating a new set containing common elements only
common = set1.intersection(set2)
print(f'These are the common elements in both sets: {common}')

#number 5
words = input('Input random words separated by a space: ')
list = words.split() #this separates the words
odd_length_words = [word for word in list if len(word) % 2 != 0]
print(f'The words with odd number of characters are: {odd_length_words}')