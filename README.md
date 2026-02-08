# Event-Driven Data Processing Pipeline (AWS)

This project implements a fully serverless, event-driven data processing pipeline on AWS.  
Incoming events are captured through an HTTP endpoint, stored for analysis, and summarized using an automated daily reporting workflow.

---

## Architecture Overview

The solution is built using AWS managed services in a serverless architecture:

- Amazon API Gateway – HTTP entry point for event ingestion  
- AWS Lambda – Event ingestion and daily report generation  
- Amazon S3 – Storage for raw event data and generated reports  
- Amazon EventBridge – Scheduled trigger for daily reporting  
- Terraform – Infrastructure as Code  
- GitHub Actions – CI/CD for automated Lambda deployment  

---

## Processing Flow

1. Client sends event data via HTTP request  
2. API Gateway triggers the ingest Lambda function  
3. Raw event data is stored in Amazon S3  
4. EventBridge triggers the report Lambda on a daily schedule  
5. A summarized CSV report is generated and stored in Amazon S3  

---

## Automation and CI/CD

- Infrastructure is defined using Terraform
- GitHub Actions automatically deploys Lambda functions on each push to the main branch
- AWS credentials are securely managed using GitHub Secrets
- Successful CI/CD executions are visible in the GitHub Actions tab

---

## Repository Structure

event-driven-pipeline/
├── lambdas/
│ ├── ingest_lambda.py
│ ├── report_lambda.py
│
├── terraform/
│ ├── provider.tf
│ ├── s3.tf
│ └── outputs.tf
│
├── .github/
│ └── workflows/
│ └── deploy-lambda.yml
│
└── README.md


---

## Deployment Notes

- The project is designed to stay within AWS Free Tier limits
- Terraform state files and provider binaries are excluded from version control
- The solution does not use Docker or container-based services

---

## Author

Nandeesh