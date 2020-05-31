# Creating a Machine Learing mode to predict NBA salary on Azure Machine Learning Studio

1. download the NBA_FULL_Salaries_2000-2019.csv from [kaggle.com](https://www.kaggle.com/hrfang1995/nba-salaries-by-players-of-season-2000-to-2019)

2. run NBA_players_salary_data.ipynb. The jupyter notebook will scrape 10 years NBA players data (2010 - 2019) from basketball-reference.com, combine the players data and salary data (NBA_FULL_Salaries_2000-2019.csv), and split players to 3 groups by salary ranges ("$0 - $2,000,000", "$2,000,000 - $8,000,000", and "more than $8,000,000"). (the result is players_salary_by_groups.csv)

3. use the result (players_salary_by_groups.csv) from the jupyter notebook to create machine learning mode on Azure Machine learning Studio.

4. create your machine learning mode on Azure Machine Learning Studio and make/deploy it as web application

5. After creating your machine learning web applocation, copy your Primary key and Request Response url to the my_api_info.py in Flask_app (check the README.md in web_app folder)
