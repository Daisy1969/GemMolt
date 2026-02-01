import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GeminiClient:
    def __init__(self, model_name="gemini-pro"):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)
        self.chat = self.model.start_chat(history=[])

    def send_message(self, message):
        """Sends a message to Gemini and returns the response."""
        try:
            response = self.chat.send_message(message)
            return response.text
        except Exception as e:
            return f"Error communicating with Gemini: {e}"

    def set_system_instruction(self, instruction):
        """
        Note: The current google-generativeai SDK for some models might handle system instructions differently 
        or via initial prompt context. This is a placeholder for model configuration.
        """
        # For gemini-pro, system instructions are often passed as part of the initial context logic 
        # or config if supported by the specific SDK version/endpoint.
        pass
