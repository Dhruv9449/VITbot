import os
import discord
import random
from discord.ext import commands 
from discord.utils import get
from datetime import datetime


class Embeds(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  
  @commands.command()
  async def rules(self,ctx):
    Embed=discord.Embed(title="RULES",url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngaaa.com%2Fdetail%2F284653&psig=AOvVaw12Xcf-elI6NU73gl1xEN9L&ust=1631335534723000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNCjqs7M8_ICFQAAAAAdAAAAABAI", description="""Please note that this is not an official server of the university. It is run by students.\nThese rules are set in place to keep our community clean and safe for all members. The Mods have the final choice. Rules are applied at the discretion of their overall overview.\n\nHave a great time and Welcome to the Family :orange_heart:""", colour=0xff1818)

    Embed.set_footer(text="VIT Vellore",icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")

    Embed.add_field(name="1. Be respectful to everyone",value="• No sort of bullying will be tolerated. Treat everyone as you would like to be treated.\n\n• No comment should include any traces of sexism, homophobia, racism, xenophobia or hate against any particular religious community (Or even caste). This will result in instant permeant ban.\n\n• Swearing is allowed in the server, we all are mature, draw a line between toxicity and fun. Let's respect the community and maintain a standard and decorum.")

    Embed.add_field(name="2. No NSFW or triggering content",value='• NSFW content is strictly prohibited.\n\n• Avoid sending triggering content, use spoiler tags and stop if someone is uncomfortable.')

    Embed.add_field(name="3. No drama",value="• Take it to dms")

    Embed.add_field(name="4. Keep content channel specific",value="• Avoid spamming channels")

    Embed.add_field(name="5. Don't abuse tags",value="• Avoid tagging user unnecessarily")

    Embed.add_field(name="6. Don't send malicious links and files",value="• This is a cybercrime, if found, will be reported")


    await ctx.send(embed=Embed)


    
  


def setup(bot):
  bot.add_cog(Embeds(bot))