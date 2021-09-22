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
    await ctx.message.delete()
    Embed=discord.Embed(title="RULES",url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngaaa.com%2Fdetail%2F284653&psig=AOvVaw12Xcf-elI6NU73gl1xEN9L&ust=1631335534723000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNCjqs7M8_ICFQAAAAAdAAAAABAI", description="""Please note that this is not an official server of the university. It is run by students.\nThese rules are set in place to keep our community clean and safe for all members. The Mods have the final choice. Rules are applied at the discretion of their overall overview.\n\nHave a great time and Welcome to the Family :orange_heart:​​""", colour=0xff1818)

    Embed.set_footer(text="VIT Vellore",icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")

    Embed.add_field(name="1. Be respectful to everyone",value="• No sort of bullying will be tolerated. Treat everyone as you would like to be treated.\n\n• No comment should include any traces of sexism, homophobia, racism, xenophobia or hate against any particular religious community (Or even caste). This will result in instant permeant ban.\n\n• Swearing is allowed in the server, we all are mature, draw a line between toxicity and fun. Let's respect the community and maintain a standard and decorum.​",inline=False)

    Embed.add_field(name="2. No NSFW or triggering content",value='• NSFW content is strictly prohibited.\n\n• Avoid sending triggering content, use spoiler tags and stop if someone is uncomfortable.​',inline=False)

    Embed.add_field(name="3. No drama",value="• Take it to dms​",inline=False)

    Embed.add_field(name="4. Keep content channel specific",value="• Avoid spamming channels​",inline=False)

    Embed.add_field(name="5. Don't abuse tags",value="• Avoid tagging user unnecessarily​",inline=False)

    Embed.add_field(name="6. Don't send malicious links and files",value="• This is a cybercrime, if found, will be reported​",inline=False)


    await ctx.send(embed=Embed)


  @commands.command()
  async def invite(self,ctx):
    await ctx.message.delete()

    Embed = discord.Embed(title="Invite link",url="https://discord.gg/Zxd7MQ6Rfd",colour=0x2F3136)

    Embed.set_image(url=str(ctx.guild.icon_url))

    Embed.add_field(name="Permenant invite link", value="https://discord.gg/Zxd7MQ6Rfd​")

    Embed.set_footer(text="VIT Vellore", icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")

    await ctx.send(embed=Embed)


  @commands.command()
  async def curriculum(self,ctx):

    Embed1 = discord.Embed(title="Curriculum and Syllabi", description="Computer Science Engineering",url="https://vit.ac.in/schools/school-of-computer-science-and-engineering-for-ug-courses",colour=0x2F3136)

    Embed1.add_field(name="CSE", value="https://vit.ac.in/sites/default/files/scope/B.Tech_CSE_2020_2021.pdf", inline=False)

    Embed1.add_field(name="CSE spec in Bioinformatics", value="https://vit.ac.in/sites/default/files/scope/B.Tech(CSE)_BioInformatics_2020_2021.pdf", inline=False)

    Embed1.add_field(name="CSE spec in Information Security", value="https://vit.ac.in/sites/default/files/scope/B.Tech_CSE_IS_2020_2021.pdf", inline=False)

    Embed1.add_field(name="CSE spec in Business Systems(TCS)", value="https://vit.ac.in/sites/default/files/scope/B.Tech_CSE_BS_2020_2021.pdf", inline=False)

    Embed1.add_field(name="CSE spec in IOT", value="https://vit.ac.in/sites/default/files/scope/B.Tech(CSE)_IoT_2020_2021.pdf", inline=False)

    Embed1.add_field(name="CSE spec in Data Science", value="https://vit.ac.in/sites/default/files/scope/B.Tech(CSE)_DS_2020_2021.pdf", inline=False)

    Embed1.add_field(name="CSE spec in Block Chain", value="https://vit.ac.in/sites/default/files/scope/B.Tech-CSE-BlockChainTechnology.pdf", inline=False)

    Embed1.add_field(name="IT", value="https://vit.ac.in/sites/default/files/site/B.Tech_IT_Curriculum_Syllabi_2019-2020.pdf", inline=False)

    Embed1.set_footer(text="VIT Vellore", icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")

  
  """@commands.command(aliases=["ru"])
  @commands.has_any_role('Admins','Mods')
  async def resource_upload(self, ctx,*,msg):

    await ctx.message.delete()
    if ctx.message.attachments!=[]:
      at = ctx.message.attachments[0]
      f = await at.to_file()
    else:
      f=None
    await ctx.send(content = msg, file=f)"""

  @commands.command(aliases=["ru"])
  @commands.has_any_role('Admins','Mods')
  async def resource_upload(self, ctx,*,msg):
    await ctx.message.delete()
    at= ctx.message.attachments[0]
    URL = at.url
    size = str(at.size/(1024*1024))[:4]+"MB"
    ty = at.type

    embed =  discord.Embed(title=msg, timestamp=datetime.now(), color=0x2F3136, url = URL)


    embed.add_field(name= "Size", value=size )

    embed.set_footer(text="VIT Vellore", icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")

    await ctx.send(embed=embed)
    

  




    


    


    

  


def setup(bot):
  bot.add_cog(Embeds(bot))