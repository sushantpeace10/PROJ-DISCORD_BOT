import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive



load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']

bot = commands.Bot(command_prefix = '.mc ')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='commands starting with: .mc'))

@bot.command()
async def load(ctx, extension):
  bot.load_extension(f'cogs.{extension}')
  msg = discord.Embed(
      title = "Alert!",
      colour = 0x2EFF2E,
      description = f"Successfully loaded extension: {extension}",
      )
  await ctx.channel.send(embed = msg)

@bot.command()
async def unload(ctx,extension):
  bot.unload_extension(f'cogs.{extension}')
  msg = discord.Embed(
      title = "Alert!",
      colour = 0x2EFF2E,
      description = f"Successfully unloaded extension: {extension}",
      )
  await ctx.channel.send(embed = msg)

@bot.command()
async def reload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')
  bot.load_extension(f'cogs.{extension}')
  msg = discord.Embed(
    title = "Alert!",
    colour = 0x2EFF2E,
    description = f"Successfully reloaded extension: {extension}",
    )
  await ctx.channel.send(embed = msg)



for filename in os.listdir('cogs/'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

keep_alive()
bot.run(TOKEN)


