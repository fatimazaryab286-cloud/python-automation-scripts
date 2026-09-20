import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

load_dotenv()
token=os.getenv('DISCORD_BOT_TOKEN')

intents=discord.Intents.default()
intents.message_content=True

bot=commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f"you are ready to go in {bot.user.name}")

@bot.command(description="reminds to study python")             
async def remind(ctx,*,arg):
    await ctx.send(f"Reminder set: {arg}")

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
      await ctx.send("You forgot to include a required Argument!")
    elif isinstance(error,commands.CommandNotFound):
        pass #ignore unknown commands
    else:
        raise error

bot.run(token)