# Accessing Amazon CloudWatch logs for AWS Lambda<a name="monitoring-cloudwatchlogs"></a>

AWS Lambda automatically monitors Lambda functions on your behalf, reporting metrics through Amazon CloudWatch\. To help you troubleshoot failures in a function, after you set up permissions, Lambda logs all requests handled by your function and also automatically stores logs generated by your code through Amazon CloudWatch Logs\. 

You can insert logging statements into your code to help you validate that your code is working as expected\. Lambda automatically integrates with CloudWatch Logs and pushes all logs from your code to a CloudWatch Logs group associated with a Lambda function, which is named /aws/lambda/*<function name>*\.

You can view logs for Lambda functions using the Lambda console, the CloudWatch console, the AWS Command Line Interface \(AWS CLI\), or the CloudWatch API\. This page describes how to view logs using the Lambda console\.

**Note**  
It may take 5 to 10 minutes for logs to show up after a function invocation\.

**Topics**
+ [Prerequisites](#monitoring-cloudwatchlogs-prereqs)
+ [Pricing](#monitoring-cloudwatchlogs-pricing)
+ [Using the Lambda console](#monitoring-cloudwatchlogs-console)
+ [Using the AWS CLI](#monitoring-cloudwatchlogs-cli)
+ [What's next?](#monitoring-cloudwatchlogs-next-up)

## Prerequisites<a name="monitoring-cloudwatchlogs-prereqs"></a>

Your [execution role](lambda-intro-execution-role.md) needs permission to upload logs to CloudWatch Logs\. You can add CloudWatch Logs permissions using the `AWSLambdaBasicExecutionRole` AWS managed policy provided by Lambda\. To add this policy to your role, run the following command:

```
aws iam attach-role-policy --role-name your-role --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

For more information, see [AWS managed policies for Lambda features](lambda-intro-execution-role.md#permissions-executionrole-features)\.

## Pricing<a name="monitoring-cloudwatchlogs-pricing"></a>

There is no additional charge for using Lambda logs; however, standard CloudWatch Logs charges apply\. For more information, see [CloudWatch pricing\.](https://aws.amazon.com/cloudwatch/pricing/)

## Using the Lambda console<a name="monitoring-cloudwatchlogs-console"></a>

**To view logs using the Lambda console**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console\.

1. Choose a function\.

1. Choose **Monitor**\.

1. Choose **View logs in CloudWatch**\.

## Using the AWS CLI<a name="monitoring-cloudwatchlogs-cli"></a>

To debug and validate that your code is working as expected, you can output logs with the standard logging functionality for your programming language\. The Lambda runtime uploads your function's log output to CloudWatch Logs\. For language\-specific instructions, see the following topics:
+  [AWS Lambda function logging in Node\.js](nodejs-logging.md) 
+  [AWS Lambda function logging in Python](python-logging.md) 
+  [AWS Lambda function logging in Ruby](ruby-logging.md) 
+  [AWS Lambda function logging in Java](java-logging.md) 
+  [AWS Lambda function logging in Go](golang-logging.md) 
+  [Lambda function logging in C\#](csharp-logging.md) 
+  [AWS Lambda function logging in PowerShell](powershell-logging.md) 

## What's next?<a name="monitoring-cloudwatchlogs-next-up"></a>
+ Learn more about log groups and accessing them through the CloudWatch console in [Monitoring system, application, and custom log files](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.html) in the *Amazon CloudWatch User Guide*\.