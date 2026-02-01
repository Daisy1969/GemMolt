# Implementation Plan: GemMolt Security & Autonomy Update

# Goal Description

Upgrade GemMolt from a simple CLI bot to a Secure, Autonomous Agent (v2.0).
Key changes: **Google Cloud Security** (Secrets/PubSub) and **Autonomous Capabilities** (Task Scheduler).

## User Review Required
>
> [!IMPORTANT]
> **Google Cloud Setup**: This plan requires creating a GCP Project. You will need to enable APIs (Secret Manager, Pub/Sub) and download a Service Account JSON key.

> [!WARNING]
> **Autonomy Risks**: The bot will be given shell access. We will implement a "Safe Mode" where it asks for confirmation before running shell commands.

## Proposed Changes

### Phase 1: Foundation (GitHub & GCP)

* **GitHub**: Initialize `git` repo, create `.gitignore` (exclude secrets), and link to User's GitHub.
* **GCP Project**: Setup `gemmolt-secure` project (User action required if not automated).
* **Secret Manager**: Upload API Keys to GCP Secret Manager.
* **Service Account**: Generate `service-account.json` for the local bot.
* **Code Update**: Modify `main.py` to authenticate via Google Auth and fetch secrets from `google-cloud-secret-manager` instead of `.env`.

### Phase 2: Secure Communication (The "No-Port" Policy)

* **Pub/Sub Setup**: Create `gemmolt-commands` topic and subscription.
* **Ingest Function**: Deploy a simple Cloud Function (Python) to receive Webhooks (from BlueBubbles) and publish to Pub/Sub.
* **Bot Update**: Replace Flask Server with `google-cloud-pubsub` subscriber.
  * *Benefit*: Bot works behind any firewall without port forwarding.

### Phase 3: Autonomy & Advanced Tools

* **Scheduler**: Implement `schedule` library loop for periodic tasks.
* **Shell Tool**: Create `ShellClient` class for executing generic commands (`subprocess`).
* **Web Tool**: (Optional) Integrate specialized browsing capability if requested.

### Phase 4: Migration

[MODIFY] [main.py](file:///g:/My%20Drive/GemMolt/src/main.py) - Update to init GCP clients.
[NEW] [gcp_client.py](file:///g:/My%20Drive/GemMolt/src/core/gcp_client.py) - Handles Secrets/PubSub.
[DELETE] [message_listener.py] - Flask server is deprecated in favor of Pub/Sub.

## Verification Plan

### Automated

* **Secret Fetch Test**: Script verifies it can retrieve a dummy secret from GCP.
* **Pub/Sub Test**: Publish a message manually in GCP Console -> Verify Bot prints it.

### Manual

* **Remote Command**: Send iMessage -> Cloud Function -> Pub/Sub -> Bot Action.
* **Autonomy**: Set a reminder "Ping me in 1 minute" and verify execution.
