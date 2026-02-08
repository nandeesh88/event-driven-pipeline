resource "aws_s3_bucket" "event_data" {
  bucket = "event-driven-pipeline-nandeesh-4821"

  tags = {
    Project = "EventDrivenPipeline"
    Owner   = "Nandeesh"
  }
}
