from fastapi import APIRouter
from core.config import Settings
from fastapi.responses import JSONResponse

router = APIRouter()

integration_json = {
  "data": {
    "date": {
      "created_at": "2025-02-18",
      "updated_at": "2025-02-18"
    },
    "descriptions": {
      "app_name": "1st integration",
      "app_description": "Simple ci/cd notification service",
      "app_logo": "http://100.25.191.235",
      "app_url": "http://100.25.191.235",
      "background_color": "#fff"
    },
    "is_active": True,
    "integration_type": "modifier",
    "key_features": [
      "update",
      "slack notification"
    ],
    "author": "Victor",
    "settings": [
      {
        "label": "slack-channel",
        "type": "text",
        "required": True,
        "default": "#Devops Alert"
      },
      {
        "label": "Notifications",
        "type": "dropdown",
        "required": True,
        "default": "immediate",
        "options": [
          "immediate",
          "1min",
          "5min"
        ]
      },
      {
        "label": "event type",
        "type": "dropdown",
        "required": True,
        "default": "ci-notifications",
        "options": [
          "ci-notifications",
          "cd-notifications"
        ]
      },
      {
        "label": "include logs",
        "type": "checkbox",
        "required": True,
        "default": "true"
      }
    ],
    "target_url": "https://hooks.slack.com/services/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",
    "tick_url": "http://100.25.191.235/telex-webhook"
  }
}

@router.get("/integration-config")
async def get_integration_json():
    return JSONResponse(content=integration_json)