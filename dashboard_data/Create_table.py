mport boto3
import time
import json, decimal

# dynamo_client = boto3.client('dynamodb')
dynamo_client = boto3.Session(region_name='us-east-1').client('dynamodb')

dynamo = boto3.resource('dynamodb', region_name="us-east-1")


def create_table(table):
        # table='bobTable'
        # table='teams'
        # attr_name = 'team'

        # table='players'
        if table == 'players_test':
            attr_name = 'player'
        else:
            attr_name = 'team'

        response = dynamo_client.create_table(
            AttributeDefinitions=[{
                # 'AttributeName': 'event',
                'AttributeName': attr_name,
                'AttributeType': 'S'
            }
   
            ], 
                TableName=table, 
                KeySchema=[{
                    # 'AttributeName': 'event', 
                    'AttributeName': attr_name, 
                    'KeyType': 'HASH'
	}
    
    ]
            , 
            ProvisionedThroughput={
                'ReadCapacityUnits': 1, 
                'WriteCapacityUnits': 2
            }
      )
        time.sleep(5)
        # put_item()
        return response

tables = ['teams','players']

for table in tables:
    create_table(table)


