import os
import requests
import json

class HAClient:
    def __init__(self):
        self.base_url = os.getenv("HOME_ASSISTANT_URL")
        self.token = os.getenv("HOME_ASSISTANT_TOKEN")
        
        if not self.base_url or not self.token:
            # We don't raise error here to allow the bot to start without HA, but functionality will be limited
            print("Warning: HOME_ASSISTANT_URL or HOME_ASSISTANT_TOKEN not set.")
            self.enabled = False
        else:
            self.headers = {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            }
            self.enabled = True

    def get_states(self):
        """Fetch all states from Home Assistant."""
        if not self.enabled: return "Home Assistant not configured."
        
        try:
            response = requests.get(f"{self.base_url}/api/states", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return f"Error fetching HA states: {e}"

    def call_service(self, domain, service, entity_id, data=None):
        """Call a service in Home Assistant (e.g., light.turn_on)."""
        if not self.enabled: return "Home Assistant not configured."
        
        payload = {"entity_id": entity_id}
        if data:
            payload.update(data)
            
        try:
            response = requests.post(
                f"{self.base_url}/api/services/{domain}/{service}",
                headers=self.headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return f"Error calling HA service: {e}"

    def get_state(self, entity_id):
        """Get the state of a specific entity."""
        if not self.enabled: return "Home Assistant not configured."
        
        try:
            response = requests.get(f"{self.base_url}/api/states/{entity_id}", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return f"Error getting state for {entity_id}: {e}"
