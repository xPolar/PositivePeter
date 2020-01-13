# IMPORTANT
# Whenever you edit the Config file you must do a full restart of the bot (This also applies if you edit the main file)
# IMPORTANT

# Imports
import motor.motor_asyncio

# Discord Bot
# Bot's token (DON'T SHARE WITH ANYONE ELSE!) (To find your token go to https://discordapp.com/developers/appli~cations/ > Your Wumpus-Bot Application > Bot (Turn the application into a bot if you haven't already) > Token)
TOKEN = ""
# Bot's prefix
PREFIX = ""
# Owner IDS (People who have access to restart the bot)
OWNERIDS = []
# Main Color (Replace the part after 0x with a hex code)
MAINCOLOR = 0x
# Error Color (Replace the part after the 0x with a hex code)
ERRORCOLOR = 0x
# Thread Channel (Channel where thread logs will be sent)
THREAD_CHANNEL =
# Role that volunteers will have that allows them to help
VOLUNTEER_ROLE =
# Channel where join logs will be stored
JOIN_LOG =
# Channel where suggestions will be stored
TRIGGER_SUGGEST_LOG =

# MongoDB
# Cluster (Replace the <password> of your uri part with your password and remove the "<>")
CLUSTER = motor.motor_asyncio.AsyncIOMotorClient("")
