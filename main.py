import pyrogram
import datetime
import random
import pymongo

bot = pyrogram.Client("my_bot", api_id="15428219", api_hash="0042e5b26181a1e95ca40a7f7c51eaa7", bot_token="5166769555:AAFM8gtzAOJ4H9MRteci8QSvjO4f6m8YTCc")

db = pymongo.MongoClient("mongodb+srv://RP:RP@tgreporter.fgojwcu.mongodb.net/?retryWrites=true&w=majority").my_db

@bot.on_message()
async def handle_message(client, message):
    if message.text.startswith("@admin"):
        report_text = message.text[6:]
        report_time = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        track_id = f"#MB{random.randint(1, 1000000)}"
        report = {
            "reporter": message.from_user.username,
            "reporter_id": message.from_user.id,
            "track_id": track_id,
            "report_text": report_text,
            "report_time": report_time,
        }
        db.reports.insert_one(report)
        await message.reply(report)
        channel_id = -1001904370879
        await client.send_message(channel_id, report)

print("❗️🙌🏻❗️🙌🏻❗️")
bot.run()
