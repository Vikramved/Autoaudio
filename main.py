import os
from pyrogram import Client, filters

app = Client("my_bot")

@app.on_message(filters.document & filters.mkv)
def detect_language(client, message):
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
