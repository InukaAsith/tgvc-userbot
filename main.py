from os import environ
# import logging
from pyrogram import idle
from pyrogram import Client as bot

API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]
session_name = environ["SESSION_NAME"]

Plugins = dict(
    root="plugins",
    include=[
        "vc.player",
        "sysinfo"
    ]
)
bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=plugins
)

app = Bot(session_name, API_ID, API_HASH)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> DPLAYER STARTED')


bot.start()
run()

