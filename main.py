from telethon import TelegramClient, events

# ==========================================
# 1. CONFIGURATION
# ==========================================
import os

API_ID = int(os.getenv("API_ID", "2172759"))
API_HASH = os.getenv("API_HASH", "06734ed5b53ec321c64b752c75052117")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
# ID of your private channel. 
# Private channel IDs in Telegram always start with -100
DESTINATION_CHANNEL = -1003977878474 

# Initialize the bot client
client = TelegramClient('stealth_bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# ==========================================
# 2. EVENT HANDLER
# ==========================================
# Listen for any new incoming private message (e.is_private ignores group spam)
@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def silent_forwarder(event):
    try:
        # COPY METHOD (Recommended): 
        # Copies text and media exactly, without a "Forwarded from" header.
        await client.send_message(
            DESTINATION_CHANNEL, 
            event.message, 
            silent=True # Sends to the channel without a notification sound
        )
        
        # FORWARD METHOD (Alternative):
        # If you want to keep the "Forwarded from [User]" tag, uncomment the line below 
        # and delete the send_message block above.
        # await client.forward_messages(DESTINATION_CHANNEL, event.message, silent=True)
        
    except Exception as e:
        print(f"Error forwarding message: {e}")

# Start the bot
print("Bot is running and listening for incoming messages...")
client.run_until_disconnected()
