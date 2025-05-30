# Sentivisor

An intelligent emotional analysis agent that provides real-time insights into participant emotions during video conference calls. Built on the Agno framework, Sentivisor helps managers understand team dynamics and identify potential concerns through advanced AI-powered emotion detection.

## 🎯 Features

- **Real-time Emotion Analysis**
  - Facial expression analysis using DeepFace
  - Voice tone and stress detection
  - Text sentiment analysis from speech transcripts
  - Multi-modal emotional state tracking

- **Meeting Insights**
  - Live emotional state monitoring
  - Engagement level tracking
  - Risk indicator detection
  - Post-meeting emotional reports

- **Privacy-Focused**
  - Secure data handling
  - Configurable privacy settings
  - Private manager alerts
  - No raw data storage

## 📦 Installation

### Prerequisites
- Python 3.8+
- Docker (optional, for containerized deployment)
- pip or uv package manager (uv is recommended)
- CUDA-capable GPU (recommended for real-time analysis)

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sentivisor.git
cd sentivisor
```

2. Create a virtual environment and install dependencies:
```bash
uv sync
```

3. Add your API keys to the `.env` file:
```bash
OPENAI_API_KEY=your_openai_api_key
AGNO_API_KEY=your_agno_api_key
```

4. Start the application:
```bash
uvicorn app:app --reload
```

5. Open Agno Playground:
- Ensure your AGNO_API_KEY is set in the `.env` file
- Run main.py to start the Playground
- Visit https://app.agno.com/playground/agents
- Select localhost:7777 as the endpoint

### Docker Deployment
```bash
docker-compose up --build
```

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

- Thanks to [agno](https://github.com/agno-agi/agno) for the incredible framework
- Built with [DeepFace](https://github.com/serengil/deepface), [Whisper](https://github.com/openai/whisper), and [HuggingFace](https://huggingface.co/) models

## 📞 Contact

For questions or support, please open an issue in the repository.
