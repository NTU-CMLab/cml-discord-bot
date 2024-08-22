from discord.ext import commands

@commands.command()
async def ping(ctx: commands.Context, msg: str):
    msg = f'{ctx.author} send message in {ctx.channel}: {ctx.command} {ctx.args}'
    print(msg)
    await ctx.send(msg)
