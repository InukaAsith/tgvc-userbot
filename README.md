# Telegram Voice Chat UserBot

A Telegram UserBot to Play Audio in Voice Chats.

This is also the source code of the userbot which is being used for playing DJ/Live Sets music in [VC DJ/Live Sets](https://t.me/VCSets) group.

Made with [tgcalls](https://github.com/MarshalX/tgcalls) and [Pyrogram Smart Plugin](https://docs.pyrogram.org/topics/smart-plugins)

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/dashezup/tgvc-userbot/tree/dev)

- Session string can be exported by using Pyrogram
  ```
  # pip install Pyrogram TgCrypto
  from pyrogram import Client

  api_id = 1234567
  api_hash = "0123456789abcdef0123456789abcdef"

  with Client(":memory:", api_id, api_hash) as app, open("session.txt", "w+") as s_file:
      session_string = app.export_session_string()
      s_file.write(session_string)
      print("Session string has been saved to session.txt")
      print(session_string)
  ```
- Enable the worker after deploy the project to Heroku
- Reply to an audio with `!play` in a Voice Chat enabled Telegram group to start using it

There are some other branchs for other plugins,
you can press the "Deploy to Heroku" button there to deploy it as well.

## Introduction

**Features**

- Playlist, queue
- Loop one track when there is only one track in the playlist
- Automatically downloads audio for the first two tracks in the playlist
  to ensure smooth playing
- Automatically pin the current playing track
- Show current playing position of the audio

**Commands**

The main plugin is `vc.player` which has the following command commands and admin commands.
After start the bot, send `!join` to a voice chat enabeld group chat from userbot account
itself or its contacts, and then common commands like `/play` and `/current` will be available
to every member of the group. send `!help` to check more commands.

- Common commands, available to group members of current voice chat
- starts with / (slash) or ! (exclamation mark)

| Common Commands | Description                                            |
|-----------------|--------------------------------------------------------|
| /play           | reply with an audio to play/queue it, or show playlist |
| /current        | show current playing time of current track             |
| !help           | show help for commands                                 |

- Admin commands, available to userbot account itself and its contacts
- starts with ! (exclamation mark)

| Admin Commands | Description                      |
|----------------|----------------------------------|
| !skip [n] ...  | skip current or n where n >= 2   |
| !join          | join voice chat of current group |
| !leave         | leave current voice chat         |
| !vc            | check which VC is joined         |
| !stop          | stop playing                     |
| !replay        | play from the beginning          |
| !clean         | remove unused RAW PCM files      |
| !mute          | mute the VC userbot              |
| !unmute        | unmute the VC userbot            |

- Commands from other plugins, available only to userbot account itself

| Plugin  | Commands | Description         |
|---------|----------|---------------------|
| ping    | !ping    | show ping time      |
| uptime  | !uptime  | show userbot uptime |
| sysinfo | !sysinfo | show system info    |

**How to Use the Player plugin**

1. Start the userbot
2. send `!join` to a voice chat enabled group chat from userbot account itself
   or its contacts
3. reply to an audio with `/play` to start playing it in the voice chat, every
   member of the group can use common commands such like `/play`, `/current` and `!help` now.
4. check `!help` for more commands

## Requirements

- Python 3.6 or higher
- A [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api) and a Telegram account
- Choose plugins you need, install dependencies which listed above and run `pip install -U -r requirements.txt` to install python package dependencies as well

## Run

Choose one of the two methods and run the userbot with
`python userbot.py`, stop with <kbd>CTRL+c</kbd>. The following example
assume that you were going to use `vc.player` and `ping` plugin, replace
`api_id`, `api_hash` to your own value.

### Method 1: use config.ini

Create a `config.ini` file

```
[pyrogram]
api_id = 1234567
api_hash = 0123456789abcdef0123456789abcdef

[plugins]
root = plugins
include =
    vc.player
    ping
```

### Method 2: write your own userbot.py

Replace the file content of `userbot.py`

```
from pyrogram import Client, idle

api_id = 1234567
api_hash = "0123456789abcdef0123456789abcdef"

plugins = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping"
    ]
)

app = Client("tgvc", api_id, api_hash, plugins=plugins)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
```

## Notes

- Read module docstrings of [plugins/](plugins) you are going to use at
  the beginning of the file for extra notes

# License

AGPL-3.0-or-later
