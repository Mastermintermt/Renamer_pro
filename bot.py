from pyrogram import Client
from configs import API_ID,API_HASH,BOT_TOKEN,LOG_CHANNEL,MONGODB_URI,PRO_USERS,OWNER_ID
from route import web_server
from aiohttp import web

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="simple-renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            log_channel=LOG_CHANNEL,
            mongodb_url=MONGODB_URI,
            pro_users=PRO_USERS,
            owner_id=OWNER_ID,
            workers=100,
            plugins={"root": "main"},
            sleep_threshold=10,
        )
    async def start(self):
        await super().start()
        me = await self.get_me()   
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        port = "8080"
        await web.TCPSite(app, bind_address, port).start()   
        print(f"{me.first_name} | @{me.username} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳...⚡️")
       
    async def stop(self, *args):
       await super().stop()      
       print("Bot Restarting........")


bot = Bot()
bot.run()
