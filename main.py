from telethon import TelegramClient,events,Button
from telethon.tl import functions
from telethon.tl import types
from telethon.tl.types import *
from telethon.errors import *
import os
API_ID = 23136380
API_HASH = "6ae6541159e229499615953de667675c"
TOKEN = "1762569512:AAETqZDQrxlKanTAEXam5wuflH7M_VHbUi4"
client=TelegramClient("banallbot",api_id=API_ID,api_hash=API_HASH)
client.start(bot_token=TOKEN)
print('Bot Run')

chat = -1001295691690
@client.on(events.NewMessage(pattern="Start"))
async def deleter(event):
    try:
	    idbot = await client.get_me()
	    idd = idbot.id
	    x=await client.get_participants(chat)
	    for i in x:
	    	if i.id == idd:
	    		pass
	    	else:
	    		await client.edit_permissions(chat, i.id, view_messages=False)
    except: pass
client.run_until_disconnected()
