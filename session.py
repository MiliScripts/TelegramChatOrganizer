from pyrogram import Client
from dotenv import load_dotenv
import os
from colorama import init, Fore, Style

init(autoreset=True)

load_dotenv()

try:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
except (ValueError, KeyError) as e:
    print(f"{Fore.RED}Error: Could not read API_ID or API_HASH from environment variables.{Style.RESET_ALL}")
    exit(1)

app = Client("my_account", api_id=API_ID, api_hash=API_HASH, in_memory=True)

async def main():
    async with app:
        string_session = await app.export_session_string()
        print(f"{Fore.GREEN}Session String:{Style.RESET_ALL} {string_session}")
        await app.send_message("me", f"{Fore.YELLOW}**Here is Your Session:**{Style.RESET_ALL}\n\n<code>{string_session}</code>")

app.run(main())
