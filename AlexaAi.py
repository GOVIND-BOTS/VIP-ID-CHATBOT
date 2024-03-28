from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import random
import os
from pymongo import MongoClient

API_ID = "your_api_id"
API_HASH = "your_api_hash"
SESSION_NAME = "your_session_name"
MONGO_URL = os.environ.get("MONGO_URL", "")

client = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)


@client.on_message(
    filters.command("alive", prefixes=["/", ".", "?", "-"]) & ~filters.private
)
async def start(client, message):
    await message.reply_text("**ᴀʟᴇxᴀ ᴀɪ ᴜsᴇʀʙᴏᴛ ғᴏʀ ᴄʜᴀᴛᴛɪɴɢ ɪs ᴡᴏʀᴋɪɴɢ**")


@client.on_message(
    (filters.text | filters.sticker)
    & ~filters.private
    & ~filters.me
    & ~filters.bot
)
async def alexaai(client: Client, message: Message):
    chatdb = MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]

    if not message.reply_to_message:
        alexadb = MongoClient(MONGO_URL)
        alexa = alexadb["AlexaDb"]["Alexa"]
        is_alexa = alexa.find_one({"chat_id": message.chat.id})
        if not is_alexa:
            await client.send_chat_action(message.chat.id, "typing")
            K = []
            is_chat = chatai.find({"word": message.text})
            k = chatai.find_one({"word": message.text})
            if k:
                for x in is_chat:
                    K.append(x["text"])
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text["check"]
                if Yo == "sticker":
                    await message.reply_sticker(f"{hey}")
                if not Yo == "sticker":
                    await message.reply_text(f"{hey}")

    if message.reply_to_message:
        alexadb = MongoClient(MONGO_URL)
        alexa = alexadb["AlexaDb"]["Alexa"]
        is_alexa = alexa.find_one({"chat_id": message.chat.id})
        getme = await client.get_me()
        user_id = getme.id
        if message.reply_to_message.from_user.id == user_id:
            if not is_alexa:
                await client.send_chat_action(message.chat.id, "typing")
                K = []
                is_chat = chatai.find({"word": message.text})
                k = chatai.find_one({"word": message.text})
                if k:
                    for x in is_chat:
                        K.append(x["text"])
                    hey = random.choice(K)
                    is_text = chatai.find_one({"text": hey})
                    Yo = is_text["check"]
                    if Yo == "sticker":
                        await message.reply_sticker(f"{hey}")
                    if not Yo == "sticker":
                        await message.reply_text(f"{hey}")
        if not message.reply_to_message.from_user.id == user_id:
            if message.sticker:
                is_chat = chatai.find_one(
                    {"word": message.reply_to_message.text, "id": message.sticker.file_unique_id}
                )
                if not is_chat:
                    chatai.insert_one(
                        {
                            "word": message.reply_to_message.text,
                            "text": message.sticker.file_id,
                            "check": "sticker",
                            "id": message.sticker.file_unique_id,
                        }
                    )
            if message.text:
                is_chat = chatai.find_one(
                    {"word": message.reply_to_message.text, "text": message.text}
                )
                if not is_chat:
                    chatai.insert_one(
                        {"word": message.reply_to_message.text, "text": message.text, "check": "none"}
                    )


@client.on_message(
    (filters.sticker | filters.text)
    & ~filters.private
    & ~filters.me
    & ~filters.bot
)
async def alexastickerai(client: Client, message: Message):
    chatdb = MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]

    if not message.reply_to_message:
        alexadb = MongoClient(MONGO_URL)
        alexa = alexadb["AlexaDb"]["Alexa"]
        is_alexa = alexa.find_one({"chat_id": message.chat.id})
        if not is_alexa:
            await client.send_chat_action(message.chat.id, "typing")
            K = []
            is_chat = chatai.find({"word": message.sticker.file_unique_id})
            k = chatai.find_one({"word": message.text})
            if k:
                for x in is_chat:
                    K.append(x["text"])
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text["check"]
                if Yo == "text":
                    await message.reply_text(f"{hey}")
                if not Yo == "text":
                    await message.reply_sticker(f"{hey}")

    if message.reply_to_message:
        alexadb = MongoClient(MONGO_URL)
        alexa = alexadb["AlexaDb"]["Alexa"]
        is_alexa = alexa.find_one({"chat_id": message.chat.id})
        getme = await client.get_me()
        user_id = getme.id
        if message.reply_to_message.from_user.id == user_id:
            if not is_alexa:
                await client.send_chat_action(message.chat.id, "typing")
                K = []
                is_chat = chatai.find({"word": message.text})
                k = chatai.find_one({"word": message.text})
                if k:
                    for x in is_chat:
                        K.append(x["text"])
                    hey = random.choice(K)
                    is_text = chatai.find_one({"text": hey})
                    Yo = is_text["check"]
                    if Yo == "text":
                        await message.reply_text(f"{hey}")
                    if not Yo == "text":
                        await message.reply_sticker(f"{hey}")
        if not message.reply_to_message.from_user.id == user_id:
            if message.text:
                is_chat = chatai.find_one(
                    {"word": message.reply_to_message.sticker.file_unique_id, "text": message.text}
                )
                if not is_chat:
                    toggle.insert_one(
                        {"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"}
                    )
            if message.sticker:
                is_chat = chatai.find_one(
                    {"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id}
                )
                if not is_chat:
                    chatai.insert_one(
                        {"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"}
                    )


@client.on_message(
    (filters.text | filters.sticker)
    & filters.private
    & ~filters.me
)
