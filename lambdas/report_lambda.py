import boto3
import datetime

s3 = boto3.client("s3")

BUCKET = "event-driven-pipeline-nandeesh-4821"

def lambda_handler(event, context):
    response = s3.list_objects_v2(
        Bucket=BUCKET,
        Prefix="raw/"
    )

    event_count = len(response.get("Contents", []))

    today = datetime.date.today().isoformat()
    report = f"date,event_count\n{today},{event_count}"

    s3.put_object(
        Bucket=BUCKET,
        Key="reports/daily_report.csv",
        Body=report
    )

    return {
        "status": "report generated",
        "events": event_count
    }
