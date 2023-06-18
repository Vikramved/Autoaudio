import os
from pyrogram import Client, filters

app = Client("my_bot", 
            api_id="15428219", 
            api_hash="0042e5b26181a1e95ca40a7f7c51eaa7", 
            bot_token="5166769555:AAFM8gtzAOJ4H9MRteci8QSvjO4f6m8YTCc"
            )

@app.on_message(filters.document & filters.video)
def detect_language(client, message):
    if message.document.file_name.endswith(".mkv"):
        caption = ""
        for track in message.document.thumbs[0].video_info.audio_tracks:
            if track.language:
                if caption:
                    caption += "+"
                caption += track.language
        message.reply_text(f"Audio: {caption}")

print("shahiddd")
app.run() 
            
