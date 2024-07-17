import logging
import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Read configuration from environment variables
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
SOURCE_CHANNEL_ID = int(os.getenv('SOURCE_CHANNEL_ID'))
DEST_CHANNEL_ID = int(os.getenv('DEST_CHANNEL_ID'))

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Bot has started!')

async def forward_message(update: Update, context: CallbackContext) -> None:
    logger.info(f"Received a message in source channel: {update.channel_post}")
    if update.channel_post:
        message = update.channel_post
        logger.info(f"Message details: {message}")

        if message.photo:
            logger.info("Forwarding photo")
            # If the message has a photo
            try:
                await context.bot.send_photo(chat_id=DEST_CHANNEL_ID,
                                             photo=message.photo[-1].file_id,
                                             caption=message.caption_html or "",
                                             parse_mode='HTML')
                logger.info("Photo forwarded successfully")
            except Exception as e:
                logger.error(f"Failed to forward photo: {e}")
        elif message.text:
            logger.info("Forwarding text")
            # If the message has text
            try:
                await context.bot.send_message(chat_id=DEST_CHANNEL_ID,
                                               text=message.text_html or message.text,
                                               parse_mode='HTML')
                logger.info("Text forwarded successfully")
            except Exception as e:
                logger.error(f"Failed to forward text: {e}")
        elif message.document:
            logger.info("Forwarding document")
            # If the message has a document
            try:
                await context.bot.send_document(chat_id=DEST_CHANNEL_ID,
                                                document=message.document.file_id,
                                                caption=message.caption_html or "",
                                                parse_mode='HTML')
                logger.info("Document forwarded successfully")
            except Exception as e:
                logger.error(f"Failed to forward document: {e}")
        elif message.video:
            logger.info("Forwarding video")
            # If the message has a video
            try:
                await context.bot.send_video(chat_id=DEST_CHANNEL_ID,
                                             video=message.video.file_id,
                                             caption=message.caption_html or "",
                                             parse_mode='HTML')
                logger.info("Video forwarded successfully")
            except Exception as e:
                logger.error(f"Failed to forward video: {e}")
        elif message.audio:
            logger.info("Forwarding audio")
            # If the message has an audio
            try:
                await context.bot.send_audio(chat_id=DEST_CHANNEL_ID,
                                             audio=message.audio.file_id,
                                             caption=message.caption_html or "",
                                             parse_mode='HTML')
                logger.info("Audio forwarded successfully")
            except Exception as e:
                logger.error(f"Failed to forward audio: {e}")
        elif message.voice:
            logger.info("Forwarding voice")
            # If the message has a voice
            try:
                await context.bot.send_voice(chat_id=DEST_CHANNEL_ID,
                                             voice=message.voice.file_id,
                                             caption=message.caption_html or "",
                                             parse_mode='HTML')
                logger.info("Voice forwarded successfully")
            except Exception as e:
                logger.error(f"Failed to forward voice: {e}")
        else:
            logger.info('Message type not supported.')

async def log_all_messages(update: Update, context: CallbackContext) -> None:
    logger.info(f"Update received: {update}")

def main() -> None:
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(MessageHandler(filters.COMMAND, start))
    application.add_handler(MessageHandler(filters.ChatType.CHANNEL, forward_message))
    application.add_handler(MessageHandler(filters.ALL, log_all_messages))  # Log all updates

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()