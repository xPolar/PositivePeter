# IMPORTANT
# Whenever you edit the Config file you must do a full restart of the bot (This also applies if you edit the main file)
# IMPORTANT

# Imports
import motor.motor_asyncio

# Discord Bot
# Bot's token (DON'T SHARE WITH ANYONE ELSE!) (To find your token go to https://discordapp.com/developers/appli~cations/ > Your Wumpus-Bot Application > Bot (Turn the application into a bot if you haven't already) > Token)
TOKEN = "NjQ5NTM1Njk0MTQ1ODQ3MzAx.Xm29VQ.Q3ADjHp8yaurxEJCiGr_oN8JBX8"
# Bot's prefix
PREFIX = "s!"
# Owner IDS (People who have access to restart the bot)
OWNERIDS = [619284841187246090,
            102102717165506560]
# Main Color (Replace the part after 0x with a hex code)
MAINCOLOR = 0x7289DA
# Error Color (Replace the part after the 0x with a hex code)
ERRORCOLOR = 0xFF2B2B
# Channel where join logs will be stored
JOIN_LOG = 651587329298792502
# Channel where suggestions will be stored
TRIGGER_SUGGEST_LOG = 651587561931800597
# Channel where block logs will be stored
BLOCK_LOG = 651635427035447316
# Bot ID
BOTID = 649535694145847301

# MongoDB
# Cluster (Replace the <password> of your uri part with your password and remove the "<>")
CLUSTER = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://PositivePeter:33FQ3RhnqTyV@positivepeter-kb4hl.azure.mongodb.net/test?retryWrites=true&w=majority")
