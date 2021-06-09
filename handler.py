
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
    SES_REGION = event['info']['sesregion']


    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = (f"Chris' Hourly Serverless Cron Spam\r\n"
                 f""
                )

    # The HTML body of the email.
    BODY_HTML = f"""<html>
    <head></head>
    <body>
      <h1>Chris' Hourly Serverless Cron Spam</h1>
      <pre>{prefix}</pre>
      <p>
          <a href="https://s3.console.aws.amazon.com/s3/buckets/{bucket}?region={REGION}&prefix={collect}/&showversions=false">Console View</a>
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
                'ToAddresses': addresses,
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


