# import the json utility package since we will be working with a JSON object
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    name = event['firstName'] +' '+ event['lastName']
    file = event['firstName'] + '.json'
    
    surveyEntry = {
        'name': name,
        'email': event['email'],
        'vaccinated': event['vaccinated'],
        'symptoms': event['symptoms'],
        'location': event['location']
    }
    
    bucket = 'covid-survey-data'
    data = bytes(json.dumps(surveyEntry).encode('UTF-8'))
    s3.put_object(Bucket=bucket, Key=file, Body=data)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Your response has been collected. Thank you!')
    }