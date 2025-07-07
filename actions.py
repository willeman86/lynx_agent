import logging
from .lynx_core import ask_lynx

_LOGGER = logging.getLogger(__name__)
DOMAIN = "lynx_agent"

async def async_setup(hass, config):
    async def lynx_action_handler(call):
        prompt = call.data.get("prompt", "Who are you?")
        _LOGGER.debug(f"[LYNX] Received prompt: {prompt}")
        result = await hass.async_add_executor_job(ask_lynx, prompt)
        _LOGGER.info(f"[LYNX] Response: {result}")
        return {"response": result}

    hass.http.register_action(
        domain=DOMAIN,
        name="ask",
        handler=lynx_action_handler,
        schema={"prompt": str},
    )

    return True