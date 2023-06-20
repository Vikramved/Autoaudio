from pyrogram import Client, filters
import time

app = Client("my_bot", 
            api_id="15428219", 
            api_hash="0042e5b26181a1e95ca40a7f7c51eaa7", 
            bot_token="5166769555:AAFM8gtzAOJ4H9MRteci8QSvjO4f6m8YTCc"
            )

# Define the filter for messages containing "@admin"
@admin_filter := filters.create(lambda _, __, message: "@admin" in message.text.lower())

# Handle the messages that match the filter
@app.on_message(admin_filter)
def handle_admin_message(client, message):
    # Get the sender's username and Telegram user id
    sender_username = message.from_user.username
    sender_id = message.from_user.id

    # Get the report text and current time
    report_text = message.text.replace("@admin", "").strip()
    report_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Build the reply message
    reply_message = (
        "Report sent successfully\n"
        f"Reporter: {sender_username}\n"
        f"Reporter Id: {sender_id}\n"
        f"Track id: #MB{sender_id % 10}{sender_id % 10 + 1}\n"
        f"Report Text: {report_text}\n"
        f"Report Time: {report_time}"
    )

    # Reply to the message
    message.reply_text(reply_message)


# Start the bot
print("Started")
app.run()
