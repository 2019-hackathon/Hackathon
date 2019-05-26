import requests
import re

with open('categories.txt', 'r') as f:
    categories = f.read()

print(categories)

food = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata').text

p = re.compile(r'"strMeal":.*?,')
result = p.finditer(food)

print()
name = ''
for i in result:
    name += i.group(0)[11:-2]

print(name)
