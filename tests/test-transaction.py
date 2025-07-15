import requests

url = "your-url"
payload={
    "entity_id": "trusted_user123",
    "ip_address": "10.0.0.15",
    "email_address": "trusted123@company.com",
    "transaction_amount": 79.99
}
response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())

#THIS IS JUST A TEST TRANSACTION YOU CAN TEST YOUR MODEL ON OTHERS
