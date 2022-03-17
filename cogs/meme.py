import discord
import json
import lzma
import emoji
from discord.ext import commands
from instaloader_meme import get_explore, del_memes, reset_memes


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        meme_xz = get_explore()
        meme_notxz = lzma.open(f"instagram_meme/{meme_xz}")
        meme_json = json.load(meme_notxz)
        meme = discord.Embed(colour=0xE1306C, )
        meme.set_image(url=f"{meme_json['node']['display_url']}")
        meme.set_footer(
            text=
            f"\u2764\ufe0f {meme_json['node']['edge_liked_by']['count']} | {emoji.emojize(':speech_balloon:', variant = 'emoji_type')} {meme_json['node']['edge_media_to_comment']['count']}"
        )
        del_memes(meme_xz)
        await ctx.send(embed=meme)

    @commands.command()
    async def reset(self, ctx, what: str):
        if (what == 'meme'):
            reset_memes()
            msg = discord.Embed(
                title="Alert!",
                colour=0x2EFF2E,
                description=
                f"All saved memes are now deleted. use `.mc meme` to get fresh set of memes. {len(ctx.guilds)} "
            )
            await ctx.channel.send(embed=msg)
        else:
            msg = discord.Embed(
                title="Alert!",
                colour=0xFF0000,
                description=
                f" Reset `{what}`?\n आप जो लिख रहे हो वो कभी पढ़ते भी हो?")
            await ctx.channel.send(embed=msg)


def setup(bot):
    bot.add_cog(Meme(bot))
