import os

from pyrogram import Client, filters

from pydub import AudioSegment

from langdetect import detect

# Telegram API credentials

api_id = "15428219"

api_hash = "0042e5b26181a1e95ca40a7f7c51eaa7"

bot_token = "5166769555:AAFM8gtzAOJ4H9MRteci8QSvjO4f6m8YTCc"

# Create the Pyrogram client

app = Client("caption_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Function to detect the language of an audio file

def detect_language(file_path):

    audio = AudioSegment.from_file(file_path)

    audio.export("temp.wav", format="wav")

    lang = detect("temp.wav")

    os.remove("temp.wav")

    return lang

# Handler for incoming messages

@app.on_message(filters.document)

def handle_message(client, message):

    # Check if the document is a movie file

    if message.document.mime_type.startswith("video"):

        # Download the file

        file_path = client.download_media(message, file_name="movie_file")

        

        # Detect the language of the audio

        lang = detect_language(file_path)

        

        # Format the audio language information

        audio_info = f"Audio: {lang}"

        

        # Add the audio language information to the caption

        caption = message.caption if message.caption else ""

        if "Audio:" not in caption:

            caption = f"{caption}\n{audio_info}"

        

        # Update the caption of the message

        client.edit_message_caption(

            message.chat.id,

            message.message_id,

            caption

        )

# Start the bot

print("sett")

app.run()

