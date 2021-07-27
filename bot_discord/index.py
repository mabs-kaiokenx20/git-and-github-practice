import urllib
import discord 
from discord.ext import commands
from discord.ext.commands import bot
from urllib import request, parse
import re



bot = commands.Bot(command_prefix='!', description= 'Tell what do you need?')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_ready():
    print('I am ready motherfucker')

@bot.command()
async def info(ctx):
    await ctx.send(embed = discord.Embed(title=f'{ctx.guild.name}'))

# @bot.command()
# async def iwannasee(ctx, * , search):
#     user_search = parse.urlencode({'search_query': search})
#     html = request.urlopen('http://www.youtube.com/results?' + user_search)
#     result = re.findall("href=\*\\/watch\\?v=(.{11})", html.read().decode())
#     #await ctx.send('https://www.youtube.com/watch?v=' + result[0])
    # file_html = request.urlopen(url)
    # search_results = re.findall(r'', file_html.read().decode())
    # print(search_results) "/watch?v=lWgHvh1bKrA"


@bot.command()
async def iwannasee(ctx, * , user_search):
    url = 'https://www.youtube.com/results?search_query=' + parse.quote_plus(user_search)
    url2 = request.urlopen(url)
    print(url2.read().decode())

@bot.command()
async def name(ctx):
    await ctx.send('I am pepe bot')

bot.run('hero goes the token')
