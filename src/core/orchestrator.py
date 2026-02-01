import json
from .gemini_client import GeminiClient
from .project_manager import ProjectManager
from .network_scanner import NetworkScanner
from .ha_client import HAClient

class Orchestrator:
    def __init__(self, root_path="G:/My Drive"):
        self.gemini = GeminiClient()
        self.project_manager = ProjectManager(root_path)
        self.network_scanner = NetworkScanner()
        self.ha_client = HAClient()
        
        # Initialize the system with knowledge of its tools
        self._initialize_system_prompt()

    def _initialize_system_prompt(self):
        system_prompt = """
        You are GemMolt, a master coding and home automation assistant.
        You have access to the following capabilities:
        1. **Project Management**: You can list projects and read their summaries.
        2. **Network Scanning**: You can scan the local network for devices.
        3. **Home Automation**: You can control lights, climate, and read sensor data via Home Assistant.
        
        When asked to perform an action, you should act as a smart agent. 
        If you need to know about the environment, ask the user to run a scan or (if automated) say you are scanning.
        
        (Note: In this v0.1 implementation, you are text-based, but your backend has these python classes ready.)
        """
        # In a real implementation we would send this as the first history item
        self.gemini.chat.history.append({"role": "user", "parts": [system_prompt]})
        self.gemini.chat.history.append({"role": "model", "parts": ["Understood. I am ready to assist via Home Assistant, Network operations, and Code management."]})

    def handle_input(self, user_input):
        # Here we could add logic to intercept specific commands like "/scan" or "/deploy"
        # For now, we pass everything to Gemini, but we could inject context if needed.
        
        # Simple keywords context injection (POC)
        context = ""
        if "network" in user_input.lower() or "scan" in user_input.lower():
            devices = self.network_scanner.scan_network()
            context += f"\n[System Context] Network Scan Results: {devices}\n"
        
        if "project" in user_input.lower():
            projects = self.project_manager.list_projects()
            context += f"\n[System Context] Projects in Drive: {projects}\n"

        if "light" in user_input.lower() or "temperature" in user_input.lower():
            states = self.ha_client.get_states()
            # This might be too huge, so maybe just listing entity IDs or filtering
            if isinstance(states, list):
                # Filter for lights/climate to save context winow
                relevant_states = [s['entity_id'] for s in states if 'light' in s['entity_id'] or 'climate' in s['entity_id']]
                context += f"\n[System Context] Home Assistant Relevant Entities: {relevant_states}\n"

        full_message = user_input + context
        return self.gemini.send_message(full_message)
