import discord
from discord.ext import commands

import config

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user} (ID : {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commandes synchronisées")
    except Exception as e:
        print(f"Erreur lors de la synchronisation des commandes : {e}")

if __name__ == "__main__":
    bot.run(config.TOKEN)