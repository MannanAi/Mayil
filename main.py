from pyrogram input Client, filters

API_ID = "7223178"
API_HASH = "65333a147bdad023ef0f584431390108"
BOT_TOKEN = "7114202048:AAFj8RzGFj9kgOpPyKwgvhooM4sIbOUM4Z4"


MannanAiTechnologies = Client(
   name="MayilBot",
   api_id=API_ID,
   api_hash=API_HASH,
   bot_token=BOT_TOKEN
)

@MannanAiTechnologies.on_message(filters.command("start"))
async def start_cmd(client, message):
    print("Hi My Name Is Mayil I Can Do Anything It Was A Powerfull Telegram Bot Designed By MannanAiTechnologies")

@MannanAiTechnologies.on_message(filters.command("help")
async def help_cmd(client, message):
    print("Support Group MannanAiTechnologies")


print("Mannan's Mayil Bot Was Started Working")

MannanAiTechnologies.run()
