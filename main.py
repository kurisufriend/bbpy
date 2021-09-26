import discord
import asyncio
from io import StringIO
from contextlib import redirect_stdout

print(discord.__version__)
dclient = discord.Client()

exec_env_global = dict()
exec_env_local = dict()

@dclient.event
async def on_message(message):
    if message.content.startswith(".bbpy "):
        message.content = message.content.replace(".bbpy ", "")
        print(message.content)
        try:
            f = StringIO()
            with redirect_stdout(f):
                exec(message.content, exec_env_global, exec_env_local)
            await message.channel.send(f.getvalue())
        except Exception as e:
            await message.channel.send(type(e).__name__+str(e.args))


dclient.run("token", bot=True)
