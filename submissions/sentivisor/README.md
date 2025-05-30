# Agent App

A high-performance, scalable framework for implementing and deploying AI agents. Built with simplicity and speed in mind, this project provides a robust foundation for creating and managing AI agents in production environments.

## 🚀 Features

- Fast and efficient agent implementation
- Scalable architecture design
- RESTful API interface
- Docker support for easy deployment
- Modular and extensible design

## 📦 Installation

### Prerequisites
- Python 3.8+
- Docker (optional, for containerized deployment)
- pip or uv package manager (uv is recommended)

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/agent-app.git
cd agent-app
```

2. Create a virtual environment and install dependencies (uv is recommended):
```bash
uv sync
```

3. Add your API keys to the `.env` file:
```bash
OPENAI_API_KEY=your_openai_api_key
AGNO_API_KEY=your_agno_api_key
```

4. Start the application (Optional, for local testing):
```bash
uvicorn app:app --reload
```

5. Open Agno Playground (UI):
- Ensure your AGNO_API_KEY is set in the `.env` file
- Run main.py to start the Playground
- Visit https://app.agno.com/playground/agents to see the Playground
- Select localhost:7777 as the endpoint

### Docker Deployment
```bash
docker-compose up --build
```

## 🛠️ Usage

### Basic Agent Creation
```python
from agno.agent import Agent

# Create a new agent
agent = Agent(name="my_agent")
agent.run()
```

### API Endpoints
- `POST v1/answer` - Answer a question

## 🏗️ Architecture

The project follows a modular architecture:
- `src/agents/` - Core agent implementations
- `src/tools/` - Reusable tools for agents
- `src/tasks/` - Task management system
- `src/models/` - Data models and schemas
- `api/` - REST API implementation
- `config/` - Configuration files

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](docs/CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to [agno](https://github.com/agno-agi/agno) for the incridle framework
- Inspired by the need for fast and scalable agent implementations and deployment

## 📞 Contact

For questions or support, please open an issue in the repository.
