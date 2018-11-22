# Amazon Lex Bot

Client code for Amazon Lex, example Lambda code to handle a Lex intent, and some tips for building the bot using AWS Console.

## Building the Lex bot

Simply open AWS Console (the web thing), find Lex console, and start a new bot. You can test the bot by pressing Build, and opening the test dialog at the right side of the Lex console.

The Publish button creates a new version of the bot, which you can then call with the client code. Use an alias like 'latest' to point at your latest version.

Check out example for a simple handler Lambda from src-lambda. Note that the handler needs to return a properly crafted dialogAction to make Lex happy.

## Tips for managing the Lex bot and Lambda functions

- Lambda function needs to have an invocation permission for Principal lex.amazonaws.com. If you create the lambda functions via Lex, it automatically adds the permission.

- Lex doesn't yet have CloudFormation support, but the bots can be exported and imported as zip/json files.

- You cannot clone the bots via export/import without renaming the bot and the intents from the exported file first. Lex will complain the about name clashes.

- The Lambda functions referenced from exported bots need to exist, and need to have the invocation permission already in place for the import to work.

## Adding Lex invocation permission to a Lambda function

Needs to be done with AWS CLI, since AWS Console doesn't provide this functionality.

Replace the Lambda and Lex intent ARNs and the statement id before executing:
```
aws lambda add-permission --function-name arn:lambda-arn-here --statement-id my-lex-intent-permission --action 'lambda:invokeFunction' --principal 'lex.amazonaws.com' --source-arn 'arn:lex-intent-arn-here'
```

## Client code

The python example uses pyaudio and SpeechRecognition libraries for recording audio for Lex input, and playing back the audio Lex responds with. No actual speech recognition takes place client side. SpeechRecognition library only provides threshold based recording to know when to start and stop recording.

Before using the example code, configure the audio devices and Lex bot in the beginning of the file.

## Using USB speaker & mic (Jabra)

Jabra needs to be configured properly, or it will try to play the data received from Lex with a wrong sample rate. Place the provided asoundrc file as ```.asoundrc``` to your home directory at the Pi.

## Additional information

- https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/
- https://pypi.org/project/SpeechRecognition/2.1.3/
