import os
import time
import psutil
import shutil
import string
import asyncio
import config
from asyncio import TimeoutError
from helper.database.access_db import db
from helper.broadcast import broadcast_handler
from helper.database.add_user import AddUserToDatabase
from helper.display_progress import humanbytes
from pyrogram import Client, filters, StopPropagation
from helper.forcesub import ForceSub
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

START_ANIMATION = "https://telegra.ph/file/99a290331575e4c2d60d7.mp4"

@Client.on_message(filters.command(["start"]), group=-2)
async def start(client, message):
    await AddUserToDatabase(client, message)
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return 
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Developerπ§βπ»", url="https://t.me/naviya2"),
        InlineKeyboardButton("Rate us β", url="https://t.me/tlgrmcbot?start=leoyoutubedownloaderbot-review")],
        
        [InlineKeyboardButton("Updates Channel π£", url="https://t.me/new_ehi"),
        InlineKeyboardButton("Support Group π₯", url="https://t.me/leosupportx")],
        
        [InlineKeyboardButton("Totorial Video π«", url="https://t.me/new_ehi/353")],
        
        [InlineKeyboardButton("β Add me to your group β", url="https://t.me/leoyoutubedownloaderbot?startgroup=true")]
    ])
    await message.reply_animation(
        START_ANIMATION,
        caption="Hello{}π\n\nYou are Warmly welcome to Leo YT Downloader Bot π±π°</b>\n\nIf you want to know how i works just hit on /help command π".format(message.from_user.mention),
        reply_markup=joinButton
    )
