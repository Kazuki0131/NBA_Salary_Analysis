# NBA_salary_analysis

![NBA_analytics](image/NBA_analytics.jpg)

## Background
NBA is one of famous professional sport leagues in the world. Each team has a perceived worth of $1.2 billion or more per Forbes' annual report. The average NBA player salary is $7.7 million for the season (2019 - 2020). The Golden State Warrior star Stephen Curry's earnings for the season (2019 -2020) is $40.2 million. How has the highest paid salaries been determined? Do players who have high game performance always receive high salary contracts?

## Project outline
This project is to analyze status and salaries of players, find the relationship between game perhormance and salaries of players and create a machine learning mode to predict salaries using status. The result of project is hosted as Flask app on AWS. The flask app contains three parts: dashboard, analysis, and prediction.

dashboard: showing status of teams and players
analysis: analyzing salary data of NBA players from 2010 to 2019 seasons
prediction: predicting salary using the trained Azure machine learning mode

### process
1. scraping data of NBA teams and players (2020 season) from basket ball-reference.com for dashboard and upload the data to dynamoDB on AWS. (the deatil is in dashboard folder.)

2. creating analysis using Tableau.

3. scraping status data of NBA players (2010 - 2019 seasons) from basketball-reference.com, combine the status data and salary data of NBA players from kaggle.com, training machine learning mode on Azure using the combined data and creating a web application of Azure ML to predict salary. (the deatil is in Azure_ML folder.)

4. creating the Flask app with the dashboard, Tableau analysis, and web application of Azure ML and hosting it on AWS (the detail is in web_app folder.)

## Technology used
Flask, AWS, DynamoDB, Azure ML, Javascript, Tableau, Python
