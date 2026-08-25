import discord
from discord.ext import commands

import config

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}.")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commandes synchronisées")
    except Exception as e:
        print(f"Erreur lors de la synchronisation des commandes : {e}")

if __name__ == "__main__":
    bot.run(config.TOKEN)