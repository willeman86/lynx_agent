import openai

def ask_lynx(prompt: str, hass) -> str:
    api_key = hass.data.get("lynx_agent_api_key")

    if not api_key:
        return "API key not found. Please check secrets.yaml."

    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are LYNX, a smart home assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message["content"].strip()

    except Exception as e:
        return f"Error talking to LYNX: {e}"
