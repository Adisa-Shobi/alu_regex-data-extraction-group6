#!/usr/bin/python3
import re
import sys

restaurant_pattern='''\w{2,25}\s\-\s\w{2,25}''' #Oden
ingredient_pattern='''([a-zA-Z_.+-]+),'''  #Glen
RGB_pattern='''rgb\(\d{1,3},\s*\d{1,3},\s*\d{1,3}\)'''
social_pattern='''@[a-zA-Z0-9_]+'''
product_pattern='''[A-Z]{3}[0-9]{3}'''
news_pattern='''[a-zA-Z]+\s[a-zA-Z]+:\s[a-zA-Z]+\s[a-zA-Z]+\s[a-zA-Z]+'''  #Glen
event_pattern='''\w{3}\s\d{2},\s\d{4}\s-\s\d{2}:\d{2}\s\w{2}'''
email_pattern='''[a-zA-Z0-9_.+-]+@[a-zA-Z-]+\.[a-zA-Z-.]+'''

def get_lines(file_name: str) -> [str]:
    """
    This function returns the lines from the file as a list.
    It handles the opening and closing of the file.
    Also, the function assumes the file exists and can be read.
    """
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return lines
# print(get_lines('dummy-data.txt'))

data = get_lines(sys.argv[1])

colors = []
events = []
emails = []
social = []
ingredients = []
news = []
product = []
restaurants = []
for item in data:
    colors += re.findall(RGB_pattern, item)
    events += re.findall(event_pattern, item)
    emails += re.findall(email_pattern, item)
    social += re.findall(social_pattern, item)
    ingredients += re.findall(ingredient_pattern, item)
    news += re.findall(news_pattern, item )
    product += re.findall (product_pattern, item)
    restaurants += re.findall(restaurant_pattern, item)
print(colors)
print(events)
print(emails)
print(social)
print(ingredients)
print(news)
print(product)
print(restaurants)
