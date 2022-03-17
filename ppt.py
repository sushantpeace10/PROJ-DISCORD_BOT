import discord
from discord.ext import commands, tasks
from is_ppt_near import is_ppt_now
import asyncio

channel_id = 883965511422058516


class Ppt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.get_ppt.start(self.bot)

    @tasks.loop(hours=6)
    async def get_ppt(self, bot):
        if (is_ppt_now()):
            txt_msg = f"Boiis today is PPT!!!"
            msg = discord.Embed(
                title=f"Click Here to Regiter.",
                url="https://ppt.pes.edu",
                colour=0xd73422,
            )
            msg.set_author(name="PES UNIVERSITY",
                    icon_url="https://edushineglobal.com/edushine_api/public/col_logos/col-14270.png")
            msg.set_image(url="https://ppt.pes.edu/static/images/logos/PESUPPTLogo2-01.png")
            channel = bot.get_channel(channel_id)
            await channel.send(txt_msg, embed=msg)
            await asyncio.sleep(86400)
            await channel.purge(limit=1)
        else:
            pass


def setup(bot):
    bot.add_cog(Ppt(bot))