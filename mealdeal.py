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

number = int(input('> '))
meal = real_meals[number - 1]
actual_meal = meal
print(f'Here is the information for: {meal}')

meal = food.split('},{')[number - 1]

lst = meal.split(',')
img = re.search('("strMealThumb":")(.*)"', lst[1])
image_link = re.sub(r'\\', '', img.group(2))

p = re.compile(r'\d+')
for match in p.finditer(lst[2]):
    food_id = match.group(0)

# Download image for food
with open('food.jpg', 'wb') as handle:
        response = requests.get(image_link, stream=True)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)

recipe = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772').text
p = re.compile(r'"strInstructions":"(.+)","strMealThumb"')
recette = re.finditer(p, recipe)

recipe = ''
for i in recette:
    recipe = i.group(0)[19:-16]

recipe = re.sub(r'\\r\\n', '<br>', recipe)

# Things we actually care about
# actual_meal - name of meal
# recipe - recipe

with open('food_info.html', 'w') as f:
    f.write('<!DOCTYPE html>')

with open('food_info.html', 'a') as f:
    f.write('<html>')
    f.write(f'<title>{actual_meal}</title>')
    f.write(f'<h1>{actual_meal}</h1>')
    f.write(f'<img src="food.jpg">')
    f.write(f'<p>{recipe}</p>')
    f.write('</html>')
