import discord
from discord.ext import commands
import random

# Ustawienie intents
intents = discord.Intents.default()
intents.messages = True  # Włączenie nasłuchiwania wiadomości
intents.message_content = True  # Włączenie dostępu do treści wiadomości

# Tworzymy instancję bota z prefiksem komend i intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Gdy bot zostanie uruchomiony
@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')

# Event: Logowanie otrzymywanych wiadomości do debugowania
@bot.event
async def on_message(message):
    print(f"Otrzymano wiadomość: {message.content}")  # Wypisanie każdej wiadomości
    # Jeśli wiadomość jest od bota, nie przetwarzamy jej jako komendy
    if message.author == bot.user:
        return
    # Przetwarzanie komend
    await bot.process_commands(message)

# Komenda: Powitanie
@bot.command()
async def hello(ctx):
    await ctx.send('Cześć! Jestem botem na Discordzie.')

# Komenda: Prosta gra "rzuć kością"
@bot.command()
async def dice(ctx):
    roll = random.randint(1, 6)
    await ctx.send(f'Wynik rzutu kostką: {roll}')

# Komenda: Losowanie mapy
@bot.command()
async def map(ctx):
    maps = ['Mirage', 'Dust II', 'Inferno', 'Nuke', 'Overpass', 'Train', 'Vertigo']  # Lista dostępnych map
    chosen_map = random.choice(maps)  # Losowanie mapy
    await ctx.send(f'Mapa na której gramy to: {chosen_map}')


# Uruchomienie bota
bot.run('MÓJ TOKEN')
