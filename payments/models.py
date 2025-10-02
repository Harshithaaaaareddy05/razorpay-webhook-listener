from django.db import models

class PaymentEvent(models.Model):
    event_id = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    amount = models.IntegerField()
    currency = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    received_at = models.DateTimeField(auto_now_add=True)
    raw_payload = models.JSONField(null=True, blank=True)

    class Meta:
        unique_together = ('event_id', 'payment_id')

    def __str__(self):
        return f"{self.event_type} for {self.payment_id}"
