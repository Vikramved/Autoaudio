from pyrogram import Client, filters
from pyrogram.types import Message
from ffprobe import FFProbe
from concurrent.futures import ThreadPoolExecutor
from pyrogram.errors import MessageNotModified
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

api_id = "15428219"
api_hash = "0042e5b26181a1e95ca40a7f7c51eaa7"
bot_token = "5166769555:AAFM8gtzAOJ4H9MRteci8QSvjO4f6m8YTCc"

# Initialize the Pyrogram client
app = Client("telegram_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Filter to handle incoming messages with media
@Client.on_message(filters.media)
def handle_media(bot: Client, message: Message):
    # Get the media file ID
    file_id = message.media.document.file_id

    # Use a thread pool executor for parallel processing
    with ThreadPoolExecutor() as executor:
        # Download the media file
        file_path = bot.download_media(file_id)

        # Submit the analysis task to the executor
        future = executor.submit(analyze_media, bot, message.chat.id, file_path)

        # Add a callback to send the file with the caption when analysis is complete
        future.add_done_callback(lambda f: send_media_with_caption(bot, message.chat.id, file_id, f.result()))

# Function to analyze the media file and extract the language information
def analyze_media(bot: Client, chat_id: int, file_path: str):
    probe = FFProbe(file_path)
    audio_streams = probe.audio_streams

    # Extract audio language information
    languages = set()
    for stream in audio_streams:
        language = stream.tags.get("language")
        if language:
            languages.add(language)

    # Log the detected languages
    logging.info(f"Bot detected languages: {languages}")

    # Build the caption based on the extracted audio languages
    if len(languages) > 1:
        caption = "Audio: " + "+".join(languages)
    elif len(languages) == 1:
        caption = "Audio: " + list(languages)[0]
    else:
        caption = "No audio language information found."

    return (file_path, caption)

# Function to send the media file with the caption
def send_media_with_caption(bot: Client, chat_id: int, file_id: str, result):
    file_path, caption = result

    # Log the media file detection
    logging.info(f"Bot detected media file: {file_path}")

    # Send the media file with the caption as its caption
    try:
        bot.send_document(chat_id=chat_id, document=file_path, caption=caption)
    except MessageNotModified:
        pass

    # Delete the downloaded file
    bot.remove(file_path)

# Run the bot
app.run()
