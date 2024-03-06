alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Figure out how far to move the alien based on its speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New position: " + str(alien_0['x_position']))


# Make an empty list for storing aliens.

aliens = []

# Make 30 green aliens.
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
print("...")


#iterating through an objects key value pairs using for name, language in favorite_languages.items()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")


# users object's keys and value objects are accessed through for username, user_info in users.items()

users = {'aeinstein': {'first': 'albert',
                       'last': 'einstein',
                       'location': 'princeton'},
         'mcurie': {'first': 'marie',
                    'last': 'curie',
                    'location': 'paris'},
         }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


# Store information about a pizza being ordered.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.

print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

# key value map in python can be traversed using for key, value in user_0.items()
#user object

user_0 = {
	'username': 'efermi',
          'first': 'enrico',
          'last': 'fermi',
          }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# for key,value in user_0.items()

prompt = "\nPlease tell me a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

#take input from prompt using input function input(prompt)

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

                                   
# Start out with some users that need to be verified,
#  and an empty list to hold confirmed users.
# use functions pop and append on arrays

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user, until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
# Display all confirmed users.

print("\nThe following users have been confirmed:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# python while loop while num <= 5: with incrementor to print sequence of numbers

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


# using int() function and % 2 mod to find out if a given number is even or odd

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# python take input from prompt for name and say hello

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

# python example of key value pair

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # Store the response in the dictionary:
    responses[name] = response
    
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# while true keep taking input and printing, while false when you got quit message, leave the loop
  
active = True

while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)

# array of strings array.remove(array element)
# while 'cat' in pets:

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)

# int() function and if if height >= 36: 

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# calendar.isLeap(2024) function

import calendar
print('is 2024 a leap year ' + calendar.isLeap(2024));
print('is 2023 a leap year ' + calendar.isLeap(2023));
