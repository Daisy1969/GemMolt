# Task List: GemMolt Assistant (v2.0)

- [x] Phase 1: Planning & Design
  - [x] Create Design Doc (v2 Security & Autonomy)
  - [x] Create Implementation Plan (v2)
  - [x] User Review & Approval

- [ ] Phase 2: Foundation & Security (GCP & GitHub)
  - [ ] **GitHub Initialization**: Initialize git, add `.gitignore`, and push to remote.
  - [ ] **GCP Setup**: Verify `gcloud` CLI, authenticate, and enable APIs (Secret Manager, Pub/Sub).
  - [ ] **Secret Migration**: script to move `.env` variables to GCP Secret Manager.

- [ ] Phase 3: Core Refactoring (The Secure Agent)
  - [ ] Refactor `main.py` to use `GCPClient` instead of `.env`.
  - [ ] Implement `PubSubListener` to replace local Flask server.
  - [ ] Verify message reception from Cloud.

- [ ] Phase 4: Autonomy Engines
  - [ ] Implement `Scheduler` implementation for periodic tasks.
  - [ ] Implement `ShellClient` for system operations (with safety checks).
  - [ ] Implement `GitClient` for auto-backing up code.

- [ ] Phase 5: Verification & Handoff
  - [ ] Full End-to-End Test (iMessage -> PubSub -> Bot -> Action).
  - [ ] Update `walkthrough.md`.
