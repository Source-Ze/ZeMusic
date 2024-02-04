import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#       #             #  #####  #####      ####
#        #           #  #         #            #     #
#          #        #  #####   #            #####     
#           #    #    #          #     ##    #     #
#              #       #####   ######   #     #
                
                
@app.on_message(
    command(["المطور","مودي","مطور السورس","المطور مودي"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/96857cb597b588139fdd5.jpg",
        caption=f"""**⩹━★⊷━⌞ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم التواصل مع مطور زد إي ميوزك\nللتحدث مع مطور السورس اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𐇮 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮", url=f"https://t.me/ELHYBA"), 
                 ],[
                   InlineKeyboardButton(
                        "★⌞ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱 ⌝⚡", url=f"https://t.me/Source_Ze"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["مودي انجم","احمد","مودي","مبرمج","المبرمج مودي","المبرمج" ,"المطور"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("ELHYBA")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱 ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["المطور مودي الشيطان"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("ELHYBA")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱 ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["مودي انجم","مودي",])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("ELHYBA")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱 ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/96857cb597b588139fdd5.jpg",
        caption=f"""**⩹⊷━⌞ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس زد إي\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𐇮 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮", url=f"https://t.me/ELHYBA"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱 ⌝⚡", url=f"https://t.me/Source_Ze"),
                ],

            ]

        ),

    )



    
