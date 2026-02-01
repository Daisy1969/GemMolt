# Walkthrough: GemMolt Assistant

The "GemMolt" Assistant has been successfully scaffolded. It is designed to be your central nervous system, connecting Gemini AI to your Code, Network, and Home.

## 1. Setup

### A. Install Dependencies

Open a terminal in `g:\My Drive\GemMolt` and run:

```bash
pip install -r requirements.txt
```

### B. Configuration

1. Open `.env.example` and rename it to `.env` (or copy it).
2. **Required**: Edit `.env` and add your `GOOGLE_API_KEY` from AI Studio.
3. **Optional**: Add your Home Assistant URL/Token if you want home control.
4. **Optional**: Add BlueBubbles URL if you have the iMessage server set up.

## 2. Running the Bot

Double-click `start.bat` or run:

```bash
python src/main.py
```

This will:

1. Connect to Gemini.
2. Start the iMessage Webhook listener on port 5000.
3. Give you a command prompt to chat with the bot.

## 3. Capabilities

### 🧠 The Brain

You can chat naturally. "How do I fix this python bug?" or "Plan a party."

### 💻 The Coder

The bot can see your projects in `G:\My Drive`.

* *Try*: "What projects do I have?"
* *Try*: "Read the readme for Project X."

### 📡 The Network

The bot can scan your local network.

* *Try*: "Scan the network."
* *Try*: "Who is on the wifi?"

### 🏠 The Home

(Requires Home Assistant)

* *Try*: "Turn on the living room lights."
* *Try*: "What's the temperature?"

## 4. Next Steps

* **iMessage**: Setup BlueBubbles on a Mac and point the webhook to `http://<YOUR_WINDOWS_IP>:5000/imessage`.
* **Expansion**: Edit `src/core/orchestrator.py` to add more complex logic or new tools.
