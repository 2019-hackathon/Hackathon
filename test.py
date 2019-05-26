import requests

site = requests.get('https://www.themealdb.com/api/json/v1/1/categories.php').text
print(site)