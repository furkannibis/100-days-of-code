import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

random_float = round(random.random() * 5, 2)
print(random_float)

love_score = random.randint(1, 2)
print(f'Your love score is {love_score}.')

state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware",
               "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts",
               "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire",
               "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina",
               "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

print(state_names[0])
print(state_names[-1])

state_names.append('Furkanland')
state_names.extend(['Somewhereland', 'Othersomewhereland'])

print(state_names[-1], state_names[-2], state_names[-3])
print(state_names[len(state_names) - 1])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]