
import boto3
from botocore.exceptions import ClientError

client = boto3.client('s3') # example client, could be any
REGION = client.meta.region_name

def notify(event, context):

    aws_lambda = boto3.client('lambda')
    tags = aws_lambda.list_tags(Resource = arn)
    address = tags['Tags']['who']

    SUBJECT = f"""Chris' hourly lambda spam """

    SENDER = f"Serverless example code <spam@rsgiscx.net>"


    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = (f"Chris' Hourly Serverless Cron Spam\r\n"
                 f"This GitHub project at https://github.com/hobu/chrisspam demonstrates a https://www.serverless.com Serverless configuration that creates a Lambda function that fires and email to Chris Irwin every hour until he figures out how to shut it off."
                )

    # The HTML body of the email.
    BODY_HTML = f"""<html>
    <head></head>
    <body>
      <h1>Chris' Hourly Serverless Cron Spam</h1>
      <p>
          This <a href="https://github.com/hobu/chrisspam">GitHub project</a> demonstrates a <a href="https://www.serverless.com/">Serverless</a> configuration that creates a Lambda function that fires and email to Chris Irwin every hour until he figures out how to shut it off.
      </p>
    </body>
    </html>
                """

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name='us-east-1')
    logger.debug(f'Sending email to {addresses} {type(addresses)}')

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [address],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    # Display an error if something goes wrong.
    except ClientError as e:

        logger.debug(e.response['Error']['Message'])
    else:
        logger.debug("Email sent! Message ID:"),
        logger.debug(response['MessageId'])


