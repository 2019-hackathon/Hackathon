import requests
import re

with open('categories.txt', 'r') as f:
    categories = f.read().split()

print('What are you in the mood for?\n')
for n, category in enumerate(categories):
    print(f'{n+1}. {category}')

category = categories[int(input('> ')) - 1]

link = f'https://www.themealdb.com/api/json/v1/1/filter.php?c={category}'
food = requests.get(link).text

p = re.compile(r'"strMeal":.*?,')
result = p.finditer(food)

real_meals = []
for i in result:
    real_meals.append(i.group(0)[11:-2])

print()
print('Pick a meal:')
for n, meal in enumerate(real_meals):
    print(f"{n+1}. {meal}")

meal = real_meals[int(input('> ')) - 1]
print(f'Here is the information for: {meal}')

# Download image for food
print(food)
