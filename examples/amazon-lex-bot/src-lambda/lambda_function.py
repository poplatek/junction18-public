import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    logger.info('got: ' + str(event))
    
    weight = event['currentIntent']['slots']['Weight']
    logger.info('weight: ' + str(weight))
    
    result = {
        'dialogAction': {
            'type': 'Close',
            "message": {
              "contentType": "PlainText",
              "content": "Thank you! Logged " + str(weight) + " kilos."
            },
            'fulfillmentState': 'Fulfilled'
        }
    }
    
    return result
