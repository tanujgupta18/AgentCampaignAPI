from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Agent, Campaign, CampaignResult

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'voice_id', 'updated')
    search_fields = ('name', 'language', 'voice_id')
    list_filter = ('language',)


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'campaign_type', 'phone_number', 'status', 'agent')
    search_fields = ('name', 'phone_number', 'status')
    list_filter = ('campaign_type', 'status', 'agent')


@admin.register(CampaignResult)
class CampaignResultAdmin(admin.ModelAdmin):
    list_display = ('name', 'result_type', 'phone', 'outcome', 'cost', 'call_duration', 'campaign')
    search_fields = ('name', 'phone', 'outcome', 'campaign__name')
    list_filter = ('outcome', 'campaign')
