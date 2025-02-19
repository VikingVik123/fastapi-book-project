from fastapi import APIRouter
from core.config import settings
from fastapi.responses import JSONResponse

router = APIRouter()

integration_json = {
  "data": {
    "date": {
      "created_at": "2025-02-19",
      "updated_at": "2025-02-19"
    },
    "descriptions": {
      "app_name": "Test",
      "app_description": "simple ci cd slack notification app",
      "app_logo": "http://100.25.191.235",
      "app_url": "http://100.25.191.235",
      "background_color": "#fff"
    },
    "is_active": True,
    "integration_type": "modifier",
    "key_features": [
      "realtime updates",
      "slack notification"
    ],
    "author": "Victor",
    "settings": [
      {
        "label": "slack-channel",
        "type": "text",
        "required": True,
        "default": "#Devops"
      },
      {
        "label": "Time interval",
        "type": "dropdown",
        "required": True,
        "default": "immediate",
        "options": [
          "immediate",
          "1min",
          "2min"
        ]
      },
      {
        "label": "event type",
        "type": "dropdown",
        "required": True,
        "default": "ci pipeline",
        "options": [
          "ci pipeline",
          "cd pipeline",
          "deployment error"
        ]
      },
      {
        "label": "include logs",
        "type": "checkbox",
        "required": True,
        "default": "True"
      },
      {
        "label": "message",
        "type": "text",
        "required": True,
        "default": "ci/cd-notifications"
      }
    ],
    "target_url": settings.SLACK_WEBHOOK_URL,
    "tick_url": settings.TICK_URL
  }
}

@router.get("/integration-config")
async def get_integration_json():
    return JSONResponse(content=integration_json)