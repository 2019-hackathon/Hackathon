import requests
import re
import webbrowser

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
    meal = re.sub(r'\\r\\n', '<br>', meal)
    meal = re.sub(r'\\u00b0', '°', meal)
    meal = re.sub(r'\\u00e8', 'è', meal)
    meal = re.sub(r'\\u00bd', '½', meal)
    meal = re.sub(r'\\u00e0', 'à', meal)

    print(f"{n+1}. {meal}")

number = int(input('> '))
meal = real_meals[number - 1]

actual_meal = re.sub(r'\\r\\n', '<br>', meal)
actual_meal = re.sub(r'\\u00b0', '°', actual_meal)
actual_meal = re.sub(r'\\u00e8', 'è', actual_meal)
actual_meal = re.sub(r'\\u00bd', '½', actual_meal)
actual_meal = re.sub(r'\\u00e0', 'à', actual_meal)

print(f'Here is the information for: {actual_meal}')

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


recipe = requests.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={food_id}').text

p = re.compile(r'"strInstructions":"(.+)","strMealThumb"')
recette = re.finditer(p, recipe)

recipe = ''
for i in recette:
    recipe = i.group(0)[19:-16]

recipe = re.sub(r'\\r\\n', '<br>', recipe)
recipe = re.sub(r'\\n', '<br>', recipe)

blank = ''
count = 1
for i in recipe.split('<br>'):

    if i:
        blank += str(count) + '. '
        count += 1
        blank += i
        blank += '<br>'

recipe = blank

# Things we actually care about
# actual_meal - name of meal
# recipe - recipe

with open('food_info.html', 'w') as f:
    f.write('<!DOCTYPE html>')

with open('food_info.html', 'a') as f:
    f.write(f'<meta charset="utf-8"/>')
    f.write('<html>')
    f.write('<head>')
    f.write(f'<title>{actual_meal}</title>')
    f.write(f'<link href="foodstyle.css" rel="stylesheet" type="text/css">')
    f.write(f'</head>')

    f.write(f'<body>')
    f.write(f'<header>')
    f.write(f'<nav id="navbar" class="navbar-fixed">')

    f.write('<ul>')
    f.write('<li><a class="active" href="index.html">Home</a></li>')
    f.write('<li><a href="#first">Make Your Own</a></li>')
    f.write('<li><a href="food_info.html">Stories</a></li>')
    f.write('<li><a href="#bottom">About Us</a></li>')
    f.write('</ul>')
    f.write('</nav>')
    f.write('<br>')

    f.write(f'<div class="words">')
    f.write(f'<h1>{actual_meal}</h1>')

    f.write(f'<br><br>')

    f.write(f'<img src="food.jpg" height="750" width="750">')
    f.write(f'</div>')

    f.write(f'<div class="gay">')

    f.write(f'<p>{recipe}</p>')
    f.write(f'</div>')
    f.write('</header>')
    f.write('</body>')

    f.write('</html>')

with open('food_info.html', 'r') as f:
    web = f.read()

web = re.sub(r'\\u00b0', '°', web)
web = re.sub(r'\\u00e8', 'è', web)
web = re.sub(r'\\u00bd', '½', web)
web = re.sub(r'\\u00e0', 'à', web)

with open('food_info.html', 'w') as f:
    f.write(web)

webbrowser.open('/tmp/hack/food_info.html', new=0, autoraise=True)
