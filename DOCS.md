# 1.Webhook Receiver Endpoint
### Endpoint:
POST /webhook/payments
#### Purpose:
Receives webhook events from payment providers and stores them in the database after verifying authenticity.
#### Parameters:
Headers:
Header	               Description
Content-Type:          application/json	(Required)
X-Razorpay-Signature:	 HMAC signature to verify authenticity (simulated)

### Request Body (Example - payment_authorized.json):
{
    "event": "payment.authorized",
    "payload": {
      "payment": {
        "entity": {
          "id": "pay_014",
          "status": "authorized",
          "amount": 5000,
          "currency": "INR"
        }
      }
    },
    "created_at": 1751889865,
    "id": "evt_auth_014"
}
### Behavior:
#### Validates the signature using the shared secret test_secret.
##### Rejects invalid requests:
Missing signature → 403 Forbidden
Invalid signature → 403 Forbidden
Invalid JSON → 400 Bad Request
Stores event in the database if valid.
Ensures idempotency: duplicate event_id is ignored.

### Response Example (Success Example):
{
  "results": [
    {
      "id": "evt_auth_014",
      "message": "Event processed successfully",
      "status": 200
    }
  ]
}

### Response Example(Duplicate Example):
{
  "results": [
    {
      "id": "evt_auth_014",
      "message": "Duplicate event",
      "status": 409
    }
  ]
}



# 2. Payment Event Query Endpoint
### Endpoint: 
GET /payments/{payment_id}/events
#### Purpose:
Fetch all historical events for a specific payment ID, sorted chronologically.
#### Parameters:
Parameter	   Description
payment_id	The ID of the payment to fetch events for

### Response Example
[
  {
    "event_type": "payment.authorized",
    "received_at": "2025-10-01T16:38:39.306804+00:00"
  },
  {
    "event_type": "payment.captured",
    "received_at": "2025-10-01T16:38:39.326221+00:00"
  }
]

# 3. Mock Payloads
You can find sample payloads in the mock_payloads/ folder:

# Testing with curl:
## Send webhook event
curl -X POST http://127.0.0.1:8000/webhook/payments \
  -H "Content-Type: application/json" \
  -H "X-Razorpay-Signature: TEST_SIGNATURE" \
  -d @mock_payloads/payment_authorized.json

## Fetch events for a payment
curl http://127.0.0.1:8000/payments/pay_014/events
