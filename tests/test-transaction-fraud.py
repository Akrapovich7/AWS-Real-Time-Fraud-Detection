import requests

url = "your-url"
payload = {
    "entity_id": "suspicious_user666",
    "ip_address": "185.200.118.45",  # known risky IP range (e.g., from VPN or proxy)
    "email_address": "x99fraud@darkmail.ru",
    "transaction_amount": 5999.99  # abnormally high
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())

#THIS IS JUST A TEST TRANSACTION YOU CAN TEST YOUR MODEL ON OTHERS
