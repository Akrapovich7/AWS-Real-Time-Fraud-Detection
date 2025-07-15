import json
import boto3
import uuid
from datetime import datetime

frauddetector = boto3.client('frauddetector')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FraudDetectionResults')

def lambda_handler(event, context):
    # Parse the JSON body from API Gateway event
    body = json.loads(event['body'])

    event_id = str(uuid.uuid4())
    entity_id = body['entity_id']

    variables = {
        'ip_address': body['ip_address'],
        'email_address': body['email_address'],
        'transaction_amount': str(body['transaction_amount'])
    }

    response = frauddetector.get_event_prediction(
        detectorId='transaction_detector',
        eventId=event_id,
        eventTypeName='transaction_event',
        eventTimestamp=datetime.utcnow().isoformat() + "Z",
        entities=[{
            'entityId': entity_id,
            'entityType': 'transaction_entity'  # Replace with your actual entity type
        }],
        eventVariables=variables
    )

    print("Fraud Detector response:", response)

    prediction = "no_match"
    if response.get('ruleResults') and len(response['ruleResults']) > 0:
        if 'outcomes' in response['ruleResults'][0] and len(response['ruleResults'][0]['outcomes']) > 0:
            prediction = response['ruleResults'][0]['outcomes'][0]

    table.put_item(Item={
        'event_id': event_id,
        'entity_id': entity_id,
        'timestamp': datetime.utcnow().isoformat(),
        'prediction': prediction,
        'ip_address': variables['ip_address'],
        'email_address': variables['email_address'],
        'transaction_amount': variables['transaction_amount']
    })

    return {
        'statusCode': 200,
        'body': json.dumps({
            'event_id': event_id,
            'prediction': prediction
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
