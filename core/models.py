from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    voice_id = models.CharField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    INBOUND = 'Inbound'
    OUTBOUND = 'Outbound'

    CAMPAIGN_TYPE_CHOICES = [
        (INBOUND, 'Inbound'),
        (OUTBOUND, 'Outbound'),
    ]

    RUNNING = 'Running'
    PAUSED = 'Paused'
    COMPLETED = 'Completed'

    CAMPAIGN_STATUS_CHOICES = [
        (RUNNING, 'Running'),
        (PAUSED, 'Paused'),
        (COMPLETED, 'Completed'),
    ]

    name = models.CharField(max_length=255)
    campaign_type = models.CharField(max_length=10, choices=CAMPAIGN_TYPE_CHOICES)
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=CAMPAIGN_STATUS_CHOICES)
    agent = models.ForeignKey(Agent, related_name="campaigns", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CampaignResult(models.Model):
    SUCCESS = 'Success'
    FAILURE = 'Failure'

    OUTCOME_CHOICES = [
        (SUCCESS, 'Success'),
        (FAILURE, 'Failure'),
    ]

    name = models.CharField(max_length=255)
    result_type = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    cost = models.FloatField()
    outcome = models.CharField(max_length=10, choices=OUTCOME_CHOICES)
    call_duration = models.FloatField()
    recording = models.URLField(max_length=255)
    summary = models.TextField()
    transcription = models.TextField()
    campaign = models.ForeignKey(Campaign, related_name="results", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
