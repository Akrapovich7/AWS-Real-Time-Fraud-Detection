aws frauddetector create-model-version \
  --model-id transaction_model \
  --model-type ONLINE_FRAUD_INSIGHTS \
  --training-data-source TRAINING_DATA \
  --training-data-schema-labels fraud,legit
