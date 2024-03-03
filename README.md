# AWS Infrastructure Automation

## Overview

This repository contains scripts and code for automating various tasks related to AWS infrastructure management.

### 1. EBS Cleanup Script (`EBS_Delete.py`)

The `EBS_Delete.py` script is designed to perform cleanup operations on AWS Elastic Block Store (EBS) snapshots. It is intended to be used as part of an automation process to manage EBS snapshots efficiently.

### 2. Lambda Function for EC2 CPU Alerts

The Lambda function monitors CPU utilization of EC2 instances and triggers alerts when CPU usage exceeds a certain threshold. It utilizes Amazon CloudWatch for monitoring and Amazon Simple Notification Service (SNS) for sending alerts.

## Prerequisites

- Python 3 installed on your local machine.
- AWS account with appropriate permissions to create and manage Lambda functions, CloudWatch alarms, and SNS topics.

## Installation and Setup

1. Clone this repository to your local machine:

2. Navigate to the directory containing the scripts or Lambda function code.

3. Install the required Python packages using pip:


4. For the Lambda function:
- Set up the AWS environment:
  - Create an IAM role with permissions for Lambda execution, CloudWatch access, and SNS publishing.
  - Create an SNS topic and subscribe to it to receive alerts.
- Deploy the Lambda function using your preferred deployment method (AWS CLI, AWS Console, etc.).
- Configure CloudWatch alarms to monitor CPU utilization of EC2 instances and trigger the Lambda function when thresholds are exceeded.

## Usage

- For the EBS Cleanup Script:
- Run the script using the command:
 ```
 /usr/bin/python3 EBS_Delete.py
 ```

- For the Lambda function:
- Monitor alerts sent via SNS for any CPU spikes in your EC2 instances.

## Notes
- Ensure proper IAM permissions are assigned to Lambda functions and other AWS resources.

