# ButBot - Telegram Bot (Python Version)

This is a Python implementation of the ButBot Telegram bot that was originally written in Go.

## Features

- `/start` - Welcome message with available commands
- `/get` - Fetches schedule information from the official website
- `/cat` - Sends a random HTTP status cat picture
- Responds to "привет" with a greeting

## Setup

1. Clone the repository
2. Navigate to the `python_bot` directory
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
   - Create a `.env` file or set the `API_TOKEN` environment variable with your Telegram bot token

## Running the Bot

```bash
# Set your bot token as an environment variable
export API_TOKEN="your_bot_token_here"

# Run the bot
python bot.py
```

## Dependencies

- python-telegram-bot
- requests
- beautifulsoup4
- lxml
- pyyaml