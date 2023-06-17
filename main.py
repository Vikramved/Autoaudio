import os
from pyrogram import Client, filters

app = Client("my_bot", 
            api_id="15428219", 
            api_hash="0042e5b26181a1e95ca40a7f7c51eaa7", 
            bot_token="5166769555:AAFM8gtzAOJ4H9MRteci8QSvjO4f6m8YTCc")

@app.on_message() 
def detect_language(client, message):
    if message.document and message.document.mime_type == "video/x-matroska":
        file_path = message.document.file_name
    os.system(f"mkvmerge -i {file_path} -o temp.mkv")
    os.system("ffmpeg -i temp.mkv -vn -acodec copy temp.aac")
    languages = os.system("ffmpeg -i temp.aac -map 0:a -c:a copy -f segment -segment_time 3 - | ffprobe -v quiet -show_entries stream=tags=language -of default=nw=1:nk=1")
    caption = f"Audio : {languages}"
    message.reply_document(file_path, caption=caption)
    os.remove("temp.mkv")
    os.remove("temp.aac")

print("startedddd")
app.run() 
