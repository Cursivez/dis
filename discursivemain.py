import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import chalk
import datetime
import re
import pytz

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print ("Bot Online")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="DISCURSIVE Tournaments"))


#1v1 COMMANDS

@bot.command(pass_context=True)
async def vs(ctx):
    channel = ctx.message.author.voice.voice_channel
    voice = await bot.join_voice_channel(channel)
    player = voice.create_ffmpeg_player('game_starting.mp3')
    player.start()
    embed = discord.Embed(
        title = '**1v1 Starting**',
        description = 'To Start Another 1v1 Please Use `!stop` Before Using `!vs` again.',
        colour = discord.Colour.gold()
    )

    await bot.say(embed=embed)



@bot.command(pass_context=True)
async def stop(ctx):
    server = ctx.message.server
    voice_bot = bot.voice_client_in(server)
    await voice_bot.disconnect()


#SUPPORT COMMANDS

@bot.command(pass_context=True)
async def support(ctx):
    await bot.say("@STAFF , **your assistance is needed.**")

@bot.command(pass_context=True)
async def time(ctx):
    await bot.say("**The Server's Current Time** https://www.timeanddate.com/worldclock/singapore/singapore")

@bot.command(pass_context=True)
async def website(ctx):
    await bot.say("**Check out our website!** https://discursiveasia.wixsite.com/discursive")




bot.run("NTA0NTkzODU3NTM1ODAzMzky.DsLOGQ.OdVt5U5Bx0JUWupeTpKHpkdNcc4")