# VoiceFoundryProject
This repo contain my project, which I have done for VoiceFoundry 3rd round interview.

Please call +441135380153 to test my Amazon Connect Call Centre.

Exercise:
1  Create a Lambda that converts phone numbers to vanity numbers and save the best 5 resulting vanity numbers and the caller's number in a DynamoDB table. "Best" is defined as you see fit - explain your thoughts.
2  Create an Amazon Connect contact flow that looks at the caller's phone number and says the 3 vanity possibilities that come back from the Lambda function.
3  Writing and Documentation

Solution: 
0. Chose the region where all serviced available, specially Amazon Connect not available all regions at the moment. 
1. Create a DynamoDb table with a Name : "number-to-letters", and a Particion key of "CallerId"(String).
2. Create and IAM role to let Lambda Access DynamoDB, SNS, and Amazon connect.
3. Create a lambda function  called "writedata" which has 3 python file attached ("lambda_function.py", "twl.py", "vanity.py"). The reason python been used is I was only able
to find the twl.py, which is the vocabulary file in Python.
  
  a, The lambda_function.py code 
    - Write the 5 best options to DynamoDb and sending the 3 best options to Amazon Connect

    - Lambda function will be triggered by an event from Amazon Connect and getting a Json file which will include the Costumer phone number.
    - The "receivedAttribute" will be point to the number from the event which is located under "Details""ContactData""CustomerEndpoint""Address" in the JSON file"
    - It will send the received date vanity.py and waiting for return.
    - The code specify the DynamoDb table name("number-to-letters"), which will store the callers id as well as the 5 option received back.  
    - Also specify the 6 column of the table to writhe the return data into. 
    - The return will send the top 3 option back to Amazon Connect for the costumer. 

  b, The vanity.py code
    - Generates a vanity number from the last 7 digits of a phone number received from Amazon Connect through the Lambda function

    - It can be observed that each digit represents 3 or 4 different letters in the alphabet apart from 0 and 1 
    which doesn't represent any.
    - Map each of the numbers recursive with their string of probable letters, i.e 2 with “abc”, 3 with “def” etc. 
    numbersMap[i] stores all characters that correspond to digit i in phone
    - The helper method _get_substrings(self, word) will return all substing words that can be found in the transformed number.
    - The helper method _get_words(self, phone) will return all possible words that can be obtained by the last 7 digits of the input number 
    in the order of the length of the valid substings it contains. 
    - The helper method _get_all(self, phone) will return all possible alphanumeric variations that can be obtained by the input number. 
    - The helper method _get_numbers(self, number, output, txt, idx, l) will return all possible words that can be obtained by the input number. 
    - The output words are one by one stored in output[]. The txt is appended with the current digit on the current posisiton,
    adding all 3 or 4 possible characters for current digit  and recur for remaining digits.
    
   c, The twl.py code (This code is outsourced) 
    - Check if a word is in the dictionary.

    - Provides a simple API using the TWL06 (official Scrabble tournament) dictionary. Contains American English words that are between 2 and 15 
    characters long, inclusive. The dictionary contains 178691 words.
    - Implemented using a DAWG (Directed Acyclic Word Graph) packed in a binary lookup table for a very small memory footprint, not only on 
    disk but also once loaded into RAM. In fact, this is the primary benefit of this method over others - it is optimized for low memory
    usage (not speed).
    - The data is stored in the Python module as a base-64 encoded, zlib-compressed string.
    - Each record of the DAWG table is packed into a 32-bit integer.
    - MLLLLLLL IIIIIIII IIIIIIII IIIIIIII
    - M - More Flag
    - L - ASCII Letter (lowercase or '$')
    - I - Index (Pointer)
    - The helper method _get_record(index) will extract these three elements into a Python tuple such as (True, 'a', 26). 
    - All searches start at index 0 in the lookup table. Records are scanned sequentially as long as the More flag is set. 
    These records represent all of the children of the current node in the DAWG.
    - The helper method _get_child(index, letter) will return a new index (or None if not found) when traversing an edge to a new node. 
    For example, _get_child(0, 'b') returns 25784.
    - The search is performed iteratively until the sentinel value, $, is found. If this value is found, the string is a word in the dictionary. 
    If at any point during the search the appropriate child is not found, the search fails - the string is not a word.
    - See also: http://code.activestate.com/recipes/577835-self-contained-twl06-dictionary-module-500-kb/
      
4. Test your code with either running the sample JSON file as the event(located on the git "sample.json") on Lambda, ot with running the main.py and the test.py on your local computer.  
5. Create an SNS topic for failed lambda function to send an email.
6. Set up Cloudwatch to set an alarm to trigger the SNS function if there is a Lambda Error. 
7. Set up the Amazon Connect. First setting up the instance. My instance is https://petrucsik.my.connect.aws, test user log in details "test_user", password: "T3stUs3r". This account has a view only access. 
8. Contact your Lambda function with Amazon Connect on the instance set up under "Contact flow" => "AWS Lambda". 
9. Log in to the Amazon Connect Instance and set up the following:
 
              1, The phone number first.
              2, Set hours of Operations
              3, Create a queue
              4, Create your connect flow for this excercise my flow called "myfirstconnectchart" located on the Git "myfirstconnectchart"
              5, Publish your connect flow
              6, Create a routing profiles
              7, Set up the created flow for the phone number destination flow. 
Extras:

There is an advanced Option for generate the Vanity numbers under using the "vanity_advance.py". But find it too long to generate a 7 digit option
and the Lambda 8 second limit within the Amazon Connect has delivered a Timeout error. 
     - Generates a vanity number from the last 7 digits of a phone number.

     - It can be observed that each digit represents 3 or 4 different letters in the alphabet apart from 0 and 1 which doesn't represent any.
     - Map each of the numbers recursive with their string of probable letters, i.e 2 with “abc”, 3 with “def” etc. 
     numbersMap[i] stores all characters that correspond to digit i in phone
     - The helper method _split_word(word) will return all substings and each weight that can be found in the transformed number.
     - Different rules could be set up for defining what weighs more. ATM the more and longer the words are would come out on top.
     - In addition with some letters (eg. A, B, I, R U, Y) and some numbers (eg. 1, 2, 4) that can mean a word on their own adding some extra weight.
     - Ordinals (a number followed by 'st', 'nd', 'rd' or 'th') are also considered to be valid and weight more than just regular numbers.
     - The helper method _get_words(self, phone) will return all possible words that can be obtained by the last 7 digit of the input number 
     in the order of the length of the valid substings it contains. 
     - The helper method _get_all(phone) will return all possible alphanumeric variations that can be obtained by input number. 
     - The helper method _get_numbers(number, output, txt, idx, l) will return all possible words that can be obtained by input number. 
     - The output words are one by one stored in output[]. The txt is appended with the current digit on the current positon,
     adding all 3 or 4 possible characters for current digit  and recur for remaining digits.

Have created a static website which call all saved number from the DynamoDb and display all 5 possible options for all phone number called. 
http://project.petrucsik.co.uk/ this site hosted in a S3 bucket and using Lambda functions and API Gateway to display the information. 

"Record your reasons for implementing the solution the way you did, struggles you faced and problems you overcame."

My main focus was to create a fully working serverless environment, which will use a vocabulary to find as many words from the phone number last 7 digit as possible. I have 
chose the last 7 digit to shortcut the code running time as well in most of the country the first 4 number is the Country and the area number code. In the UK from mobile phone 
we will leave the +4475 as a fix number. This will still give us enough option to create a words.  I have chosen the longest word for the best solution in my code. 
There was a great journey to lunch my first Amazon Connect Centre and see how can I learn from this exciting service. 
There was a challenge to find the right code as well as to write everything in Python, as most of my code before was in JS, but as mentioned before the vocabulary is in Python.
I was able to get a lot of code from the web which helped me to get the project done, and I see I will have to push myself on that front to become better.

"What shortcuts did you take that would be a bad practice in production?"

Some of my services has full access from other services without limitation. Also using one Lambda function to write, convert and give back which will give me the option to use a 
step function and use the more advanced code. 

What would you have done with more time? We know you have a life. :-)

As mentioned above if I do not run out of time probably break down the lambda code to use the advanced code option. 
Also would introduce a first check on the Amazon Connect and give the option for the costumers to choose another number before processing through the lambda function. 
Would like to introduce Amazon Lex to enable the speaking options on Amazon Connect as well as the keyboard. 
Send the options out via text or email to the caller. 
 
main.py and test.py for local run test purpose only, using both version of the vanity code. 
 
Thank you for giving me the opportunity to learn about Amazon Connect and create something with a service I never used and learned from before. I`m looking forward to getting 
any feedback regarding any part of my work. 

                                                                                              Warm Regards,
                                                                                          Geza Gabor Petrucsik
