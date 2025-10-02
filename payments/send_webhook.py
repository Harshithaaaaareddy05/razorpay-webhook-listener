import hmac
import hashlib
import json
import requests
import os

SECRET_KEY = "test_secret"
ENDPOINT_URL = "http://localhost:8000/webhook/payments"

MOCK_PAYLOAD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mock_payloads'))
mock_files = [
    'payment_authorized.json',
    'payment_captured.json',
    'payment_failed.json'
]

for mock_file in mock_files:
    mock_path = os.path.join(MOCK_PAYLOAD_DIR, mock_file)
    print(f"\nSending payload from: {mock_file}")
    with open(mock_path, 'r') as f:
        payload = json.load(f)
    payload_json = json.dumps(payload)
    computed_signature = hmac.new(
        SECRET_KEY.encode(), payload_json.encode(), hashlib.sha256
    ).hexdigest()
    print(f"Computed Signature for curl: {computed_signature}")
    response = requests.post(
        ENDPOINT_URL,
        data=payload_json,
        headers={
            "Content-Type": "application/json",
            "X-Razorpay-Signature": computed_signature
        }
    )
    print("Status Code:", response.status_code)
    print("Response:", response.text)