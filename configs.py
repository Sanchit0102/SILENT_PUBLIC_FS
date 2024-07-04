# (c) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧        ==> For New Updates And Changes !!
# Dont Try To Remove

import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "25833520"))
  API_HASH = os.environ.get("API_HASH", "7d012a6cbfabc2d0436d7a09d8362af7")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7038670237:AAEBFulq0RNu80O7Kg_ukKTgPWqrWYi-E98")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "PublicFileStore01_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001828164247"))
  # SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "")
  # SHORTLINK_API = os.environ.get('SHORTLINK_API', "")
  try:
      ADMINS=[]
      for x in (os.environ.get("ADMINS", "563896360 1562935405 7053097886").split()):
          ADMINS.append(int(x))
  except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://trumbot:trumbot@cluster0.cfkaeno.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002224312828")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001828164247"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", False))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔸 Owner: [Click Here](tg://settings)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧](https://t.me/THE_DS_OFFICIAL)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a **Public File Store Bot**.

How to Use Bot & it's Benefits??

Send me any File & It will be uploaded in My Database & You will Get the File Link.

Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from CopyRight Infringement Issue. I support Channel Also You Can Check About Bot.

Note: Store only MOVIE & SERIES Nothing else. 

PORNOGRAPHY CONTENTS and STUDEY METRIALS are strictly prohibited & get Permanent Ban.
"""
