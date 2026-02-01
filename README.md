# GemMolt - Master Coding and Manager Assistant

![GemMolt Logo](https://img.shields.io/badge/GemMolt-v0.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8+-blue)

**GemMolt** is an autonomous, secure central nervous system designed to be your master coding and manager assistant for your home and digital workspace. Inspired by **OpenClaw.ai**, GemMolt features autonomous task execution, deep system integration, and proactive capabilities with security as a paramount concern.

## 🌟 Features

### Core Capabilities
- **Autonomous Task Execution**: Intelligent planning and execution of complex tasks
- **Deep System Integration**: Seamless integration with system resources and services
- **Proactive Monitoring**: Continuous monitoring with proactive response capabilities
- **Security First**: Leverages Google Cloud Platform (GCP) for identity and secret management

### Key Components

1. **Security Manager**
   - GCP IAM integration for identity management
   - GCP Secret Manager for secure credential handling
   - Permission verification and access control
   - Encrypted secret storage and retrieval

2. **Task Executor**
   - Autonomous task planning and execution
   - Intelligent error handling and recovery
   - Task history and monitoring
   - Context-aware execution

3. **System Integration**
   - System resource monitoring
   - File system operations
   - Process management
   - Network integration

4. **Proactive Monitor**
   - Continuous system health monitoring
   - Event detection and alerting
   - Proactive response capabilities
   - Event history and analysis

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Daisy1969/GemMolt.git
cd GemMolt

# Install dependencies
pip install -r requirements.txt

# Install GemMolt
pip install -e .
```

### Basic Usage

```python
from gemmolt import GemMolt

# Initialize GemMolt with configuration
config = {
    'security': {
        'gcp_project_id': 'your-gcp-project-id',
        'use_gcp': True
    },
    'tasks': {
        'max_history': 100
    },
    'monitoring': {
        'max_history': 1000
    }
}

# Create and start GemMolt
gemmolt = GemMolt(config)
gemmolt.start()

# Execute a task
result = gemmolt.execute_task(
    "Analyze system health and report status",
    context={"priority": "high"}
)

print(result)

# Get system status
status = gemmolt.get_status()
print(status)

# Stop GemMolt
gemmolt.stop()
```

## 📋 Configuration

### GCP Setup

GemMolt uses Google Cloud Platform for secure identity and secret management. To configure GCP:

1. **Create a GCP Project**
   ```bash
   gcloud projects create your-gemmolt-project
   ```

2. **Enable Required APIs**
   ```bash
   gcloud services enable secretmanager.googleapis.com
   gcloud services enable iam.googleapis.com
   ```

3. **Set Up Authentication**
   ```bash
   gcloud auth application-default login
   ```

4. **Configure GemMolt**
   
   Create a `config.yaml` file:
   ```yaml
   security:
     gcp_project_id: "your-gcp-project-id"
     use_gcp: true
   
   tasks:
     max_history: 100
   
   monitoring:
     max_history: 1000
   
   integration:
     enable_system_commands: false
   ```

### Environment Variables

```bash
export GEMMOLT_GCP_PROJECT_ID="your-gcp-project-id"
export GEMMOLT_CONFIG_PATH="/path/to/config.yaml"
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
```

## 🏗️ Architecture

GemMolt follows a modular architecture:

```
┌─────────────────────────────────────────────┐
│            GemMolt Core                     │
│  (Central Nervous System)                   │
└─────────────────────────────────────────────┘
           │         │         │         │
     ┌─────┴──┐ ┌───┴───┐ ┌───┴────┐ ┌──┴────────┐
     │Security│ │ Tasks │ │Integration│ │Monitoring│
     │Manager │ │Executor│ │          │ │          │
     └────────┘ └────────┘ └──────────┘ └──────────┘
         │                                     │
    ┌────┴────┐                           ┌───┴───┐
    │   GCP   │                           │Events │
    │IAM/SM   │                           │Alerts │
    └─────────┘                           └───────┘
```

## 🔐 Security

Security is paramount in GemMolt:

- **GCP IAM Integration**: All operations are authenticated using GCP Identity and Access Management
- **Secret Management**: Credentials and sensitive data are stored in GCP Secret Manager
- **Least Privilege**: Components operate with minimum required permissions
- **Audit Logging**: All security-sensitive operations are logged
- **Encrypted Communication**: All external communications are encrypted

### Best Practices

1. Always use GCP Secret Manager for storing credentials
2. Regularly rotate secrets and access keys
3. Use service accounts with minimal required permissions
4. Enable audit logging for all GCP operations
5. Review and update security policies regularly

## 📚 Documentation

- [Installation Guide](docs/installation.md)
- [Configuration Guide](docs/configuration.md)
- [API Reference](docs/api_reference.md)
- [Security Guide](docs/security.md)
- [Examples](examples/)

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/

# Run specific test suite
python -m pytest tests/test_core.py

# Run with coverage
python -m pytest --cov=gemmolt tests/
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by **OpenClaw.ai**
- Built with security and automation in mind
- Powered by Google Cloud Platform

## 📞 Support

- Documentation: [https://github.com/Daisy1969/GemMolt/docs](https://github.com/Daisy1969/GemMolt/docs)
- Issues: [https://github.com/Daisy1969/GemMolt/issues](https://github.com/Daisy1969/GemMolt/issues)
- Discussions: [https://github.com/Daisy1969/GemMolt/discussions](https://github.com/Daisy1969/GemMolt/discussions)

## 🗺️ Roadmap

- [ ] Enhanced AI-powered task planning
- [ ] Extended system integration capabilities
- [ ] Real-time collaboration features
- [ ] Mobile app integration
- [ ] Advanced analytics and reporting
- [ ] Plugin ecosystem

---

**Built with ❤️ by the GemMolt Team**