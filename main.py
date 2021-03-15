from os import environ
# import logging
from pyrogram import idle
from pyrogram import Client as bot

API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]

Plugins = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping",
        "sysinfo"
    ]
)
bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=Plugins
)

bot.start()
run()
