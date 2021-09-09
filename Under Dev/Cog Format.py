import os
import discord
import random
from discord.ext import commands 
from discord.utils import get
from datetime import datetime


class COGname(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  pass


def setup(bot):
  bot.add_cog(logs(bot))

