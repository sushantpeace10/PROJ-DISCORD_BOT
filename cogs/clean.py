import discord
import os
from discord.ext import commands

chanl_id = int(os.environ['cc_id'])


class Clean(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx):
        if (ctx.channel.id == chanl_id):
            await ctx.channel.purge()
        else:
            msg = discord.Embed(
                title="Alert!",
                colour=0xFF0000,
                description=
                f"{ctx.message.author.mention}, `.mc clear` command don't work in {ctx.message.channel.mention}, use `.mc clean <value>` instead.\n> Where <value> is number of messages to be deleted.",
            )
            await ctx.channel.send(embed=msg)

    @commands.command()
    async def clean(self, ctx, value: int):
        await ctx.channel.purge(limit=value + 1)
        msg = discord.Embed(
            title="Alert!",
            colour=0x2EFF2E,
            description=
            f"Last {value} message(s) were deleted by {ctx.message.author.mention}",
        )
        await ctx.channel.send(embed=msg)

    @clean.error
    async def clean_error(self, ctx: commands.Context,
                          error: commands.CommandError):
        if isinstance(error, commands.MissingRequiredArgument):
            msg = discord.Embed(
                title="Alert!",
                colour=0xFF0000,
                description=
                f"{ctx.message.author.mention}, `value` tera BAAP akke type karega!\n  Use `.mc clean <value>`.\n> Where <value> is number of messages to be deleted.",
            )
            await ctx.channel.send(embed=msg)


def setup(bot):
    bot.add_cog(Clean(bot))
