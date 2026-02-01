# GemMolt Assistant - Design Document (v2.0)

## 1. Executive Summary

GemMolt is a "Master Coding and Manager Assistant" designed to be the autonomous, secure central nervous system of your home and digital workspace. Inspired by **OpenClaw.ai**, it features autonomous task execution, deep system integration, and proactive capabilities. Security is paramount, leveraging **Google Cloud Platform (GCP)** for identity and secret management.

## 2. System Architecture

The system uses a **Hybrid Cloud/Local** architecture to maximize security and capability.

### 2.1 Core Components

* **The Brain (Gemini 3 Pro)**: High-level reasoning and decision making.
* **The Agent (Local Python Bot)**: Runs on your Windows machine.
  * *Autonomy Engine*: A scheduler/job queue for proactive tasks.
  * *System Interface*: Shell access, File I/O, Web Browser control (Selenium/Playwright).
* **The Cloud Shield (Google Cloud)**:
  * **Secret Manager**: securely stores API Keys (Gemini, HA Token). **No local plaintext keys.**
  * **Pub/Sub**: Acts as the secure message broker. The local bot *pulls* messages; it does **not** listen on open ports.
* **The Hub (Home Assistant)**: Device abstraction layer.

### 2.2 Secure Data Flow (The "Pub/Sub" Model)

1. **Input**: User sends iMessage "Fix the house".
2. **Ingest**: BlueBubbles (or other webhook source) sends payload to a **Google Cloud Function** key-protected endpoint.
3. **Queue**: Cloud Function publishes message to **Cloud Pub/Sub**.
4. **Process**: Local GemMolt Bot (running behind NAT, no open ports) pulls the message from Pub/Sub via a **Service Account**.
5. **Action**: Bot executes code/HA commands.
6. **Reply**: Bot sends response back via API.

## 3. Module Breakdown

### 3.1 Autonomy & Proactive Module (OpenClaw Parity)

* **Task Queue**: "Check for library updates every morning." (Proactive Code Maintenance).
* **Observer**: "Watch my network for new devices." (Security Monitor).

### 3.2 Advanced Coding Module

* **Read/Write**: Full CRUD on the filesystem ( `G:\My Drive\GemMolt` ).
* **Terminal**: Ability to execute shell commands (e.g., `git push`, `npm install`).
* **Safety**: "Human-in-the-loop" mode for destructive commands (e.g., `rm -rf`).

### 3.3 GitHub Integration (Backup & Copilot)

* **Version Control**: The bot is git-aware. It acts as its own maintainer.
  * `git init` / `git push`: Ensures `g:\My Drive\GemMolt` is backed up to GitHub.
  * **Copilot Synergy**: Since the user has Copilot CLI, the bot can use `gh copilot suggest` (if available) to generate shell commands for complex tasks.

### 3.4 Security Implementation (GCP)

* **Service Account**: The bot runs as `gemmolt-agent@<project>.iam.gserviceaccount.com`.
* **IAM Roles**:
  * `roles/secretmanager.secretAccessor` (Read API keys).
  * `roles/pubsub.subscriber` (Read user messages).
* **Secret Manager**: Stores `GOOGLE_API_KEY`, `HA_TOKEN`, `BLUEBUBBLES_URL`.

## 4. Requirements

* **Local Hardware**: Windows PC (Always on).
* **Cloud**: Active Google Cloud Project with Billing (Free tier likely sufficient for low volume).
* **Home**: Home Assistant instance.
