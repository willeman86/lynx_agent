import voluptuous as vol
from homeassistant.core import HomeAssistant, SupportsResponse
from homeassistant.helpers.typing import ConfigType
from homeassistant.components.homeassistant.exposed_entities import async_should_expose

from .lynx_core import ask_lynx

DOMAIN = "lynx_agent"

# Action schema
ACTION_SCHEMA = vol.Schema({
    vol.Required("prompt"): str
})

# This tells Home Assistant what actions we expose
async def async_get_actions(hass: HomeAssistant) -> dict:
    return {
        "ask": {
            "name": "Ask LYNX Agent",
            "description": "Send a prompt to LYNX and get a reply",
            "fields": {
                "prompt": {
                    "name": "Prompt",
                    "description": "The question or command to ask the LYNX AI",
                    "required": True,
                    "example": "What’s the weather?",
                    "selector": {"text": {}},
                }
            },
            "supports_response": SupportsResponse.ONLY
        }
    }

# Action execution
async def async_call_action(hass: HomeAssistant, action: str, data: dict) -> dict:
    if action == "ask":
        prompt = data.get("prompt", "Who are you?")
        response = await hass.async_add_executor_job(ask_lynx, prompt, hass)
        return {"response": response}
    raise ValueError(f"Unknown action: {action}")

# Register actions
async def async_setup_actions(hass: HomeAssistant, config: ConfigType) -> bool:
    hass.data.setdefault(DOMAIN, {})
    return True
