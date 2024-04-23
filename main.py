import discord, os, requests
from discord import app_commands, interactions
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="d!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="checkserver")
async def checkserver(interaction: discord.Interaction):
    spyPetScan = requests.get(f"https://kickthespy.pet/getBot?id={interaction.guild_id}")
    scanJson = spyPetScan.json()

    if "error" in scanJson and scanJson["error"] == "Bot not found":
        await interaction.response.send_message("No spy bots found in the server!")
    elif "id" in scanJson:
        await interaction.response.send_message(f"**WARNING:** A bot has been found with the user id: {scanJson["id"]}")

        @bot.tree.command(name="checkserver")

bot.run(os.getenv("TOKEN"))