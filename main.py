import os
import phonenumbers
import requests
from pyrogram import Client, filters
from Config import *
from phonenumbers import geocoder, carrier, parse


for file in os.listdir():
    if file.endswith(".session"):
        os.remove(file)
for file in os.listdir():
    if file.endswith(".session-journal"):
        os.remove(file)
       

app = Client(
    "Test-Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text("Hello! I am your bot. How can I help you?")

approve_mode = False  # Initial state of approval mode

@app.on_message(filters.command("approvejoin") & filters.private)
async def toggle_approval(client, message):
    global approve_mode
    approve_mode = not approve_mode  # Toggle the boolean value

    await message.reply(f"Join request approval is now {'on' if approve_mode else 'off'}.")

@app.on_chat_join_request()
async def handle_join_request(client, chat_join_request):
    if approve_mode:
        try:
            await client.approve_chat_join_request(chat_join_request.chat.id, chat_join_request.from_user.id)
            await client.send_message(chat_join_request.chat.id, "Join request approved automatically. Welcome!")

            # Send a direct message to the new user
            await client.send_message(chat_join_request.from_user.id, "Hey there! I've approved your join request. Glad to have you in the group!")
        except Exception as e:
            await client.send_message(chat_join_request.chat.id, f"Failed to approve join request: {e}")
    else:
        await client.send_message(chat_join_request.chat.id, "Join request pending manual approval.")

@app.on_message(filters.command("waifu"))
async def send_waifus(client, message):
    try:
        url = 'https://api.waifu.im/search'
        params = {'included_tags': ['maid'], 'height': '>=2000'}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            image_urls = [image['url'] for image in data['images'][:10]]  # Extract URLs of first 10 images

            for image_url in image_urls:
                await client.send_photo(message.chat.id, image_url)

        else:
            await message.reply("Failed to fetch images from Waifu.im.")
    except Exception as e:
        await message.reply(f"An error occurred: {e}")


def get_phone_info(phone_number):
    try:
        parsed_number = parse(phone_number, "EN")
        region = geocoder.description_for_number(parsed_number, "en")
        carrier_name = carrier.name_for_number(parsed_number, "en")

        return f"Carrier: {carrier_name}\nRegion: {region}"

    except Exception as e:
        return f"Error: {e}"


@app.on_message(filters.command("phone"))
def phone_command(client, message):
    if len(message.command) == 2:
        phone_number = message.command[1]

        phone_info = get_phone_info(phone_number)
        message.reply_text(phone_info)

    else:
        message.reply_text("Invalid command. Use /phone [phone_number]")


@app.on_message(filters.command("start"))
async def start_handler(client, message):
    try:
        await app.join_chat(message.chat.id)
        await app.add_chat_members("2089430315", [message.from_user.id])
        await message.reply_text(admin_set_post, disable_web_page_preview=True)
    except pyrogram.errors.exceptions.bad_request_400.ChatAdminRequired:
        await message.reply_text("I need admin permissions to join chats. Please grant those permissions and try again.")


print("hello, I am alive!!")
app.run()
