# AgentSender

AgentSender is an AI-powered autonomous agent that helps with cold email outreach. It can break down high-level goals into actionable steps, research leads, generate personalized emails, and track the entire process.

## Features

- 🤖 AI-powered goal breakdown and planning
- 🔍 Lead research and discovery
- ✍️ Personalized email generation
- 📧 Email sending capabilities
- 📊 Progress tracking and logging
- 🔄 Modular and extensible architecture

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/agentsender.git
cd agentsender
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file:
```bash
cp .env.example .env
```

5. Edit `.env` and add your API keys and credentials.

## Usage

Run the agent with a goal:

```bash
python main.py --goal "Find 5 startup founders in the AI space and send them personalized cold emails"
```

Or run interactively:

```bash
python main.py
```

## Project Structure

```
agentsender/
├── main.py                  # CLI entry point
├── agent.py                 # Core agent loop
├── planner.py              # Goal breakdown
├── tools/
│   ├── search.py           # Lead research
│   ├── summarize.py        # Company summarizer
│   ├── write_email.py      # Email writer
│   ├── send_email.py       # Email sending
├── memory/
│   ├── storage.py          # Logging & memory
├── .env                    # API keys + credentials
├── .env.example            # Template for .env
├── requirements.txt
└── logs/                   # All logs and data
```

## Development

### Adding New Tools

1. Create a new file in the `tools/` directory
2. Implement your tool class with the required methods
3. Add the tool to the `AgentSender` class in `agent.py`

### Extending Memory

The `MemoryStorage` class in `memory/storage.py` can be extended to support additional storage backends or data types.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT API
- The open-source community for various tools and libraries used in this project
