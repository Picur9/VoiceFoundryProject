'''
Functionality:
    - Write the 5 best options to DynamoDb and sending the 3 best options to Amazon Connect

Lambda function will be tiggered by an event from Amazon Connect and getting a Json file which will include the Costumer phone number.

The "receivedAttribute" will be point to the number from the event which is located under "Details""ContactData""CustomerEndpoint""Address" in the JSON file"

It will send the received date vanity.py and waiting for return.

The code specify the DynamoDb table name("number-to-letters"), which will store the callers id as well as the 5 option received back.  

Also specify the 6 colloum of the table to writhe the return data into. 

The retun will send the top 3 option back to Amazon Connect for the costumer the hear straight away. 

'''

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
    resultMap = { 
            'Option1': vanity_number[0],
            'Option2': vanity_number[1],
            'Option3': vanity_number[2],}
    return resultMap
