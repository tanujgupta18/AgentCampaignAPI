# AgentCampaignAPI

AgentCampaignAPI is a Django-based REST API built using **Django Rest Framework (DRF)** for managing agents, campaigns, and campaign results. The API allows users to:

- Create, read, update, and delete (CRUD) agents and campaigns.
- Track campaign results such as call duration, outcome, cost, and more.
- Use built-in pagination for listing agents, campaigns, and results.

## Features

- **Agent Management**: Create, update, and delete agents.
- **Campaign Management**: Create, update, and delete campaigns, assign agents, and track campaign status.
- **Campaign Results**: Track the outcome of each campaign, including call duration, outcome, cost, and a transcription of the call.
- **Pagination**: Support for pagination on listing endpoints.

## API Endpoints

The following are the available API endpoints for interacting with the system:

### Agents

- **GET** `/api/agents/` - List all agents (paginated).
- **POST** `/api/agents/` - Create a new agent.
- **GET** `/api/agents/{id}/` - Retrieve a specific agent by ID.
- **PUT** `/api/agents/{id}/` - Update an existing agent.
- **DELETE** `/api/agents/{id}/` - Delete an agent.

### Campaigns

- **GET** `/api/campaigns/` - List all campaigns (paginated).
- **POST** `/api/campaigns/` - Create a new campaign.
- **GET** `/api/campaigns/{id}/` - Retrieve a specific campaign by ID.
- **PUT** `/api/campaigns/{id}/` - Update an existing campaign.
- **DELETE** `/api/campaigns/{id}/` - Delete a campaign.

### Campaign Results

- **GET** `/api/campaign-results/` - List all campaign results (paginated).
- **POST** `/api/campaign-results/` - Create a new campaign result.
- **GET** `/api/campaign-results/{id}/` - Retrieve a specific campaign result by ID.
- **PUT** `/api/campaign-results/{id}/` - Update an existing campaign result.
- **DELETE** `/api/campaign-results/{id}/` - Delete a campaign result.

## Deployed Link

The API is deployed and accessible at:  
[https://agentcampaignapi.onrender.com](https://agentcampaignapi.onrender.com)

## API Usage

Once the server is running, you can interact with the API using tools like **Postman**, **cURL**, or the **Django browsable API**. Below are examples of the common requests you can make.

### Create an Agent (POST)

**Endpoint**: `/api/agents/`

```json
{
  "name": "Jose Alinson",
  "language": "English",
  "voice_id": "voice_123"
}
```

### Create a Campaign (POST)

**Endpoint**: `/api/campaigns/`

```json
{
  "name": "Campaign Alpha",
  "campaign_type": "Outbound",
  "phone_number": "123-456-7890",
  "status": "Running",
  "agent": 1 // ID of the agent to assign to the campaign
}
```

### Create a Campaign Result (POST)

**Endpoint**: `/api/campaign-results/`

```json
{
  "name": "Result 1",
  "result_type": "Success",
  "phone": "123-456-7890",
  "cost": 25.5,
  "outcome": "Success",
  "call_duration": 300.5,
  "recording": "http://someurl.com/recording.mp3",
  "summary": "Call was successful",
  "transcription": "Hello, this is a transcript of the call",
  "campaign": 1 // ID of the campaign
}
```
