# ecr-scan-ingest

A Lambda function to send Slack alerts based on ECR scan findings

## Notes

This uses the `requests` library, which is not natively available in Lambda functions.

Run `./bundle.sh` to build your zip file to upload to Lambda. The artifact will be saved to `/tmp/ecr-scan-lambda.zip`

## AWS Docs

[Link](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ecr-eventbridge.html)

Sample EventBridge Event:

```json
{
    "version": "0",
    "id": "85fc3613-e913-7fc4-a80c-a3753e4aa9ae",
    "detail-type": "ECR Image Scan",
    "source": "aws.ecr",
    "account": "123456789012",
    "time": "2019-10-29T02:36:48Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:ecr:us-east-1:123456789012:repository/my-repo"
    ],
    "detail": {
        "scan-status": "COMPLETE",
        "repository-name": "my-repo",
        "finding-severity-counts": {
	        "CRITICAL": 10,
	        "MEDIUM”: 9
	    },
        "image-digest": "sha256:7f5b2640fe6fb4f46592dfd3410c4a79dac4f89e4782432e0378abcd1234",
        "image-tags": []
    }
}
```

## IAM

Lambda role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Lambda policy:

You can use the `AWSLambdaBasicExecutionRole` policy.
