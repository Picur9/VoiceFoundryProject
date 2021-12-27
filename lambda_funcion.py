import boto3
import vanity

def lambda_handler(event, context):
    receivedAttribute = event["Details"]["ContactData"]["CustomerEndpoint"]["Address"]
    vanity_number=vanity.generate(receivedAttribute)
    client = boto3.resource('dynamodb')
    table = client.Table('number-to-letters')
    
    
    input = {
            'CallerId':  receivedAttribute,
            'Option1': vanity_number[0],
            'Option2': vanity_number[1],
            'Option3': vanity_number[2],
            'Option4': vanity_number[3],
            'Option5': vanity_number[4]
        
    }
    response = table.put_item(Item=input)
    return input
