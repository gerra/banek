from telegram import Bot
import os
import asyncio
import datetime


async def send_anek():
    token = os.environ.get('TG_BOT_TOKEN')
    channel_id = os.environ.get('TG_NAILS_CHANNEL_ID')

    with open("anek_nails.txt", "r") as f:
        text = f.read()
        bot = Bot(token=token)
        await bot.send_message(chat_id=channel_id, text=text)


def log(msg):
    with open("logs.txt", "a") as f:
        script_file_name = os.path.basename(__file__)
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{script_file_name}] {date} - {msg}\n")


if __name__ == '__main__':
    log("I'm HERE")

    asyncio.run(send_anek())
