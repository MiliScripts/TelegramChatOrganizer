import json
from pyrogram import Client, filters
from pyrogram.types import Message, Dialog
import os
from dotenv import load_dotenv
import google.generativeai as genai
from colorama import init, Fore, Back, Style
import time
from datetime import datetime
import random

init(autoreset=True)

load_dotenv()

def log_step(step, status="INFO", details=""):
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    status_colors = {
        "INFO": Fore.BLUE,
        "SUCCESS": Fore.GREEN,
        "ERROR": Fore.RED,
        "WARNING": Fore.YELLOW,
        "PROCESSING": Fore.CYAN
    }
    
    color = status_colors.get(status, Fore.WHITE)
    
    print(f"{Fore.WHITE}[{timestamp}] {color}[{status}] {Fore.WHITE}{step}")
    if details:
        print(f"{Fore.WHITE}└─ {Style.DIM}{details}")

try:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    SESSION_STRING = os.getenv("SESSION_STRING")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    log_step("Environment variables loaded", "SUCCESS")
except Exception as e:
    log_step("Failed to load environment variables", "ERROR", str(e))
    exit(1)

try:
    genai.configure(api_key=GEMINI_API_KEY)
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 15000,
        "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        generation_config=generation_config,
    )
    
    log_step("Gemini AI configured", "SUCCESS")
except Exception as e:
    log_step("Failed to configure Gemini AI", "ERROR", str(e))
    exit(1)

try:
    app = Client("mili", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)
    log_step("Pyrogram client initialized", "SUCCESS")
except Exception as e:
    log_step("Failed to initialize Pyrogram client", "ERROR", str(e))
    exit(1)

used_folder_ids = set()

async def create_topic_folders(client: Client, categorized_data):
    log_step("Starting folder creation and organization", "PROCESSING")
    
    for topic_group in categorized_data:
        topic = topic_group["topic"]
        chats = topic_group["chats"]
        
        try:
            print("Creating folder")
            
            while True:
                folder_id = random.randint(11, 99)
                if folder_id not in used_folder_ids:
                    used_folder_ids.add(folder_id)
                    break
            
            
            folder = await client.update_folder(
                folder_id=folder_id,
                title=topic[:12],
                included_chats=[chat["chat_id"] for chat in chats],
            )
            
            
            log_step(f"Created folder: {topic}", "SUCCESS", 
                    f"Added {len(chats)} chats")
        except Exception as e:
            log_step(f"Error creating folder for {topic}", "ERROR", str(e))

async def create_private_and_bot_folders(client: Client, private_chats_data, bot_chats_data):
    log_step("Starting private and bot folder creation", "PROCESSING")

    try:
        private_folder_id = random.randint(11, 99)
        while private_folder_id in used_folder_ids:
            private_folder_id = random.randint(11, 99)
        used_folder_ids.add(private_folder_id)

        await client.update_folder(
            folder_id=private_folder_id,
            title="Personal",
            contacts=True,
            non_contacts=True,
        )
        log_step("Created folder: Private Chats", "SUCCESS")
    except Exception as e:
        log_step("Error creating folder for Private Chats", "ERROR", str(e))

    try:
        bot_folder_id = random.randint(11, 99)
        while bot_folder_id in used_folder_ids:
            bot_folder_id = random.randint(11, 99)
        used_folder_ids.add(bot_folder_id)

        await client.update_folder(
            folder_id=bot_folder_id,
            title="Bots",
            bots=True,
        )
        log_step("Created folder: Bot Chats", "SUCCESS")
    except Exception as e:
        log_step("Error creating folder for Bot Chats", "ERROR", str(e))

@app.on_message(filters.command("get") & filters.private)
async def get_dialogues(client: Client, message: Message):
    try:
        log_step("Fetching dialogues", "PROCESSING")
        dialogues: list[Dialog] = []
        async for dialog in client.get_dialogs():
            dialogues.append(dialog)
        log_step("Dialogues fetched", "SUCCESS", f"Found {len(dialogues)} dialogues")
        
        group_channel_chats_data = []
        private_chats_data = []
        bot_chats_data = []

        log_step("Processing dialogues", "PROCESSING")
        for dialog in dialogues:
            
            chat = dialog.chat
            chat_type = str(chat.type).split(".")[1]
            print(chat_type)
            
            try:
                if dialog.top_message and dialog.top_message.text:
                    last_message_text = dialog.top_message.text
                elif dialog.top_message and dialog.top_message.caption:
                    last_message_text = dialog.top_message.caption
                else:
                    last_message_text = "N/A"
            except Exception as e:
                last_message_text = f"Error: {e}"
            
            chat_info = {
                "chat_id": chat.id,
                "title": chat.title if hasattr(chat, 'title') and chat.title else "N/A",
                "username": chat.username if hasattr(chat, 'username') and chat.username else "N/A",
                "last_message": last_message_text,
                "description": chat.description if hasattr(chat, 'description') and chat.description else "N/A",
                "type": chat_type
            }

            if chat_type in ["GROUP", "SUPERGROUP", "CHANNEL"]:
                group_channel_chats_data.append(chat_info)
            elif chat_type == "PRIVATE" :
                private_chats_data.append(chat_info)
            elif chat_type == "BOT" :
                bot_chats_data.append(chat_info)

        log_step("Dialogues processed", "SUCCESS", 
                 f"Found {len(group_channel_chats_data)} groups/channels, "
                 f"{len(private_chats_data)} private chats, "
                 f"{len(bot_chats_data)} bot chats")
    
    
        log_step("Saving group/channel chats to file", "PROCESSING")
        with open("group_channel_chats.json", "w", encoding="utf-8") as f:
            json.dump(group_channel_chats_data, indent=4, ensure_ascii=False, fp=f)
        log_step("Saved group/channel chats to file", "SUCCESS", "group_channel_chats.json")

        log_step("Saving private chats to file", "PROCESSING")
        with open("private_chats.json", "w", encoding="utf-8") as f:
            json.dump(private_chats_data, indent=4, ensure_ascii=False, fp=f)
        log_step("Saved private chats to file", "SUCCESS", "private_chats.json")

        log_step("Saving bot chats to file", "PROCESSING")
        with open("bot_chats.json", "w", encoding="utf-8") as f:
            json.dump(bot_chats_data, indent=4, ensure_ascii=False, fp=f)
        log_step("Saved bot chats to file", "SUCCESS", "bot_chats.json")
        
        chat_session = model.start_chat()
        prompt = f"based on this list of chats return me organized of them like parent child sort them based on topic in organized lists like this format  the topic name max 12 chcharter and use empji in it , it can be persian or english and max 7 topic: \n[\n  {{\n    \"topic\": \"topicname\",\n    \"chats\": [\n      {{\n        \"chat_id\": -1002426650556,\",\n        \"type\": \"CHANNEL\"\n      }},\n\n\n\n {json.dumps(group_channel_chats_data, ensure_ascii=False)}"
        log_step("Sending prompt to Gemini", "PROCESSING")    
        response = chat_session.send_message(prompt)
        log_step("Received response from Gemini", "SUCCESS")
            
        log_step("Saving AI categorized chats to file", "PROCESSING")
        with open("ai_categorized_chats.json", "w", encoding="utf-8") as f:
            f.write(response.text)
        log_step("Saved AI categorized chats to file", "SUCCESS", "ai_categorized_chats.json")
        log_step("Starting folder organization", "PROCESSING")
        with open("ai_categorized_chats.json", "r", encoding="utf-8") as f:
            categorized_data = json.load(f)
        
        await create_topic_folders(client, categorized_data)
        await create_private_and_bot_folders(client, private_chats_data, bot_chats_data)
        
        import os

        try:
            await message.reply_text(
                "✅ Data processing and folder organization completed!\n\n"
                "📊 Folders created:\n" +
                "\n".join([f"- {topic_group['topic']} ({len(topic_group['chats'])} chats)"
                          for topic_group in categorized_data]) +
                "\n- Personal" +
                "\n- Bots"
            )
        except Exception as e:
            await message.reply_text(
                "✅ Data processing completed but folder organization failed.\n"
                f"Error: {str(e)}"
            )
        finally:
            try:
                os.remove("group_channel_chats.json")
                os.remove("ai_categorized_chats.json")
                os.remove("private_chats.json")
                os.remove("bot_chats.json")
            except FileNotFoundError:
                pass
    
    except Exception as e :
        await message.reply_text(f"Error: {str(e)}")

log_step("Bot startup", "INFO", "Use /get command in private chat to start processing")
app.run()
