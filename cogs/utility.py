import discord
from discord.ext import commands 
from discord.utils import get
from datetime import datetime


class Utility(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def ping(self,ctx):
    await ctx.send("pong")


  @commands.command()
  async def find(self,ctx,*, name):
    class Rolenotfound(Exception):
      pass
    class Emptyset(Exception):
      pass
    try:
      guild=ctx.guild
      roles=name.split(",")
      role=get(guild.roles, name=roles[0])
      if role not in guild.roles:
          raise Rolenotfound
      members=set(role.members)
      for role in roles[1:]:
        
        role = get(guild.roles, name=role.strip(" "))
        if role not in guild.roles:
          raise Rolenotfound
        lm=set(role.members)
        members=members.intersection(lm)


      l=[f"{role.name} : {role.mention}" for role in members]   
      if l==[]:
        raise Emptyset

      tnu=len(l)
      n=(tnu//46)+1
      d={}

      c=1
      while l!=[]:
        sl=l[:23]
        v="\n".join(sl)
        d[c]=discord.Embed(title='FIND USERS', description='This command is used to find users from different roles. ```!v find <role name>```**NOTE**: Role names are case sensitive.\n\n',color=0x6bb8e8)

        d[c].set_footer(text="VIT Vellore"+f" | page {c}/{n}",icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")

      
        d[c].add_field(name=name+f" - {tnu} users", value=v)
        del l[:45]
        c+=1
      c=1
      msg= await ctx.send(embed=d[c])

      await msg.add_reaction("◀️")
      await msg.add_reaction("▶️")
      

      def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
            # This makes sure nobody except the command sender can interact with the "menu"

      while True:
        try:
          reaction, user = await self.bot.wait_for("reaction_add", check=check)

          if str(reaction.emoji) == "▶️" and c!= n:
            c+=1
            await msg.edit(embed=d[c])

            await msg.remove_reaction(reaction, user)

          elif str(reaction.emoji) == "◀️" and c>1 :
            c-=1
            await msg.edit(embed=d[c])

            await msg.remove_reaction(reaction, user)
                
          else: 
            await msg.remove_reaction(reaction, user)

        except asyncio.TimeoutError:
          await message.delete()
          break

    except Rolenotfound:
      Embed=discord.Embed(title='INVALID ROLE', description='Please Enter a valid role! \n **NOTE**: Role names are case sensitive!',color=0xf00202)
      Embed.set_footer(text="VIT Vellore",icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")
      await ctx.send(embed=Embed)

    except Emptyset:
      Embed=discord.Embed(title='EMPTY LIST', description='There is no User with all these roles!',color=0xf00202)
      Embed.set_footer(text="VIT Vellore",icon_url="https://vit.ac.in/vit-rank/assets/img/VIT-logo.png")

      await ctx.send(embed=Embed)
  

  @commands.command(aliases=["member_count","member count"])
  async def membercount(self,ctx):
    await ctx.send(str(ctx.guild.member_count))



  

def setup(bot):
  bot.add_cog(Utility(bot))