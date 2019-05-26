import requests
import re
import webbrowser
import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path='~/Desktop/Chris/Hackathon/chromedriver')

with open('categories.txt', 'r') as f:
    categories = f.read().split()

with open("chooser.html", "w") as f:
    f.write("<!DOCTYPE html>")

with open("chooser.html", "a") as f:
    f.write("<html>")
    f.write("<title>Menu Chooser</title>")
    f.write("<h1>Choose a category:</h1>")
    f.write("<ol>")

    for me in categories:
        me = re.sub(r'\\r\\n', '<br>', me)
        me = re.sub(r'\\u00b0', '°', me)
        me = re.sub(r'\\u00e8', 'è', me)
        me = re.sub(r'\\u00bd', '½', me)
        me = re.sub(r'\\u00e0', 'à', me)
        f.write(f"<li>{me}")

    f.write("</ol>")
    f.write('<button onclick="enter()">Click to Choose</button>')
    f.write('<p id="choice1"></p>')
    f.write('<script>function enter() {  var choice = prompt("Choose a number", "1"); document.getElementById("choice1").innerHTML = choice; } </script>')
    f.write("</html>")

url = 'file:///tmp/hack/chooser.html'

browser.get(url)

num = browser.find_element_by_id("choice1")
inner = browser.execute_script("return document.body.innerHTML")
print(inner)

print(site)

category = categories[int(input('> ')) - 1]

link = f'https://www.themealdb.com/api/json/v1/1/filter.php?c={category}'
food = requests.get(link).text

p = re.compile(r'"strMeal":.*?,')
result = p.finditer(food)

real_meals = []
for i in result:
    real_meals.append(i.group(0)[11:-2])

with open("chooser.html", "w") as f:
    f.write("<!DOCTYPE html>")

with open("chooser.html", "a") as f:
    f.write("<html>")
    f.write("<title>Menu Chooser</title>")
    f.write("<h1>Choose your meal:</h1>")
    f.write("<ol>")

    for me in real_meals:
        me = re.sub(r'\\r\\n', '<br>', me)
        me = re.sub(r'\\u00b0', '°', me)
        me = re.sub(r'\\u00e8', 'è', me)
        me = re.sub(r'\\u00bd', '½', me)
        me = re.sub(r'\\u00e0', 'à', me)
        f.write(f"<li>{me}")

    f.write("</ol>")
    f.write("</html>")

webbrowser.open('./chooser.html', new=0, autoraise=True)

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
