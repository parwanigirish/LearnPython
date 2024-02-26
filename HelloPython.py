print('hello python');
print("How are you doing python");
print("Hello Python world!");

# learn one to 5 chapters from python crash course

array = [1,2,3,4];
print(array);
array.append(5);
array.append(6);
array.append(7);
print(array);

numeral = 9;
string = "Hello";

print(type(numeral));
print(type(string));
print('type of array is' , type(array));

# concatenate first name and last name

first_name = "Girish";
last_name = "Parwani";
full_name = first_name + " " + last_name;
message = "Hello, " + full_name.title() + "!";
print(message);

# more fun

age = 43
message = "Happy " + str(age) + "th Birthday!"
print(message)

message = "One of Python's strengths is its diverse community."
print(message)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)

message2 = "My first bicycle was a " + bicycles[0] + "."
print(message2)

print('girish'.title());
print('girish');

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse alphabetical list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print("\n")
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

people = ['jaidev','priti','swapnil','aniket','shweta']
print("\n")
print(people)

too_difficult = 'swapnil'
people.remove(too_difficult)
print("\n" + too_difficult.title() + " is too difficult for me.")

numbers = list(range(1,6)) 
print(numbers)

numbers10 = list(range(1,11))
print(numbers10)

numbers10.append(11)
print(numbers10)

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("\nHere are the first five players on my team:")
for player in players[:5]:
	print(player.title())

print("\nTable of number 1 : \n")
numbers10 = list(range(1,11))
for number in numbers10:
	print(number)

print("\nTable of number 2 : \n")
numbers10 = list(range(1,11))
for number in numbers10:
	print(number * 2)

print("\n Table of number 3 : \n")
numbers10 = list(range(1,11))
for number in numbers10:
	print(number * 3)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    
print(squares)


even_numbers = list(range(2,11,2)) 
print(even_numbers)

odd_numbers = list(range(1,10,2))
print(odd_numbers)

my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:] 

my_foods.append('cannoli') 
friend_foods.append('ice cream') 

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n")
magicians = ['alice', 'david', 'carolina']

for magician in magicians: 
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you everyone, that was a great magic show!\n")

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("\nYour admission cost is $" + str(price) + ".")

age = 12

if age < 4:
    price = 0
elif age < 65:
    price = 10
elif age < 18:
    price = 5
elif age >= 65:
    price = 5

print("\nYour admission cost is $" + str(price) + ".")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print("\n" + user.title() + ", you can post a response if you wish.")

cars = ['audi', 'bmw', 'subaru', 'toyota']
print("\n")
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

answer = 42

if answer != 42:
    print("That is not the correct answer. Please try again!")


available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("\nAdding " + requested_topping + ".")
    else:
        print("\nSorry, we don't have " + requested_topping + ".")
        
print("\nFinished making your pizza!")


age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

