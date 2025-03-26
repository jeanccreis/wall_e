import google.generativeai as genai

class GeminiChat:
    def __init__(self, api_key: str, model_name: str = 'gemini-2.0-flash-lite'):
        self.api_key = api_key
        self.model_name = model_name
        self._configure()
        self.model = self._load_model()

    def _configure(self):
        genai.configure(api_key=self.api_key)

    def _load_model(self):
        return genai.GenerativeModel(self.model_name)

    def send_prompt(self, prompt: str):
        if not prompt.strip():
            raise ValueError("Prompt não pode estar vazio.")
        response = self.model.generate_content(prompt)
        return response.text


