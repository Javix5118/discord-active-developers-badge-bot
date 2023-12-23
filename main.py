import discord
from discord.ext import commands
from time import sleep
import os
from time import sleep
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN_KEY')
CHANNEL = os.getenv('CHANNEL_KEY')
sleep(5)
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client = discord.Client(intents=discord.Intents.all())
@bot.event
async def on_ready():
    channel = bot.get_channel(int(CHANNEL))
    await channel.send('Hey, welcome to the **Badge Active Program Easy Method**')
    sleep(2)
    await channel.send('Turn this community into a public one')
    sleep(1)
    await channel.send("Use this command in order to enable the slash command in case it doesn't appear -> **!sync**")
    await channel.send('And then send the following command -> **/test**')
@bot.command()
async def sync(ctx):
    await bot.tree.sync()
    await ctx.send('SLASH COMMANDS READY!')


@bot.tree.command(name='test', description='Use this command')
async def pry(interaction: discord.Interaction):
    await interaction.response.send_message("I'M WORKING!")
    await interaction.response.send_message("Now you'll have to wait some days, until you are able to claim the badge here -> https://discord.com/developers/active-developer")

bot.run(TOKEN)