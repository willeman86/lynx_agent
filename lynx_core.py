import openai
from homeassistant.core import HomeAssistant

def ask_lynx(prompt: str, hass: HomeAssistant = None) -> str:
    try:
        # Load the API key from secrets.yaml via hass config
        if hass is not None:
            api_key = hass.data["lynx_agent_api_key"]
        else:
            return "[LYNX Error] No access to hass object for secret loading."

        openai.api_key = api_key

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are LYNX, a smart home assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )

        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"[LYNX Error] {e}"
