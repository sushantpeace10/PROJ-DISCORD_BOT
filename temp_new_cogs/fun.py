import discord
from discord.ext import commands




class Fun(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def hm(self, ctx, comd : str):
      if(comd == "start"):
        file = discord.File("hangman/begin.png")
        msg = discord.Embed(
        title = "Alert!",
        colour = 0x2EFF2E,
        description = "Welcome to Hangman\n\n> How to Play:\n 1. Objective is to find the movie name by guessing letter by letter.`Simply type the letter in your message`\n 2. If the letter is in Movie's name, I will fill that for you.\n 3. If guessed wrong, you will loss life. ",
        )
        msg.set_image(url="attachment://begin.png")
        msg.set_footer(text = "`Game start in will few seconds.`")
        await ctx.send(file = file, embed = msg)



def setup(bot):
  bot.add_cog(Fun(bot))
    