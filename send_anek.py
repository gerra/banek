from telegram import Bot
import os
import asyncio
import datetime

from telegram.error import TelegramError

script_directory = os.path.dirname(os.path.abspath(__file__))
script_file_name = os.path.basename(__file__)


async def send_anek():
    token = os.environ.get('TG_BOT_TOKEN')
    channel_id = os.environ.get('TG_NAILS_CHANNEL_ID')
    anek_file_path = os.path.join(script_directory, "anek_nails.txt")

    with open(anek_file_path, "r") as f:
        text = f.read()
        try:
            log("Creating a bot...")
            bot = Bot(token=token)
            log("Sending a message...")
            await bot.send_message(chat_id=channel_id, text=text)
            log("Message sent!")
        except TelegramError as e:
            log(e)
        except Exception as e:
            log(f"Error: {e.__str__()}")


def log(msg):
    logs_file_path = os.path.join(script_directory, "logs.txt")
    with open(logs_file_path, "a") as f:
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        msg_to_log = f"[{script_file_name}] {date} - {msg}"
        f.write(f"{msg_to_log}\n")
        print(msg_to_log)


if __name__ == '__main__':
    log("Starting a script...")
    asyncio.run(send_anek())
