# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27028102"))
API_HASH = getenv("API_HASH", "b08bff34983dd9ba5837e83b3f093f1e")
BOT_TOKEN = getenv("BOT_TOKEN", "7789372178:AAGjXBZDKMn8CLfO9niDEmN74yysFz-s3SI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5128979564").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://gcute1918:FmgCaYK2Z47ctoSv@cluster0.1fok9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002404360909"))
