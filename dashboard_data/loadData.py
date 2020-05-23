import boto3
import json
import decimal
import time

#dynamo_client = boto3.Session(region_name='us-east-1').client('dynamodb')
dynamo_client= boto3.resource('dynamodb', region_name='us-east-1')

jsonFiles = ["NBA_teams_data.json", "NBA_players_data.json"]


for jsonFile in jsonFiles:
    if jsonFile == "NBA_teams_data.json":
        table_name = 'teams'
    else:
        table_name = 'players'

    table = dynamo_client.Table(table_name)

    with open(jsonFile) as json_file:
        # movies = json.load(json_file, parse_float = decimal.Decimal)
        dataset = json.load(json_file, parse_float = decimal.Decimal)
        print(dataset)
        #upload the json data to dynamoDB
        for data in dataset:
            #upload each item in json data to dynamoDB
            print(data)
            table.put_item(
                Item = data
            )
