import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
import decimal


def lambda_handler(event, context):
    
    
    # TODO implement
    name1=event['name']
    email = event['email']
    dob1 = event['dob']
    mobile1 = event['mobile']
    dynamo_db = boto3.resource('dynamodb') 
    match_table = dynamo_db.Table('dr11-userwalletdb')
   
  
    response = match_table.put_item(
     Item={
        'name': name1,
        'email': email,
        'dob' : dob1,
        'mobile' : mobile1,
        'balance' : 0,
     }
    )
    
    return { 
            'statusCode': 200, 
            'headers': { 
                "Access-Control-Allow-Origin" : "*", # Required for CORS support to work 
                "Access-Control-Allow-Credentials" : True # Required for cookies, authorization headers with HTTPS  
              }, 
            'body': json.dumps({'name': name1,'email': email,'dob' : dob1,'mobile' : mobile1,'balance' : 0}) 
        } 
