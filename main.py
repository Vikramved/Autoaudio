from pyrogram import Client, filters
from pyrogram.types import Message
from ffprobe import FFProbe
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

    # Download the media file
    file_path = bot.download_media(file_id)

    # Log the start of language detection
    logging.info("Language detection started...")

    # Use FFprobe to analyze the media file
    probe = FFProbe(file_path)
    audio_streams = probe.audio_streams

    # Extract audio language information
    languages = set()
    for stream in audio_streams:
        language = stream.tags.get("language")
        if language:
            languages.add(language)
    
    # Log the detected languages
    logging.info(f"Detected languages: {languages}")

    # Build the caption based on the extracted audio languages
    if len(languages) > 1:
        caption = "Audio: " + "+".join(languages)
    elif len(languages) == 1:
        caption = "Audio: " + list(languages)[0]
    else:
        caption = "No audio language information found."

    # Send the media file with the caption as its caption
    bot.send_document(chat_id=message.chat.id, document=file_path, caption=caption)

    # Delete the downloaded file
    bot.remove(file_path)


# Run the bot
print("start")
app.run()
