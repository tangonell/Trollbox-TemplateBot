import asyncio
import html

from socketio import AsyncClient

class TemplateBot:
    HEADERS: dict[str, str] = {
        "Accept": "*/*",
        "Accept-Encoding": "identity",
        "Accept-Language": "*",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "null=null",
        "Host": "www.windows93.net",
        "Origin": "http://www.windows93.net",
        "Pragma": "no-cache",
        "Referer": "http://www.windows93.net/trollbox/index.php",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }

    def __init__(self):
        self.socket: AsyncClient = AsyncClient()
        self.socket.on("_connected", self.connect)
        self.socket.on("message", self.message)
    
    async def connect(self):
        await self.socket.emit("user joined", ("TemplateBot", "pink;TemplateBot", "", ""))
    
    async def message(self, data):
        data["msg"] = html.unescape(data["msg"])
        data["nick"] = html.unescape(data["nick"])

        if data["msg"] == "t!hello":
            await self.socket.send(f"Hello, {data["nick"]}!")

async def main():
    bot: TemplateBot = TemplateBot()
    await bot.socket.connect("http://www.windows93.net:8081", headers=bot.HEADERS)
    await bot.socket.wait()

if __name__ == "__main__":
    asyncio.run(main())
