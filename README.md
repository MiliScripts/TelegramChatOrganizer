# Clean Telegram

This project provides tools to organize your Telegram chats into folders based on topics, private chats, and bots. It uses the Pyrogram library to interact with the Telegram API and Google's Gemini AI to categorize chats by topic.

## File Tree
content_copy
download
Use code with caution.
Markdown

┗ 📂clean-telegram
┣ 📜bot.py
┣ 📜session.py
┗ 📜telegram_organizer.py

## Description

*   `bot.py`: A Pyrogram bot that uses Gemini AI to categorize Telegram chats and organize them into folders.
*   `session.py`: A script to generate a Pyrogram session string for authentication.
*   `telegram_organizer.py`: A command-line tool to organize your Telegram chats into folders using the Pyrogram library and Google's Gemini AI.

## Prerequisites

Before using this project, ensure you have the following:

*   Python 3.6 or higher
*   A Telegram account
*   A Google Cloud project with the Gemini AI API enabled and an API key
*   Environment variables set for API\_ID, API\_HASH, SESSION\_STRING, and GEMINI\_API\_KEY

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd clean-telegram
    ```

2.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**

    Create a `.env` file in the project root directory and add your Telegram API credentials and Gemini API key:

    ```
    API_ID=<your_telegram_api_id>
    API_HASH=<your_telegram_api_hash>
    SESSION_STRING=<your_pyrogram_session_string>
    GEMINI_API_KEY=<your_gemini_api_key>
    ```

    You can obtain the API\_ID and API\_HASH from the [Telegram API development tools](https://my.telegram.org/apps).

    To get the SESSION\_STRING use `session.py`:

    ```bash
    python session.py
    ```

    Copy the generated session string from the console output or your Telegram saved messages.

    To get the GEMINI\_API\_KEY, enable the Gemini AI API in your Google Cloud project and create an API key.

## Usage

### `bot.py`

This script provides a Telegram bot that organizes your chats.

1.  **Run the bot:**

    ```bash
    python bot.py
    ```

2.  **Interact with the bot:**

    Start a private chat with your bot on Telegram and send the `/get` command. The bot will fetch your dialogues, categorize them using Gemini AI, and organize them into folders.

### `telegram_organizer.py`

This script provides a command-line interface to organize your chats.

1.  **Run the script:**

    ```bash
    python telegram_organizer.py --organize
    ```

    Alternatively, run without the `--organize` to review the setup.

    ```bash
    python telegram_organizer.py
    ```

    The script will prompt you to confirm before organizing the chats.

## Detailed File Descriptions

### `bot.py`

This file contains the core logic for the Telegram bot.

*   It uses the `pyrogram` library to interact with the Telegram API.
*   It loads environment variables using the `dotenv` library.
*   It configures the Gemini AI API using the `google.generativeai` library.
*   It defines a command handler for the `/get` command, which fetches dialogues, categorizes them using Gemini AI, and organizes them into folders.
*   It uses colorama for colored logging.

### `session.py`

This file generates a session string for your Telegram account using the Pyrogram library.

*   It loads environment variables using the `dotenv` library.
*   It creates a Pyrogram client in memory and exports the session string.
*   It prints the session string to the console and sends it to your Telegram account.

### `telegram_organizer.py`

This file provides a command-line tool for organizing Telegram chats.

*   It uses the `pyrogram` library to interact with the Telegram API.
*   It loads environment variables using the `dotenv` library.
*   It configures the Gemini AI API using the `google.generativeai` library.
*   It fetches dialogues, categorizes them using Gemini AI, and organizes them into folders.
*   It uses colorama for colored logging.
*   It includes an argument parser for command-line options.

## Error Handling and Logging

The scripts include comprehensive error handling and logging using the `colorama` library for colored output. Errors and warnings are logged in red and yellow, respectively, while informational messages are logged in blue and successful operations are logged in green.

## Limitations

*   The accuracy of chat categorization depends on the quality of the Gemini AI model and the prompt used.
*   The number of folders created is limited to 7 to avoid exceeding Telegram's folder limits.
*   Rate limits imposed by the Telegram API may affect performance, especially when processing a large number of dialogues.
*   Gemini AI API usage is subject to Google's pricing and usage policies.

## Contributing

Contributions to this project are welcome. Please submit a pull request with your changes.
content_copy
download
Use code with caution.
