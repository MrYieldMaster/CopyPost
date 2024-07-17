# MegaWhaleWatcher Bot

## Overview

MegaWhaleWatcher is a Telegram bot designed to forward messages from a specified source channel to a destination channel. It supports various types of messages including text, photos, documents, videos, audios, and voices.

## Bot Information

- **Name**: MegaWhale Watcher
- **About**: Your go-to bot for the latest updates and signals from @MegaWhaleCalls!
- **Description**: MegaWhale Watcher provides real-time updates, alerts, and signals directly from the MegaWhale community. Stay informed and make timely decisions with ease.

## Setup and Deployment

### Prerequisites

- Python 3.9 or later
- A Telegram bot token from BotFather
- Access to the source and destination Telegram channels

### Installation

1. **Clone the Repository**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configuration**

    Create a `.env` file in the root directory with the following content:

    ```ini
    TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
    SOURCE_CHANNEL_ID=YOUR_SOURCE_CHANNEL_ID
    DEST_CHANNEL_ID=YOUR_DESTINATION_CHANNEL_ID
    ```

    Replace `YOUR_TELEGRAM_BOT_TOKEN`, `YOUR_SOURCE_CHANNEL_ID`, and `YOUR_DESTINATION_CHANNEL_ID` with your actual bot token and channel IDs.

### Running the Bot Locally

1. **Activate the Virtual Environment**

    ```bash
    source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
    ```

2. **Run the Bot**

    ```bash
    python bot.py
    ```

### Deploying to an Ubuntu Server

1. **Update and Upgrade the Server**

    SSH into your server and update the package lists:

    ```bash
    sudo apt update
    sudo apt upgrade -y
    ```

2. **Install Python and Pip**

    ```bash
    sudo apt install python3 python3-venv python3-pip -y
    ```

3. **Transfer Files to the Server**

    Use SCP, SFTP, or any other method to transfer your project files to the server. Example using SCP:

    ```bash
    scp -r /path/to/local/project user@your-server-ip:/path/to/remote/project
    ```

4. **Navigate to Your Project Directory**

    ```bash
    cd /path/to/remote/project
    ```

5. **Create a Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

6. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

7. **Setup Environment Variables**

    Create a `.env` file in the project directory on the server:

    ```ini
    TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
    SOURCE_CHANNEL_ID=YOUR_SOURCE_CHANNEL_ID
    DEST_CHANNEL_ID=YOUR_DESTINATION_CHANNEL_ID
    ```

8. **Run the Bot**

    ```bash
    nohup python bot.py &
    ```

    This will run the bot in the background. You can check the logs with:

    ```bash
    tail -f nohup.out
    ```

### Setting Up as a Systemd Service (Optional)

For better management and to ensure the bot restarts on reboot, you can set it up as a systemd service.

1. **Create a Systemd Service File**

    ```bash
    sudo nano /etc/systemd/system/megawhalewatcher.service
    ```

2. **Add the Following Content**

    ```ini
    [Unit]
    Description=MegaWhale Watcher Bot
    After=network.target

    [Service]
    User=your-username
    WorkingDirectory=/path/to/remote/project
    ExecStart=/path/to/remote/project/venv/bin/python /path/to/remote/project/bot.py
    Restart=always
    Environment="TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN"
    Environment="SOURCE_CHANNEL_ID=YOUR_SOURCE_CHANNEL_ID"
    Environment="DEST_CHANNEL_ID=YOUR_DESTINATION_CHANNEL_ID"

    [Install]
    WantedBy=multi-user.target
    ```

    Replace `your-username` and paths with the appropriate values.

3. **Reload Systemd and Start the Service**

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start megawhalewatcher
    sudo systemctl enable megawhalewatcher
    ```

4. **Check the Service Status**

    ```bash
    sudo systemctl status megawhalewatcher
    ```

## How the Bot Works

1. **Bot Initialization**

    The bot is initialized using the `Application.builder().token(TOKEN).build()` method from the `python-telegram-bot` library. Handlers for different types of messages are added to the bot.

2. **Message Handling**

    - The bot listens for updates from the source channel using a `MessageHandler` with the `filters.ChatType.CHANNEL` filter.
    - When a message is received, the `forward_message` function processes it and forwards it to the destination channel.
    - Different types of messages (text, photos, documents, etc.) are handled and forwarded accordingly.

3. **Logging**

    The bot uses Python's `logging` module to log information about received and forwarded messages, as well as any errors that occur during processing.

## Commands

Currently, the bot does not have specific user commands. However, it can be extended to include commands like:

start - Start interacting with the bot
help - Get a list of available commands and their descriptions
info - Get information about MegaWhale Watcher
subscribe - Subscribe to updates
unsubscribe - Unsubscribe from updates


## Support and Contributions

For any issues or contributions, please reach out to the maintainer or submit a pull request on the project's repository.

