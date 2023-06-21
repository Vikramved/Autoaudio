import pyrogram
import datetime
import random
import time
import pytz

bot = pyrogram.Client(
    "my_bot",
    api_id="15428219",
    api_hash="0042e5b26181a1e95ca40a7f7c51eaa7",
    bot_token="5166769555:AAFM8gtzAOJ4H9MRteci8QSvjO4f6m8YTCc"
)

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

        # Update the loading message with the filled animation
        for i in range(10):
            filled = "●" * (i + 1)
            unfilled = "○" * (10 - (i + 1))
            loading_bar = f"Report sending {filled}{unfilled}"
            await loading_message.edit_text(loading_bar)
            time.sleep(0.5)

        await loading_message.delete()

        await message.reply(f"{report_top}\n\n👤 Rᴇᴘᴏʀᴛᴇʀ: {message.from_user.first_name}\n🆔 Rᴇᴘᴏʀᴛᴇʀ ɪᴅ: {message.from_user.id}\n📜 Tʀᴀᴄᴋ ɪᴅ: {track_id}\n\n💬 Rᴇᴘᴏᴛʀ ᴛᴇxᴛ : {report_text}\n\n⌚ Rᴇᴘᴏʀᴛ ᴛɪᴍᴇ: {report_time}\n🗓️ Rᴇᴘᴏʀᴛ ᴅᴀᴛᴇ: {report_date}\n⛅ Rᴇᴘᴏʀᴛ ᴅᴀʏ: {report_day}")
        channel_id = -1001904370879
        await client.send_message(channel_id, f"Reporter: {message.from_user.first_name}\nReporter ID: {message.from_user.id}\nTrack ID: {track_id}\nReport Text: {report_text}\nReport Time: {report_time}\nReport Date: {report_date}\nReport Day: {report_day}")

print("❗️🙌🏻❗️🙌🏻❗️")

app = bot.export_session_string()
bot.stop()

app.run(host="0.0.0.0", port=3000)
