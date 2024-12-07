from rest_framework import serializers
from .models import Agent, Campaign, CampaignResult

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id', 'name', 'campaign_type', 'phone_number', 'status', 'agent']


class CampaignResultSerializer(serializers.ModelSerializer):
    campaign = CampaignSerializer()

    class Meta:
        model = CampaignResult
        fields = '__all__'

    def create(self, validated_data):
        # Extract the campaign data from validated data
        campaign_data = validated_data.pop('campaign')

        # Create the campaign first
        campaign = Campaign.objects.create(**campaign_data)

        # Now create the campaign result and link it to the created campaign
        campaign_result = CampaignResult.objects.create(campaign=campaign, **validated_data)

        return campaign_result
