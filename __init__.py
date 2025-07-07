"""Project LYNX AI Brain - Action Based"""

import logging
from .lynx_core import ask_lynx

_LOGGER = logging.getLogger(__name__)
DOMAIN = "lynx_agent"

async def async_setup(hass, config):
    # Load OpenAI key from secrets.yaml
    hass.data["lynx_agent_api_key"] = hass.secrets["lynx_agent_api_key"]

    async def lynx_action_handler(call):
        prompt = call.data.get("prompt", "Who are you?")
        _LOGGER.debug(f"[LYNX] Received prompt: {prompt}")
        result = await hass.async_add_executor_job(ask_lynx, prompt, hass)
        _LOGGER.info(f"[LYNX] Response: {result}")
        return {"response": result}

    # Register the Action (modern Home Assistant)
    hass.http.register_action(
        domain=DOMAIN,
        name="ask",
        handler=lynx_action_handler,
        schema={
            "prompt": str,
        },
    )

    return True
