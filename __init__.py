import logging
from .lynx_core import ask_lynx

_LOGGER = logging.getLogger(__name__)
DOMAIN = "lynx_agent"

async def async_setup(hass, config):
    async def handle_ask_lynx(call):
        prompt = call.data.get("prompt", "Who are you?")
        result = await hass.async_add_executor_job(ask_lynx, prompt)
        _LOGGER.info("LYNX says: %s", result)

    hass.services.async_register(DOMAIN, "ask", handle_ask_lynx)
    return True
