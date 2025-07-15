# 🚨 Real-Time Fraud Detection System Using AWS

This project showcases a fully implemented real-time fraud detection system built using **Amazon Web Services (AWS)**. It leverages **API Gateway**, **AWS Lambda**, **Amazon Fraud Detector**, and **Amazon DynamoDB** to identify potentially fraudulent transactions as they occur.

---

## ✅ Project Summary

I designed and developed a **real-time fraud detection pipeline** that:

- Accepts and processes incoming transaction data via a secure HTTP API.
- Evaluates the data against **custom fraud rules** using **Amazon Fraud Detector**.
- Automatically logs the transaction and detection results to **Amazon DynamoDB** for audit and analysis.

This system is scalable, serverless, and cost-efficient—ideal for modern fintech applications where fraud prevention is critical.

---

## 📐 System Architecture

The solution consists of the following AWS components:

| Component             | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **Amazon API Gateway** | Acts as the public REST API entry point for transaction submissions.        |
| **AWS Lambda**         | Handles incoming API requests, invokes Fraud Detector, and stores results.  |
| **Amazon Fraud Detector** | Applies machine learning and rule-based logic to detect suspicious activity. |
| **Amazon DynamoDB**     | Persists the transaction results including risk scores and event metadata.  |
| **Amazon CloudWatch** | Captures logs and metrics from Lambda and API Gateway for monitoring and troubleshooting. |
---

## 🎯 Features

- ⚡ **Real-Time Detection**: Evaluate transactions immediately upon receipt.
- 🧠 **Custom Fraud Rules**: Fully configurable detection logic using Amazon Fraud Detector.
- 🌐 **RESTful API Access**: External applications can securely post transaction data.
- 🗃️ **Data Persistence**: Results stored in DynamoDB for monitoring, auditing, or model feedback.

---

## 📋 Prerequisites

To run this system, ensure you have the following:

- An AWS account with access to API Gateway, Lambda, Fraud Detector, and DynamoDB services.
- AWS CLI configured or use of the AWS Management Console.
- Python 3.8+ installed (for developing and deploying the Lambda function).

---

## 🚀 Deployment Steps

### 1. DynamoDB Setup

- Create a DynamoDB table named: `FraudDetectionResults`.
- Set the **primary key** as `event_id` (String).

### 2. Amazon Fraud Detector Setup

- Create a **detector** (e.g., `transaction_detector`) with:
  - Defined **event type**, **variables** (e.g., `transaction_amount`, `ip_address`, etc.).
  - Detection **rules** such as:
    ```
    $transaction_model_insightscore > 900 → Predict as FRAUD
    ```
  - **Models and rules** published in a detector version.

### 3. Lambda Function Deployment

- Develop a Python Lambda function that:
  - Parses API input.
  - Invokes the **Fraud Detector `GetEventPrediction` API**.
  - Writes the result to the `FraudDetectionResults` DynamoDB table.
- Assign an **IAM Role** to the function with the following permissions:
  - `frauddetector:GetEventPrediction`
  - `dynamodb:PutItem`

### 4. API Gateway Configuration

- Create a **REST API** with a resource `/detect` and method `POST`.
- Link it to your Lambda function.
- Optionally enable **CORS**.
- Deploy the API to a stage (e.g., `prod`).

---

## 🧪 Example Workflow

1. Client sends a `POST` request to: Your API Gateway
   With JSON payload:
{
  "event_id": "abc123",
  "transaction_amount": 1000,
  "ip_address": "123.45.67.89",
  "account_id": "user_789"
}

2. Lambda triggers and invokes Fraud Detector.

3. Result is stored in DynamoDB:

{
  "event_id": "abc123",
  "fraud_label": "FRAUD",
  "insight_score": 947,
  "timestamp": "2025-07-15T12:34:56Z"
}

## END

