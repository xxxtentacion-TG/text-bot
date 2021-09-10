import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import CallbackQuery

bot = Client(
  "message-bot",
  bot_token="1569220761:AAH3eK_MBassa72hUyGy2DP07e32pfqmTIU",
  api_id="3020564",
  api_hash="91c026fadfdc442f504a0bd3e5c8cd18",
  )
  
@bot.on_message(filters.command(['start']))
def start(client, message):
    message.reply(f"hey bruhh how are you)",
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton('𝙂𝙍𝙊𝙐𝙋 💬', url='https://t.me/MGMOVIEGRAM'),
          InlineKeyboardButton('𝙂𝙍𝙊𝙐𝙋 💬', url='https://t.me/MGMOVIEGRAM')
        ],
        [
          InlineKeyboardButton('𝙂𝙍𝙊𝙐𝙋 💬', url='https://t.me/MGMOVIEGRAM')
        ]
      ]
      )
      
bot.run()
          
