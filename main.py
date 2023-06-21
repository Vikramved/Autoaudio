import pyrogram
import datetime
import random
import time
import pymongo
import pytz

bot = pyrogram.Client(
    "my_bot",
    api_id="15428219",
    api_hash="0042e5b26181a1e95ca40a7f7c51eaa7",
    bot_token="5166769555:AAFM8gtzAOJ4H9MRteci8QSvjO4f6m8YTCc"
)

db = pymongo.MongoClient("mongodb+srv://RPN:RPN@tgreporternew.rys1amm.mongodb.net/?retryWrites=true&w=majority").my_db

@bot.on_message()
async def handle_message(client, message):
    if message.text.startswith("@admin"):
        # Send the loading message
        loading_message = await message.reply("Report sending ○○○○○○○○○")

        report_text = message.text[6:]

        # Get the current time in India
        india_timezone = pytz.timezone('Asia/Kolkata')
        now_in_india = datetime.datetime.now(india_timezone)
        report_time = now_in_india.strftime('%I:%M:%S %p')
        report_date = now_in_india.strftime('%d-%m-%Y')
        report_day = now_in_india.strftime('%A')

        track_id = f"#MB{random.randint(1, 1000000)}"
        report_top = "✅ Rᴇᴘᴏʀᴛ sᴇɴᴅ ᴛᴏ ᴀᴅᴍɪɴ ✅"

        report = {
            "report_top": report_top,
            "reporter": message.from_user.first_name,
            "reporter_id": message.from_user.id,
            "track_id": track_id,
            "report_text": report_text,
            "report_time": report_time,
            "report_date": report_date,
            "report_day": report_day,
        }
        db.reports.insert_one(report)

        # Update the loading message with the filled animation
        for i in range(10):
            filled = "●" * (i + 1)
            unfilled = "○" * (10 - (i + 1))
            loading_bar = f"Report sending {filled}{unfilled}"
            await loading_message.edit_text(loading_bar)
            time.sleep(0.5)

        await loading_message.delete()

        await message.reply(f"{report['report_top']}\n\n👤 Rᴇᴘᴏʀᴛᴇʀ: {report['reporter']}\n🆔 Rᴇᴘᴏʀᴛᴇʀ ɪᴅ: {report['reporter_id']}\n📜 Tʀᴀᴄᴋ ɪᴅ: {report['track_id']}\n\n💬 Rᴇᴘᴏᴛʀ ᴛᴇxᴛ : {report['report_text']}\n\n⌚ Rᴇᴘᴏʀᴛ ᴛɪᴍᴇ: {report['report_time']}\n🗓️ Rᴇᴘᴏʀᴛ ᴅᴀᴛᴇ: {report['report_date']}\n⛅ Rᴇᴘᴏʀᴛ ᴅᴀʏ: {report['report_day']}")
        channel_id = -1001904370879
        await client.send_message(channel_id, f"Reporter: {report['reporter']}\nReporter ID: {report['reporter_id']}\nTrack ID: {report['track_id']}\nReport Text: {report['report_text']}\nReport Time: {report['report_time']}\nReport Date: {report['report_date']}\nReport Day: {report['report_day']}")

print("❗️🙌🏻❗️🙌🏻❗️")
bot.run()
