aws frauddetector create-variable \
  --name ip_address \
  --data-type STRING \
  --data-source EVENT \
  --default-value "unknown" \
  --variable-type IP

aws frauddetector create-variable \
  --name email_address \
  --data-type STRING \
  --data-source EVENT \
  --default-value "unknown" \
  --variable-type IP

aws frauddetector create-variable \
  --name transaction_amount \
  --data-type STRING \
  --data-source EVENT \
  --default-value "unknown" \
  --variable-type IP
