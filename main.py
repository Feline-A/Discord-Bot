import discord
from discord.ext import commands
import random
import requests
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

@bot.command()
async def coin(ctx):
    coin = random.randint(1, 3)
    if coin == 1:
        await ctx.send("Head")
    if coin == 2:
        await ctx.send("Tail")

@bot.command()
async def animals(ctx):
    img_name = random.choice(os.listdir('images/animal1'))
    with open(f'images/animal1/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

bot.run('Token')
