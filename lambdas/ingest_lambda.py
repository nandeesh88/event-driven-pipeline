import json
import boto3
import datetime

s3 = boto3.client("s3")

BUCKET = "event-driven-pipeline-nandeesh-4821"

def lambda_handler(event, context):
    timestamp = datetime.datetime.utcnow().isoformat()
    key = f"raw/event_{timestamp}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(event)
    )

    return {
        "statusCode": 200,
        "body": "Event stored successfully"
    }
