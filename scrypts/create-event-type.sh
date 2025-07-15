aws frauddetector create-event-type \
  --name transaction_event \
  --event-variables name=ip_address,dataType=STRING,variableType=IP \
  name=email_address,dataType=STRING,variableType=EMAIL_ADDRESS \
  name=transaction_amount,dataType=FLOAT,variableType=NUMERIC \
  --entity-types transaction_entity \
  --labels label=legit,label=fraud
