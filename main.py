import os
from dotenv import load_dotenv

load_dotenv()

from telethon import TelegramClient, events

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient(os.getenv("SESSION_NAME"), api_id, api_hash)
print("Client Starting...")
# Log in to your account
client.start()
print("Client Created")
# Source and target channels
source_channel_id = int(os.getenv("FROM_CHANNEL_ID"))
target_channel_id = int(os.getenv("TO_CHANNEL_ID"))
print("Channels Loaded")


# keep getting all live messages from source channel
@client.on(events.NewMessage(chats=source_channel_id))
async def handler(event):
    print(event.message)
    # send message to target channel
    await client.send_message(target_channel_id, event.message)
    print("Message Sent")


# run until disconnect
client.run_until_disconnected()
