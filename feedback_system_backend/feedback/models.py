from django.db import models
from users.models import User

class Feedback(models.Model):
    SENTIMENT_CHOICES = [
        ('positive', 'Positive'),
        ('neutral', 'Neutral'),
        ('negative', 'Negative'),
    ]
    employee = models.ForeignKey(User, related_name="feedback_received", on_delete=models.CASCADE)
    manager = models.ForeignKey(User, related_name="feedback_given", on_delete=models.CASCADE)
    strengths = models.TextField()
    areas_to_improve = models.TextField()
    sentiment = models.CharField(max_length=10, choices=SENTIMENT_CHOICES)
    acknowledged = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
