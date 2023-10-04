#!/usr/bin/python3
import re
import sys

restaurant_pattern='''@Oden'''
ingredient_pattern='''@Glen'''
RGB_pattern='''rgb\(\d{1,3},\s*\d{1,3},\s*\d{1,3}\)'''
social_pattern='''^@[\w\d_]+$'''
product_pattern='''@Ade'''
news_pattern='''@Glen'''
event_pattern=r'''\w{3}\s\d{2},\s\d{4}\s-\s\d{2}:\d{2}\s(AM|PM)'''
email_pattern='''[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'''

def get_lines(file_name: str) -> [str]:
    """
    This function returns the lines from the file as a list.
    It handles the opening and closing of the file.
    Also, the function assumes the file exists and can be read.
    """
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return lines

data = get_lines(sys.argv[1])
colors = []
events = []
emails = []
social = []
for item in data:
    colors += re.findall(RGB_pattern, item)
    events += re.findall(event_pattern, item)
    emails += re.findall(email_pattern, item)
    social += re.findall(social_pattern, item)
print(colors)
print(events)
print(emails)
print(social)
