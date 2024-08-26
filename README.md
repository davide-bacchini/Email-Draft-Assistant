# Email Draft Assistant

## Overview

Email Draft Assistant is an automated system that monitors your Gmail inbox for unread messages, creates draft responses using AI, and marks the original emails as read. This tool is designed to save time and streamline email communication by providing intelligent, context-aware draft responses.

## Features

- Continuous monitoring of unread Gmail messages
- AI-powered draft creation based on email content and context
- Automatic marking of processed emails as read
- Integration with OpenAI's GPT model for natural language processing
- Secure handling of Gmail credentials and API access

## Requirements

- Python 3.7+
- Gmail account with API access enabled
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/davidebac/email-draft-assistant.git
   cd email-draft-assistant
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Gmail API credentials:
   - Follow the [Gmail API Python Quickstart](https://developers.google.com/gmail/api/quickstart/python) to obtain your `gmail_token.json` file
   - Place the `gmail_token.json` file in the project root directory

4. Set up your OpenAI API key:
   - Create an environment variable named `OPENAI_API_KEY` with your OpenAI API key

## Usage

Run the main script to start the Email Draft Assistant:

```
python main.py
```

The program will continuously monitor your Gmail inbox for unread messages. When it detects an unread email, it will:

1. Read the email content
2. Generate a draft response using the AI model
3. Create a draft in your Gmail account
4. Mark the original email as read

## Configuration

You can customize the behavior of the Email Draft Assistant by modifying the following files:

- `main.py`: Adjust the main loop and execution flow
- `functions.py`: Modify email processing and draft creation logic
- `write_email.py`: Customize the AI prompt and response generation


## Disclaimer

This tool is for assistive purposes only. Always review and edit AI-generated drafts before sending emails. The user is responsible for the content of all sent emails.