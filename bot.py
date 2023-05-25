from telethon import TelegramClient, events

api_id = #your api_id from https://my.telegram.org/apps
api_hash = # "your api hash"
phone = #"your phone number"

client = TelegramClient(phone, api_id, api_hash)

client.start()

# List of chat_id chats to be parsed
chat_id_list = # [-1001234567890, -1001234567891]

# Chat_id of the channel where you want to send messages with the keyword
target_channel = # -1001234567892

# List of words to forward
words = # ['keyword 1', 'keyword 2']

# Event handler for new messages in chats from the list
@client.on(events.NewMessage(chats=chat_id_list))
async def handler(event):
    for word in words:
        # Check if the message contains the keyword
        if word in event.message.message.lower():
            # Send a message to the target channel
            await client.forward_messages(target_channel, event.message)

# Run an infinite event loop
client.run_until_disconnected()
