from telethon.sync import TelegramClient, events
from constants import api_id, api_hash
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

with TelegramClient('test', api_id, api_hash) as client:
   for message in client.iter_messages(-1001303623202):
      print(message.id, message.text)

   client.run_until_disconnected()