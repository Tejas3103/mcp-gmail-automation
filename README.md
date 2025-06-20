<!-- PROJECT LOGO -->
<p align="center">
  <img src="https://via.placeholder.com/200x80?text=MCP+Gmail+Logo" alt="Logo" width="200" height="80">
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="Python Version"></a>
  <a href="#license"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License"></a>
  <a href="https://github.com/Tejas3103/mcp-gmail-automation/commits/main"><img src="https://img.shields.io/github/last-commit/Tejas3103/mcp-gmail-automation.svg" alt="Last Commit"></a>
</p>

# MCP Gmail

MCP Gmail is a Python project that provides tools to automate and interact with Gmail using the Google Gmail API. It allows you to send, search, read, and delete emails programmatically, and is designed to be easily integrated with agentic or AI-driven workflows.

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd MCP\ Gmail
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # or, if using poetry
   poetry install
   ```
3. **Add your `client-secret.json`** to the project root (see Setup below).
4. **Run the example:**
   ```bash
   python main.py
   ```

## Features
- Send emails (with or without attachments)
- Search emails by query or label
- Get details and body of specific email messages
- Delete emails
- Easily extensible for agentic/AI use cases

## Requirements
- Python 3.10+
- Google Cloud project with Gmail API enabled
- OAuth 2.0 credentials (client-secret.json)

## Setup Instructions

1. **Google API Setup**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project (or select an existing one)
   - Enable the Gmail API for your project
   - Create OAuth 2.0 credentials (Desktop app)
   - Download the `client-secret.json` file and place it in the project root directory

2. **First Run Authentication**
   - On first run, the app will prompt you to authenticate with your Google account in a browser. This will generate a token file in the `token files/` directory for future use.

## Usage

### Send an Email (Example)

Run the main script to send a test email:
```bash
python main.py
```
This will send an email to the address specified in `main.py` using your authenticated Gmail account.

### Integrate as a Tool
You can use the `GmailTool` class in your own scripts:
```python
from tools.google.gmail_tools import GmailTool

gmail = GmailTool('client-secret.json')
result = gmail.send_email(
    to='recipient@example.com',
    subject='Hello from MCP Gmail',
    body='This is a test email!',
)
print(result)
```

## Project Structure
```
MCP Gmail/
├── main.py                # Example script to send an email
├── mcp_gmail.py           # Tool registration for agentic/AI use
├── tools/
│   └── google/
│       ├── gmail_tools.py # Core Gmail API logic
│       └── google_apis.py# Google API service setup
├── token files/           # Stores OAuth tokens after authentication
├── client-secret.json     # Your Google OAuth credentials (not included)
├── pyproject.toml         # Project metadata and dependencies
├── README.md              # This file
```

## Notes
- **Do not commit your `client-secret.json` or token files to version control.**
- The first run will require browser authentication.
- You can extend the toolset by adding more methods to `GmailTool`.

## License
MIT

---

For questions or contributions, please open an issue or pull request!
