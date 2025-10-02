import hmac
import hashlib
import json
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from .models import PaymentEvent
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings



# The secret used for HMAC
SECRET_KEY = "test_secret"


def verify_signature(payload, received_signature):
    computed_signature = hmac.new(
        SECRET_KEY.encode(), payload.encode(), hashlib.sha256
    ).hexdigest()
    
    # Log the signature comparison for debugging
    print("Received Signature:", received_signature)
    print("Computed Signature:", computed_signature)
    
    return computed_signature == received_signature

@csrf_exempt
def webhook_receiver(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid HTTP method")

    # Get the signature header
    signature = request.headers.get('X-Razorpay-Signature')

    if not signature:
        return HttpResponseForbidden("Missing signature")

    try:
        # Read and parse the request payload
        payload = request.body.decode('utf-8')
        data = json.loads(payload)
    except Exception:
        return HttpResponseBadRequest("Invalid JSON")

    # Log for debugging
    print("Received Payload:", payload)

    # Verify the signature
    if not verify_signature(payload, signature):
        print("Invalid signature detected.")
        return HttpResponseForbidden("Invalid signature")

    # If data is a list, process each event; if it's a dict, process as single event
    events = data if isinstance(data, list) else [data]
    results = []
    for event in events:
        try:
            event_id = event.get('id')
            payment_id = event['payload']['payment']['entity']['id']
            event_type = event['event']
            status = event['payload']['payment']['entity']['status']
            amount = event['payload']['payment']['entity']['amount']
            currency = event['payload']['payment']['entity']['currency']
            created_at = timezone.datetime.utcfromtimestamp(event['created_at'])

            # Check for idempotency (prevent duplicate event_id)
            if PaymentEvent.objects.filter(event_id=event_id).exists():
                results.append({"id": event_id, "message": "Duplicate event", "status": 409})
                continue

            # Save the event to the database
            PaymentEvent.objects.create(
                event_id=event_id,
                payment_id=payment_id,
                event_type=event_type,
                status=status,
                amount=amount,
                currency=currency,
                created_at=created_at,
                raw_payload=event
            )
            results.append({"id": event_id, "message": "Event processed successfully", "status": 200})
        except Exception as e:
            results.append({"id": event.get('id', None), "message": f"Error: {str(e)}", "status": 400})

    return JsonResponse({"results": results}, status=200)



from django.http import JsonResponse
from .models import PaymentEvent
from django.views.decorators.csrf import csrf_exempt

def get_payment_events(request, payment_id):
    events = PaymentEvent.objects.filter(payment_id=payment_id).order_by('created_at')

    event_list = [{
        "event_type": event.event_type,
        "received_at": event.received_at.isoformat()
    } for event in events]

    return JsonResponse(event_list, safe=False)
