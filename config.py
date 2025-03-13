import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Telegram API Details (Get these from my.telegram.org)
API_ID = 29791926  # Direct value, remove getenv() for fixed values
API_HASH = "550ae225aaa88c599cf71983f40c86ac"

# Bot Token (Get this from @BotFather)
BOT_TOKEN = "7703772837:AAFzhIP8gxauLCSuv9hZoh2X1NwvZjSCgBU"

# MongoDB Database URL (Get this from cloud.mongodb.com)
MONGO_DB_URI = "mongodb+srv://USERNAME:PASSWORD@cluster0.vo9ib.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Bot Configuration
DURATION_LIMIT_MIN = 60  # Default duration limit for audio/video
LOGGER_ID = -1002342917994  # Log Group Chat ID
OWNER_ID = 6720017767  # Your Telegram User ID

# Heroku Configuration (If deploying on Heroku)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# GitHub Repository (Change if using a different repo)
UPSTREAM_REPO = "https://github.com/AnonymousX1025/AnonXMusic"
UPSTREAM_BRANCH = "master"
GIT_TOKEN = None  # If repo is private, replace None with "your_github_token"

# Support Links
SUPPORT_CHANNEL = "https://t.me/hkmusic4"
SUPPORT_CHAT = "https://t.me/hkmusic4"

# String Sessions (Get this from @StringFatherBot)
STRING1 = "BQHGlrYAkGrTZgLRF0Xl0tkfEmoglq2DzbnXKfpZ9c4ZH5JAg6yN1V-Ff3Dw5FeeQ5VZLFXZy0a9iZoB3nu2DcjPwkgEWsDlrH0brCrGrFR10c2VGK1ieig0v98BnKCfWQs_qCzqqeOA081oXbHzAqVj0o_VUWxifT3b_Y6hotNHK5V75ghqin5nowKOs9izb0xR4fKb_VlZyPs46vc53uivSkYr0kc0-9kBhmedJXuymfx-j4rTCp4KSrM3YxL-Kzw3WbqwDs6cUk2RVys3wwp4qaONFw8CfDp0YjDWTBYe2-mCm6l7RlFFt2HCksD4MO4Ef3Hii36mFJuew5nUt9nSo3AWYQAAAAHLLj6lAQ"

# Optional String Sessions (If needed)
STRING2 = None
STRING3 = None
STRING4 = None
STRING5 = None

# Auto Leave Assistant
AUTO_LEAVING_ASSISTANT = False  # Set to True if you want the assistant to leave after inactivity

# Spotify API (Get from developer.spotify.com)
SPOTIFY_CLIENT_ID = None
SPOTIFY_CLIENT_SECRET = None

# Playlist Fetch Limit
PLAYLIST_FETCH_LIMIT = 25

# Telegram File Size Limits
TG_AUDIO_FILESIZE_LIMIT = 104857600  # 100MB
TG_VIDEO_FILESIZE_LIMIT = 1073741824  # 1GB

# Image URLs
START_IMG_URL = "https://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpg"
PING_IMG_URL = "https://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpg"

# Function to Convert Time to Seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Check if SUPPORT_CHANNEL and SUPPORT_CHAT URLs are Valid
if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL URL is incorrect. It must start with https://")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT URL is incorrect. It must start with https://")