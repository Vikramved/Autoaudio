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
        report_time = f"{datetime.datetime.now().strftime('%I:%M:%S %p')}"
        report_date = f"Report Date:- {datetime.datetime.now().strftime('%d-%m-%Y')}"
        report_day = f"Report Day:- {datetime.datetime.now().strftime('%A')}"
        track_id = f"#MB{random.randint(1, 1000000)}"
        report = {
            "reporter": message.from_user.first_name,
            "reporter_id": message.from_user.id,
            "track_id": track_id,
            "report_text": report_text,
            "report_time": report_time,
            "report_date": report_date,
            "report_day": report_day,
        }
        db.reports.insert_one(report)
        now_in_india = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
        report_time_in_india = f"{now_in_india.strftime('%I:%M:%S %p')}"
        await message.reply(f"Reporter: {report['reporter']}\nReporter ID: {report['reporter_id']}\nTrack ID: {report['track_id']}\nReport Text: {report['report_text']}\nReport Time: {report_time_in_india}\nReport Date: {report['report_date']}\nReport Day: {report['report_day']}")
        channel_id = -1001904370879
        await client.send_message(channel_id, f"Reporter: {report['reporter']}\nReporter ID: {report['reporter_id']}\nTrack ID: {report['track_id']}\nReport Text: {report['report_text']}\nReport Time: {report_time_in_india}\nReport Date: {report['report_date']}\nReport Day: {report['report_day']}")

print("❗️🙌🏻❗️🙌🏻❗️")
bot.run()
