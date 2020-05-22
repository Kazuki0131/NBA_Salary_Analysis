Scraping NBA teams and players data from basketball-reference.com

1. run scrape_NBA_data.ipynb to create NBA_players_data.json and NBA_teams_data.json.

2. run loadData.py to load the json files to your DynamoDB (Before run loaData.py, check if you have created "aws configure" in your computer. If not, follow the steps to create "aws configure" in your computer.)

* Create a user in IAM and get Access Keys (or use your current AccessKeys)
* If you haven't done it before then install AWSCLI (pip install awscli)
* Run `aws configure` and set your access keys and the region you would like to use for you DynamoDb)

3. After you upload the json files, you should see the tables and data in your DynamoDB.