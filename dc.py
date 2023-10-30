import discord
from main import pass_make
# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$10 digit password'):
        await message.channel.send(pass_make(10))
    else:
        await message.channel.send(message.content)

client.run("MTE2MzQ1NjE3MzU1MTM5ODk3Mg.GezB-7.OlSyMYGfM9-4iZD0Lh35UuQ0SOMPfoe0FTt_bk")