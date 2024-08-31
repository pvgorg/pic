#!/usr/bin/python3

from telethon import TelegramClient, events
from os import listdir
from json import load, dump
from random import choice
import asyncio

api_id = 25817106 #Edit
api_hash = "2991b6efb8f4c2debe13e5948ce9c9cd" #Edit
client = TelegramClient('Atakeri', api_id, api_hash)

async def main():
    await client.start()
    await client.send_message('me', '✅ Successfully ran the bot on your account. You can send `Help` to receive the bot commands. Thank you, dev Alireza.\n\n🆔 @La_shy')
    print(await client.download_profile_photo('me'))

AdminBot = 1502490631 #Edit
foshall_list = []
enemyall_list = []

@client.on(events.NewMessage(pattern=r"AddFosh (.*)", from_users=AdminBot))
async def add_name(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str in foshall_list:
        await event.edit(f"**Fosh ( {input_str} ) is already in the list!**")
    else:
        foshall_list.append(input_str)
        await event.edit(f"**Fosh ( {input_str} ) added to the list!**")

@client.on(events.NewMessage(pattern=r"DelFosh (.*)", from_users=AdminBot))
async def del_name(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str not in foshall_list:
        await event.edit(f"**Fosh ( {input_str} ) is not in the list!**")
    else:
        foshall_list.remove(input_str)
        await event.edit(f"**Fosh ( {input_str} ) removed from the list!**")

@client.on(events.NewMessage())
async def clean_name(event):
    if event.raw_text == "ClearFosh" and event.sender_id == AdminBot:
        if not foshall_list:
            await event.edit("**Fosh List is already empty!**")
        else:
            foshall_list.clear()
            await event.edit("**Fosh List has been cleared!**")

@client.on(events.ChatAction)
async def leftMember(event):
    if event.user_joined:
        await event.reply("Welcome to the group!\nCreator Channel Atakeri")

@client.on(events.NewMessage())
async def timebio_on(event):
    if event.raw_text == "Help" and event.sender_id == AdminBot:
        await event.edit("**Welcome to Enemy Help!**\n\n**Instructions:**\nTo add an enemy, you must add at least one insult. You can also add a heart instead of an insult. Future updates will allow both hearts and enemies to be added!\n\nTo add an enemy (reply to a message): `SetEnemy`\nTo remove an enemy: `DelEnemy`\nTo clear all enemies: `ClearEnemy`\nTo set a new insult: `AddFosh (Text)`\nTo remove an insult: `DelFosh (Text)`\nTo clear all insults: `ClearFosh`\n\n**Dev : @La_shy**")

@client.on(events.NewMessage(from_users=AdminBot))
async def set_enemy(event):
    if event.raw_text.lower() == "setenemy":
        replied = await event.get_reply_message()
        if replied:
            sender_id = replied.sender.id
            if sender_id in enemyall_list:
                await event.edit("**User is already an enemy!**")
            else:
                enemyall_list.append(sender_id)
                await event.edit("**User has been set as an enemy!**")
    elif event.raw_text.lower() == "delenemy":
        replied = await event.get_reply_message()
        if replied:
            sender_id = replied.sender.id
            if sender_id not in enemyall_list:
                await event.edit("**User is not an enemy!**")
            else:
                enemyall_list.remove(sender_id)
                await event.edit("**User has been removed from enemies!**")

@client.on(events.NewMessage())
async def clear_enemy(event):
    if event.raw_text == "ClearEnemy" and event.sender_id == AdminBot:
        if not enemyall_list:
            await event.edit("**Enemy List is already empty!**")
        else:
            enemyall_list.clear()
            await event.edit("**Enemy List has been cleared!**")

@client.on(events.NewMessage)
async def enemy(event):
    if event.sender_id in enemyall_list:
        await event.reply(choice(foshall_list))

asyncio.run(main())
