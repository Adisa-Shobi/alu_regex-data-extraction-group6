# Regex Hackathon
## Prologue
You have just graduated with a degree in computer science and landed your first job as a Junior Software Engineer at a startup building a new social media app. The app aggregates data from different sources and displays it to users in a personalized feed.

The backend engineering team has built an API that pulls in data from various sources like news outlets, social networks, blogs etc. But the data is raw and unstructured. As a new hire, you have been tasked with writing scripts to extract and structure specific kinds of data from the raw API responses.

Here are some of the data types the product team needs extracted:

- Restaurant names and cuisine types
- Ingredient lists from recipes
- RGB color values
- Social media usernames
- Product codes
- News headlines
- Event dates and times
- Email addresses
## The Task
To efficiently extract these different data types from the messy API responses, you decide to use regular expressions. Based on examples of how these data types commonly appear, you have summarized patterns that can be used to match them:

- Restaurant names and cuisines follow "Name - Cuisine" where both are arbitrary strings.
- Ingredient lists are comma-separated like "ingredient1, ingredient2, ingredient3".
- RGB colors are strings like "rgb(255, 255, 255)" with 3 numeric values.
- Social media usernames are in the format "@username" where username can be letters and numbers.
- Product codes are formatted as "ABC123" where A, B and C are letters and 1, 2 and 3 are digits.
- News headlines follow the pattern "Headline: Subheader" where both parts are arbitrary strings.
- Event dates/times follow the pattern "MMM DD, YYYY - hh:mm AM/PM" with standard date and 12-hour time formatting.
- Email addresses follow the common format "name@domain.com".
## Requirements
1. I have created group sets for this assignment. Go to the People  menu on Canvas and join a team of your choice
2. Your github should be created with your ALU email address
3. Any group can choose a minimum of 5 challenges out of the 8 for this hackathon (You can also opt to doing all of the challenges which will have the 3 challenges become bonuses)
4. Create a GitHub repo named "alu_regex-data-extraction-groupN" where N is your Group number. Therefore, for instance, the repository name of Group One will be alu_regex-data-extraction-group1
5. Every team member must commit code at least once. Your contribution will be checked using an automated tool
6. You can use Python or JavaScript for implementation.
7. Have FUN and Happy Coding!
