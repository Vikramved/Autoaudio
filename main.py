import pyrogram
import datetime

bot = pyrogram.Client("my_bot", api_id="15428219", api_hash="0042e5b26181a1e95ca40a7f7c51eaa7", bot_token="5166769555:AAFM8gtzAOJ4H9MRteci8QSvjO4f6m8YTCc")

@bot.on_message()
async def handle_message(client, message):
    if message.text.startswith("@admin"):
        report_text = message.text[6:]
        report_time = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        track_id = f"#MB{message.chat.id}"
        report = f"Reporter: {message.from_user.username}\nReporter Id: {message.from_user.id}\nTrack id: {track_id}\nReport Text: {report_text}\nReport Time: {report_time}"
        await message.reply(report)

print("❗️🙌🏻❗️🙌🏻❗️")
bot.run()
