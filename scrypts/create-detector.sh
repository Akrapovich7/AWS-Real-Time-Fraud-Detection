aws frauddetector create-detector-version \
  --detector-id transaction_detector \
  --rules '[{"detectorRuleId":"high_risk","expression":"$transaction_model_insightscore > 900","outcomes":["fraud"]}]' \
  --model-versions '[{"modelId":"transaction_model","modelType":"ONLINE_FRAUD_INSIGHTS","modelVersionNumber":"1.0"}]'
