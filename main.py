from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession

import toml, asyncio

config = toml.load("./config.toml")

api_id = config["telegram"]["api_id"]
api_hash = config["telegram"]["api_hash"]
session_name = config["telegram"]["session_name"]
auth_string = config["telegram"]["auth_string"]


loop = asyncio.get_event_loop()

async def send_message_check_reply(conv, text, reply):
    await conv.send_message(text)
    msg = await conv.get_response()
    if not reply in msg.text:
        print('Error: "{}" not found in "{}"'.format(reply, msg.text))
        raise AssertionError
    await asyncio.sleep(1)
    return msg

async def main():
    async with TelegramClient(StringSession(auth_string), api_id, api_hash) as client:

        async with client.conversation('@BotFather') as conv:
            await send_message_check_reply(conv, '/newbot', 'Alright, a new bot. How are we going to call it? Please choose a name for your bot.')


if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.INFO)

    loop.run_until_complete(main())