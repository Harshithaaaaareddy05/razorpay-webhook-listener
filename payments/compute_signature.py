import hmac
import hashlib
import json
import os

SECRET_KEY = "test_secret"
MOCK_PAYLOAD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mock_payloads'))

# List of mock files to process
mock_files = [
    'payment_authorized.json',
    'payment_captured.json',
    'payment_failed.json'
]

# Loop through each file and compute the HMAC signature
for mock_file in mock_files:
    mock_path = os.path.join(MOCK_PAYLOAD_DIR, mock_file)
    
    with open(mock_path, 'r') as f:
        payload_json = f.read()

    print(f"\nProcessing {mock_file}...")
    print("Exact JSON string used for signature:")
    print(payload_json)
    
    # Compute HMAC signature
    computed_signature = hmac.new(
        SECRET_KEY.encode(), payload_json.encode(), hashlib.sha256
    ).hexdigest()
    
    # Print the computed signature for curl
    print(f"Computed Signature for {mock_file} (for curl): {computed_signature}")