import os
import discord
import random
from discord.ext import commands 
from discord.utils import get
from datetime import datetime


Msgs={}

class ReactionRoles(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
  

  @commands.command()
  @commands.has_role('Admins')
  async def BR(self, ctx):
    await ctx.message.delete()

    Embed=discord.Embed(title="BRANCH ROLES", description="Choose the branch you are in - \n **NOTE : ** Reaction counter will be set back to 1, do not worry, you will get the role. If you don't contact a mod or an admin.", colour=0xC27C0E)


    Embed.add_field(name="💻 - CSE", value="Computer Science Engineering(core and specializations)" , inline=False)

    Embed.add_field(name="📻 - ECE", value="Electronics and Communications Engineering(core and specializations", inline=False)

    Embed.add_field(name="💡 - EEE", value="Electrical and Electronics Engineering", inline=False)

    Embed.add_field(name="🎛 - EIE", value="Electronics and Instrumentation Engineering", inline=False)

    Embed.add_field(name="🖥 - IT", value="Information Technology", inline=False)

    Embed.add_field(name="🔧 - Mech", value="Mechanical Engineering(core and specializations)", inline=False)

    Embed.add_field(name="🧪 - Chemical", value="Chemical Engineering", inline=False)

    Embed.add_field(name="🧬 - Biotech", value="Biotechnology", inline=False)

    Embed.add_field(name="🏗 - Civil", value="Civil Engineering", inline=False)



    Embed.set_footer(text="VIT Vellore", icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")

    global msgBR
    msgBR = await ctx.send(embed=Embed)

    Msgs["BRmid"]=msgBR.id
    Msgs["BRcid"]=msgBR.channel.id

    global RolesR
    RolesR=["💻","📻","💡","🎛","🖥","🔧","🧪","🧬","🏗"]
    
    for r in RolesR:
      await msgBR.add_reaction(r)


  @commands.command()
  @commands.has_role('Admins')
  async def OR(self, ctx):
    await ctx.message.delete()
    Embed=discord.Embed(title="OTHER ROLES", description="Select the roles you want - \n", colour=0xC27C0E)

    Embed.set_footer(text="VIT Vellore", icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")


    Embed.add_field(name="🎮Gaming", value="For gamers to chat, talk, participate in tournaments and free games updates!" , inline=False)

    Embed.add_field(name="👨🏻‍💻Coding", value="For coding doubts and queries in competitive programming, open source, web devopment, embedded technologies etc or just about any coding doubt!" , inline=False)

    Embed.add_field(name="🎶Musicians", value="If you sing, play any instrument or make your own music!" , inline=False)

    Embed.add_field(name="🗣VC", value="If you want to be pinged for Voice chats" , inline=False)

    global msgOR 
    msgOR = await ctx.send(embed=Embed)
    
    
    

    global RolesOR 
    RolesOR=["🎮","👨🏻‍💻","🎶","🗣"]

    for r in RolesOR:
      await msgOR.add_reaction(r)

  






  @commands.Cog.listener()
  async def on_reaction_add(self,reaction,user):
    guild=reaction.message.guild
    if user != self.bot.user:
      if reaction.message==msgBR:
        await msgBR.remove_reaction(reaction, user)
        rolenames=["CSE","ECE","EEE","EIE","IT","Mech","Chemical","Biotech","Civil"]
        Roles=[]
        for rolename in rolenames:
          Role=get(guild.roles, name=rolename)
          Roles.append(Role)
        Rl=list(Roles)
        Roles=set(Roles)
        uroles=set(user.roles)
        Roles=list(Roles)
        Rdic=dict(zip(RolesR,Rl))
        if uroles.isdisjoint(Roles):
          await user.add_roles(Rdic[str(reaction.emoji)])
          await user.send(f"You joined **{Rdic[str(reaction.emoji)].name}**")
        
        else:
          er = list(uroles.intersection(Roles))[0]
          
          await user.remove_roles(er)
          await user.add_roles(Rdic[str(reaction.emoji)])
          await user.send(f"You joined **{Rdic[str(reaction.emoji)].name}**")
      
      elif reaction.message==msgOR:
        await msgOR.remove_reaction(reaction,user)
        rolenames=["gamers🎮","coder👨‍💻","musicians 🎶","VC 🗣"]
        Roles=[]
        for rolename in rolenames:
          Role=get(guild.roles, name=rolename)
          Roles.append(Role)
        Rl=list(Roles)
        Roles=set(Roles)
        uroles=set(user.roles)
        Roles=list(Roles)
        Rdic=dict(zip(RolesOR,Rl))
        if Rdic[str(reaction.emoji)] not in uroles:
          await user.add_roles(Rdic[str(reaction.emoji)])
          await user.send(f"You joined **{Rdic[str(reaction.emoji)].name}**")
        
        else:
          await user.remove_roles(Rdic[str(reaction.emoji)])

          await user.send(f"You left **{Rdic[str(reaction.emoji)].name}**")

      


  


def setup(bot):
  bot.add_cog(ReactionRoles(bot))
