import json
import boto3
from boto3.dynamodb.conditions import Key,Attr 

def lambda_handler(event, context):
    # TODO implement
    print(event)
    matchid = event['MatchId']
    registeration_fee = event['Fee']
    print(type(matchid))
    dynamodb = boto3.resource('dynamodb') 
    match_table = dynamodb.Table('dr11-publicmatch') 
    matchResponse  = match_table.scan( 
        FilterExpression = Attr('MatchId').eq(int(matchid)) 
    ) 
    team1 =  matchResponse['Items'][0]['Team1'] 
    team2 =  matchResponse['Items'][0]['Team2'] 
    leagueid = matchResponse['Items'][0]['LeagueId'] 
    team1_list =  list(matchResponse['Items'][0]['Team1 Players']) 
    
    for i in range(len(team1_list)):
        team1_list[i] = int(team1_list[i])
            
    team2_list =  list(matchResponse['Items'][0]['Team2 Players'])
    for i in range(len(team2_list)):
        team2_list[i] = int(team2_list[i])
    print(team1_list)
    print(team2_list)
    print(matchResponse)
    dynamodb1 = boto3.resource('dynamodb') 
    match_table1 = dynamodb1.Table('dr11-privatematch') 
    LeagueId = leagueid
    MatchId = matchid
    Fee = registeration_fee
    Team1 = team1
    Team2 = team2
    Team1 Players[0] = team1_list[0]
    Team1 Players[1] = team1_list[1]
    Team1 Players[2] = team1_list[2]
    Team1 Players[3] = team1_list[3]
    Team1 Players[4] = team1_list[4]
    Team1 Players[5] = team1_list[5]
    Team1 Players[6] = team1_list[6]
    Team1 Players[7] = team1_list[7]
    Team1 Players[8] = team1_list[8]
    Team1 Players[9] = team1_list[9]
    Team1 Players[10] = team1_list[10]
    Team2 Players[0] = team2_list[0]
    Team2 Players[1] = team2_list[1]
    Team2 Players[2] = team2_list[2]
    Team2 Players[3] = team2_list[3]
    Team2 Players[4] = team2_list[4]
    Team2 Players[5] = team2_list[5]
    Team2 Players[6] = team2_list[6]
    Team2 Players[7] = team2_list[7]
    Team2 Players[8] = team2_list[8]
    Team2 Players[9] = team2_list[9]
    Team2 Players[10] = team2_list[10]
    response = table.put_item(
     Item={
        'LeagueId': LeagueId,
        'MatchId': MatchId,
        'Fee' : Fee,
        'Team1' : Team1,
        'Team2' : Team2,
        'Team1 Players' {
                'Team1 Players[0]': Team1 Players[0],
                'Team1 Players[1]': Team1 Players[1],
                'Team1 Players[2]': Team1 Players[2],
                'Team1 Players[3]': Team1 Players[3],
                'Team1 Players[4]': Team1 Players[4],
                'Team1 Players[5]': Team1 Players[5],
                'Team1 Players[6]': Team1 Players[6],
                'Team1 Players[7]': Team1 Players[7],
                'Team1 Players[8]': Team1 Players[8],
                'Team1 Players[9]': Team1 Players[9],
                'Team1 Players[10]': Team1 Players[10]
        }
        'Team2 Players' {
                'Team2 Players[0]': Team2 Players[0],
                'Team2 Players[1]': Team2 Players[1],
                'Team2 Players[2]': Team2 Players[2],
                'Team2 Players[3]': Team2 Players[3],
                'Team2 Players[4]': Team2 Players[4],
                'Team2 Players[5]': Team2 Players[5],
                'Team2 Players[6]': Team2 Players[6],
                'Team2 Players[7]': Team2 Players[7],
                'Team2 Players[8]': Team2 Players[8],
                'Team2 Players[9]': Team2 Players[9],
                'Team2 Players[10]': Team2 Players[10]
        }
     }
  )
  print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
