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

name = ''
for i in result:
    name += i.group(0)[11:-2] + '\n'

print(name)
