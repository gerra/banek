import asyncio
import datetime
import os
import random
import subprocess

from telegram import Bot
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
            log(f"Error: {e.message}")
        except Exception as e:
            log(f"Error: {e.__str__()}")


def schedule_next():
    hour = random.randint(15, 19)
    minute = random.randint(0, 59)
    schedule_next_specific(hour, minute, True)


def schedule_next_specific(hour, minute, tomorrow):
    formatted_time = "{:02d}:{:02d}".format(hour, minute)
    if tomorrow:
        formatted_time += " tomorrow"

    command_to_run = f"echo \"python3 $HOME/Projects/banek/send_anek.py\" | at \"{formatted_time}\""

    log(f"Scheduling new send by command [{command_to_run}]")

    result = subprocess.run(command_to_run, shell=True, check=True, text=True, stderr=subprocess.PIPE)
    log(f"Result: {result.stderr.rstrip()}")


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

    schedule_next()
    # schedule_next_specific(21, 25, False)

# atq -- show scheduled jobs
# atrm X -- remove job X
# at -c X -- show info about job X
# atrm $(atq | cut -f1) -- remove all jobs
