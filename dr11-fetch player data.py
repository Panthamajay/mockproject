import json
import boto3
from boto3.dynamodb.conditions import Key,Attr 

def lambda_handler(event, context):
    # TODO implement
    print(event)
    matchid = event['MatchId']
    print(type(matchid))
    dynamodb = boto3.resource('dynamodb') 
    match_table = dynamodb.Table('dr11-publicmatch') 
    matchResponse  = match_table.scan( 
        FilterExpression = Attr('MatchId').eq(int(matchid)) 
    ) 
    print(matchResponse)
    team1_list =  list(matchResponse['Items'][0]['Team1 Players']) 
    
    for i in range(len(team1_list)):
        team1_list[i] = int(team1_list[i])
            
    team2_list =  list(matchResponse['Items'][0]['Team2 Players'])
    for i in range(len(team2_list)):
        team2_list[i] = int(team2_list[i])
    
    print(team1_list)
    print(team2_list)
    Cricket_Player_table = dynamodb.Table('dr11-playerdata') 
    playersResponse  = Cricket_Player_table.scan( 
           FilterExpression = (Attr('playerid').eq(team1_list[0]) | Attr('playerid').eq(team1_list[1]) | Attr('playerid').eq(team1_list[2]) |Attr('playerid').eq(team1_list[3]) | Attr('playerid').eq(team1_list[4]) | Attr('playerid').eq(team1_list[5]) | Attr('playerid').eq(team1_list[6]) | Attr('playerid').eq(team1_list[7]) | Attr('playerid').eq(team1_list[8]) | Attr('playerid').eq(team1_list[9]) | Attr('playerid').eq(team1_list[10]) | Attr('playerid').eq(team2_list[0]) | Attr('playerid').eq(team2_list[1]) | Attr('playerid').eq(team2_list[2]) | Attr('playerid').eq(team2_list[3]) | Attr('playerid').eq(team2_list[4]) | Attr('playerid').eq(team2_list[5]) | Attr('playerid').eq(team2_list[6]) | Attr('playerid').eq(team2_list[7]) | Attr('playerid').eq(team2_list[8]) | Attr('playerid').eq(team2_list[9]) | Attr('playerid').eq(team2_list[10])) 
       ) 
    print('**********')
    print(playersResponse)
    #print(scanExpression)
    return { 
        'statusCode': 200, 
        'headers': { 
                "Access-Control-Allow-Origin" : "*", # Required for CORS support to work 
                "Access-Control-Allow-Credentials" : True # Required for cookies, authorization headers with HTTPS  
              }, 
        'body': json.dumps(playersResponse['Items']) 
       #'body': json.dumps('Hello from Lambda!') 
    } 
    
