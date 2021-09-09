import os
import discord
import random
from discord.ext import commands 
from discord.utils import get
from datetime import datetime


class ReactionRoles(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
  

  @commands.command()
  @commands.has_role('Admins')
  async def BR(self, ctx):

    Embed=discord.Embed(title="BRANCH ROLES", description="Choose the branch you are in - \n **NOTE : ** Reaction counter will be set back to 1, do not worry, you will get the role. If you don't contact a mod or an admin", colour=0xC27C0E)


    Embed.add_field(name="CSE", value="💻 - Computer Science Engineering(core and specializations)" , inline=False)

    Embed.add_field(name="ECE", value="📻 - Electronics and Communications Engineering(core and specializations", inline=False)

    Embed.add_field(name="EEE", value="💡 - Electrical and Electronics Engineering", inline=False)

    Embed.add_field(name="EIE", value="🎛 - Electronics and Instrumentation Engineering", inline=False)

    Embed.add_field(name="IT", value="🖥 - Information Technology", inline=False)

    Embed.add_field(name="Mech", value="🔧 - Mechanical Engineering(core and specializations)", inline=False)

    Embed.add_field(name="Chemical", value="🧪 - Chemical Engineering", inline=False)

    Embed.add_field(name="Biotech", value="🧬 - Biotechnology", inline=False)

    Embed.add_field(name="Civil", value="🏗 - Civil Engineering", inline=False)



    Embed.set_footer(text="VIT Vellore", icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")


    global msg = await ctx.send(embed=Embed)


    Roles=["💻","📻","💡","🎛","🖥","🔧","🧪","🧬","🏗"]
    
    for r in Roles:
      await msg.add_reaction(r)

  @commands.Cog.listener()
  async def on_reaction_add(reaction,user):
    
    if Reaction.message==msg:
      print("hello")

    
        

      
      
      

    






    


    


    

    









  


def setup(bot):
  bot.add_cog(logs(bot))
