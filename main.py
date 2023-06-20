import pyrogram

bot = pyrogram.Client("my_bot", api_id="15428219", api_hash="0042e5b26181a1e95ca40a7f7c51eaa7", bot_token="5166769555:AAFM8gtzAOJ4H9MRteci8QSvjO4f6m8YTCc")

@bot.on_message()
async def handle_message(message):
    if message.text.startswith("@admin"):
        report_text = message.text[6:]
        report_time = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        track_id = f"#MB{message.chat.id}"
        await message.reply("Report sent successfully")
        await message.reply(f"Reporter: {message.from_user.username}")
        await message.reply(f"Reporter Id: {message.from_user.id}")
        await message.reply(f"Track id: {track_id}")
        await message.reply(f"Report Text: {report_text}")
        await message.reply(f"Report Time: {report_time}")

print("❗️🙌🏻❗️🙌🏻❗️")
bot.run()
