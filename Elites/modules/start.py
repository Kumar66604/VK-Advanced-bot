import random
from pyrogram import filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_USERNAME
from Elites import Elites as app
from Elites.core.strings import (music_txt, ai_txt, bass_txt, youtube_txt, 
misc_txt, broadcast_txt, checker_txt, devs_txt, instagram_txt)
from .broadcast import add_user

TheChampu = ["https://telegra.ph/file/9b4d1991f91bbe315ba9d.jpg" , "https://telegra.ph/file/ffb8584f80050fad3137a.jpg" , "https://telegra.ph/file/c98991272535959225f4a.jpg", "https://telegra.ph/file/2559e93cbe76fd859864c.jpg" , "https://telegra.ph/file/3ebad940c543da336da50.jpg" , "https://telegra.ph/file/d856178ed8e3f7bee5330.jpg" , "https://telegra.ph/file/cda2318c33031362b397a.jpg" , "https://telegra.ph/file/ae2b33b387846f46f2e79.jpg" , "https://telegra.ph/file/cda2318c33031362b397a.jpg" , "https://telegra.ph/file/ae2b33b387846f46f2e79.jpg" ,  "https://telegra.ph/file/51e1ff97dc84e4a111f1f.jpg" , "https://telegra.ph/file/3352cdeb623e2e5700252.jpg" , "https://telegra.ph/file/bcd77d1897f475940b884.jpg" , "https://telegra.ph/file/498910d26fa0ac18bd40f.jpg" , "https://telegra.ph/file/6c7915de931103cf47df9.jpg" , "https://telegra.ph/file/38eb88d3a7f926ed1df58.jpg" , "https://telegra.ph/file/6f88fc6fdab2570cc16bc.jpg"]
# ------------------------------------------------------------------------------- #

start_txt = """
**ʜᴇʟʟᴏ** {} 

**🎵✨ ɪ ᴀᴍ ʏᴏᴜʀ ᴡᴧɪғᴜ, ᴅᴇʟɪᴠᴇʀɪɴɢ ғʟᴀᴡʟᴇss ʙᴇᴀᴛs ᴡɪᴛʜ ᴢᴇʀᴏ ʟᴀɢ. ᴍᴏʀᴇ ᴛʜᴀɴ ᴀ ᴍᴜsɪᴄ ʙᴏᴛ, ɪ'ᴍ ᴛʜᴇ sʏᴍᴘʜᴏɴʏ ᴏғ ᴛʜᴇ ғᴜᴛᴜʀᴇ, ᴄᴜsᴛᴏᴍ-ᴍᴀᴅᴇ ғᴏʀ ʏᴏᴜʀ ᴍᴜsɪᴄᴀʟ ʙʟɪss. ʟᴇᴛ's ᴅɪᴠᴇ ɪɴᴛᴏ ᴀ ᴡᴏʀʟᴅ ᴡʜᴇʀᴇ ᴇᴠᴇʀʏ ɴᴏᴛᴇ ʀᴇsᴏɴᴀᴛᴇs ᴡɪᴛʜ ᴘᴇʀғᴇᴄᴛɪᴏɴ, ᴀɴᴅ ᴇᴠᴇʀʏ ʀʜʏᴛʜᴍ ɪɢɴɪᴛᴇs ʏᴏᴜʀ sᴏᴜʟ! 💖🌟.**
"""

# ------------------------------------------------------------------------------- #

button = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),    
        ],
        [
            InlineKeyboardButton("↯ ᴄᴏᴍᴍᴀɴᴅs ↯", callback_data="help_"),    
        ],
        [
            InlineKeyboardButton("☆ ᴍʏ ʙᴧʙᴇ ☆", url=f"https://t.me/ll_anime_dp_ll"),    
        ]
])



# ------------------------------------------------------------------------------- #

help_txt = """**
**» ˹ᴡᴧɪғᴜ˼ ᴄᴏᴏʟ ᴏʀ ᴇxᴄʟᴜsɪᴠᴇ ғᴇᴀᴛᴜʀᴇs** 
"""



# ------------------------------------------------------------------------------- #

Waifu_buttons = [              
                [
                    InlineKeyboardButton("ᴍᴜsɪᴄ", callback_data="music_"),   
                    InlineKeyboardButton("ᴀɪ", callback_data="ai_"),
                    InlineKeyboardButton("ʙᴀss", callback_data="bass_")
                ],
                [
                    InlineKeyboardButton("ʏᴏᴜᴛᴜʙᴇ", callback_data="youtube_"),   
                    InlineKeyboardButton("ᴍɪsᴄ", callback_data="misc_"),
                    InlineKeyboardButton("ʙʀᴏᴀᴅᴄᴀsᴛ", callback_data="broadcast_")
                ],
                [
                    InlineKeyboardButton("ᴄʜᴇᴄᴋᴇʀ", callback_data="checker_"),   
                    InlineKeyboardButton("ᴅᴇᴠs", callback_data="devs_"),
                    InlineKeyboardButton("ɪɴsᴛᴀɢʀᴀᴍ", callback_data="instagram_")
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home_"),
                    InlineKeyboardButton("⟲ ᴄʟᴏꜱᴇ ⟳", callback_data="close_data")
                ]
                ]


back_buttons  = [[
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_"),                    
                ]]




@app.on_message(filters.command("start"))
async def start(_, m: Message):
        add_user(m.from_user.id)
        waifu = random.choice(TheChampu)
        await message.reply_photo(photo=waifu,
                                  caption=start_txt.format(message.from_user.mention),reply_markup=button)



@app.on_callback_query()
async def cb_handler(client, query):
    if query.data=="home_":
        buttons =  [
            [
                InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
            [
                InlineKeyboardButton("↯ ᴄᴏᴍᴍᴀɴᴅs ↯", callback_data="help_")
            ],
            [
            InlineKeyboardButton("☆ ᴍʏ ʙᴧʙᴇ ☆", url=f"https://t.me/ll_ANIME_DP_ll"),    
            ]    
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                start_txt.format(query.from_user.mention),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


# ------------------------------------------------------------------------------- #
        
    elif query.data=="help_":        
        reply_markup = InlineKeyboardMarkup(Waifu_buttons)
        try:
            await query.edit_message_text(
                help_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

        
    elif query.data=="music_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                music_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="ai_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                ai_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="bass_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                bass_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="youtube_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                youtube_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

        
        
    elif query.data=="misc_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                misc_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


        
    elif query.data=="broadcast_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                broadcast_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="checker_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                checker_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

        
    elif query.data=="devs_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                devs_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass        



    elif query.data=="instagram_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                instagram_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

        
# ------------------------------------------------------------------------------- #

    elif query.data=="maintainer_":
            await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)

  
# ------------------------------------------------------------------------------- #
 
    elif query.data=="close_data":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass
