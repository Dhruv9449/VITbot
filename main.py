import os
import discord
from keep_alive import keep_alive
from discord.ext import commands 



intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!v ',intents=intents)



@bot.command()
@commands.has_role('Admins')
async def load(ctx, extention):
  bot.load_extension(f'cogs.{extention}')
  await ctx.send(f"Loaded {extention}")
  print(f"loaded {extention}")


@bot.command()
@commands.has_role('Admins')
async def unload(ctx, extention):
  bot.unload_extension(f'cogs.{extention}')
  await ctx.send(f"Unloaded {extention}")
  print(f"unloaded {extention}")

for file in os.listdir('./cogs'):
  if file.endswith('.py'):
    bot.load_extension(f'cogs.{file[:-3]}')
    print(f"loaded {file}")




@bot.event
async def on_message(message):
  controversial=["college", "open"]
  msg=message.content.lower()
  channel=message.channel

  if controversial[0] in msg and controversial[1] in msg:
    await channel.send("sus 👀")
  
  await bot.process_commands(message)







              

keep_alive() 


bot.run(os.environ['TOKEN'])

