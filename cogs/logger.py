import os
import discord
import random
from discord.ext import commands 
from discord.utils import get
from datetime import datetime


class logs(commands.Cog):
  

  def __init__(self, bot):
    self.bot = bot
    self.logc=868136121874407424
    self.red=0xf00202
    self.blue=0x274870

    
  
  
  @commands.Cog.listener()
  async def on_ready(self):
    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='VITians'))
    print("We have logged in as {0.user}!!".format(self.bot))


  @commands.Cog.listener()
  async def on_member_join(self,member):
    wc=self.bot.get_channel(868131996315050074)

    Embed=discord.Embed(title='WELCOME!', description=f'Welcome to VIT freshers 2021, {member.mention}!! Hope you have a great time here! Please read <#868131743117479989> and grab a role from <#868139315442643005>',timestamp=datetime.now(),color=0x08EF2B)

    Embed.set_footer(text="VIT Vellore",icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")
    Embed.set_thumbnail(url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")

    f=open("welcome message.txt",'r')
    wm=f.read().format(member=member.mention)
    
    await member.send(wm)
    await wc.send(embed=Embed)

  

  @commands.Cog.listener()
  async def on_member_remove(self,member):
    lc=self.bot.get_channel(self.logc)
    print(member.roles)
    Embed=discord.Embed(description=f'{member.mention} {member.name+member.discriminator}', timestamp=datetime.now(),color=self.red)

    Embed.set_author(name="Member left", icon_url=str(member.avatar_url))

    Embed.add_field(name="Roles",value="".join([f"{role.mention}" for role in member.roles[1:]]))

    Embed.set_footer(text=f"ID:{member.id}",icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")

    await lc.send(embed=Embed)

    await member.send(f"Sorry to see you leave {member.mention}. If you change your mind, here's the invite : https://discord.gg/vygkyRfQBx")
  

  @commands.Cog.listener()
  async def on_message_delete(self,message):
    lc=self.bot.get_channel(self.logc)

    Embed = discord.Embed(description=f"**Message sent by {message.author.mention} deleted in {message.channel.mention}**\n"+f'{message.content}',colour=self.red, timestamp=datetime.now())

    Embed.set_author(name=message.author.name+message.author.discriminator,icon_url=str(message.author.avatar_url))


    Embed.set_footer(text=f"Author: {message.author.id} | Message ID: {message.id}",icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")

    await lc.send(embed=Embed)
  

  @commands.Cog.listener()
  async def on_bulk_message_delete(self, messages):
    lc=self.bot.get_channel(self.logc)

    Embed=discord.Embed(description=f"**Bulk Delete in {messages[0].channel.mention}, {len(messages)} messages deleted**\n", timestamp=datetime.now(), colour=self.blue)

    Embed.set_footer(icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")

    Embed.set_author(name=f"{messages[0].guild.name}", icon_url=str(messages[0].guild.icon_url))

    await lc.send(embed=Embed)
  

  @commands.Cog.listener()
  async def on_message_edit(self,m1,m2):
    lc=self.bot.get_channel(self.logc)
    Embed = discord.Embed(description=f"**Message edited in {m1.channel.mention}** [Jump to message]({m2.jump_url})",timestamp=datetime.now(),colour=self.blue)

    Embed.add_field(name="Before", value=m1.content, inline=False)
    Embed.add_field(name="After", value=m2.content, inline=False)

    Embed.set_author(name=f"{m1.author.name+m2.author.discriminator}", icon_url=str(m1.author.avatar_url))

    Embed.set_footer(text=f"User ID: {m1.author.id}",icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")

    await lc.send(embed=Embed)
  

  @commands.Cog.listener()
  async def on_guild_channel_create(self,channel):

    lc=self.bot.get_channel(self.logc)

    Embed = discord.Embed(description=f"**Channel Created: #{channel.name}**", timestamp=datetime.now(), colour=self.blue)

    Embed.set_author(name=f"{channel.guild.name}", icon_url=str(channel.guild.icon_url))
    Embed.set_footer(text=f"ID: {channel.id}",icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")


    await lc.send(embed=Embed)
  

  @commands.Cog.listener()
  async def on_guild_channel_delete(self,channel):
    lc=self.bot.get_channel(self.logc)

    Embed = discord.Embed(description=f"**Channel Deleted: #{channel.name}**", timestamp=datetime.now(), colour=self.red)

    Embed.set_author(name=f"{channel.guild.name}", icon_url=str(channel.guild.icon_url))
    Embed.set_footer(text=f"ID: {channel.id}",icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")


    await lc.send(embed=Embed)


  @commands.Cog.listener()
  async def on_guild_role_create(self,role):
    lc=self.bot.get_channel(self.logc)

    Embed = discord.Embed(description=f"**Role Created: {role.name}**", timestamp=datetime.now(), colour=self.blue)

    Embed.set_author(name=f"{role.guild.name}", icon_url=str(role.guild.icon_url))
    Embed.set_footer(text=f"ID: {role.id}",icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")


    await lc.send(embed=Embed)
  
  @commands.Cog.listener()
  async def on_guild_role_delete(self,role):
    lc=self.bot.get_channel(self.logc)

    Embed = discord.Embed(description=f"**Role Deleted: {role.name}**", timestamp=datetime.now(), colour=self.red)

    Embed.set_author(name=f"{role.guild.name}", icon_url=str(role.guild.icon_url))
    Embed.set_footer(text=f"ID: {role.id}",icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")


    await lc.send(embed=Embed)

    

  









    


    






def setup(bot):
  bot.add_cog(logs(bot))






