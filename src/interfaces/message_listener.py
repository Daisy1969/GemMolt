from flask import Flask, request, jsonify
from ..core.orchestrator import Orchestrator
import threading

app = Flask(__name__)
bot = None # Will be initialized

@app.route('/imessage', methods=['POST'])
def handle_imessage():
    """Endpoint for BlueBubbles webhook."""
    data = request.json
    # Data structure depends on BlueBubbles webhook format
    # simplistic assumption: {'text': 'message', 'sender': 'handle'}
    sender = data.get('handle') or data.get('sender')
    text = data.get('text') or data.get('message')
    
    if text:
        print(f"Received iMessage from {sender}: {text}")
        # Process with bot
        if bot:
            response = bot.handle_input(f"Message from {sender}: {text}")
            # Here we would ideally call BlueBubbles API to reply
            # send_reply(sender, response)
            print(f"Bot generates reply: {response}")
            return jsonify({"status": "processed", "reply": response}), 200
    
    return jsonify({"status": "ignored"}), 200

def run_server(orchestrator_instance):
    global bot
    bot = orchestrator_instance
    # Run on port 5000 (default) or configurable
    app.run(port=5000, debug=False, use_reloader=False)

if __name__ == "__main__":
    # Test mode
    run_server(None)
