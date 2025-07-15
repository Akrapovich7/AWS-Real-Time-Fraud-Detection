aws frauddetector create-model \
  --model-id transaction_model \
  --model-type ONLINE_FRAUD_INSIGHTS \
  --event-type-name transaction_event \
  --input-data-config format=TEXT_CSV,s3Uri=s3://your-bucket/path.csv \
  --output-path s3://your-output-bucket/model-output \
  --role arn:aws:iam::your-account-id:role/yourFraudDetectorRole
