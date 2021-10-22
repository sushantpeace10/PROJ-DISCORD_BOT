import discord
from discord.ext import commands, tasks
from menu import get_menu
import asyncio

channel_id = 876319066451742751


class Mess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.mess_time_table.start(self.bot)

    @tasks.loop(minutes=5)
    async def mess_time_table(self, bot):
        today_menu = get_menu()
        if (today_menu != -1):
            txt_msg = f"Menu : {today_menu['Menu']}"
            msg = discord.Embed(
                title=f"Week : {today_menu['Week']} | {today_menu['Day']}",
                colour=0xFFFF00,
            )
            msg.add_field(name=f"Time : {today_menu['Time']}",
                          value=f"Menu : {today_menu['Menu']}",
                          inline=False)
            channel = bot.get_channel(channel_id)
            await channel.send(txt_msg, embed=msg)
            await asyncio.sleep(6300)
            await channel.purge(limit=1)
        else:
            pass


def setup(bot):
    bot.add_cog(Mess(bot))
