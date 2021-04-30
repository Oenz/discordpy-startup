from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


SlotRange = 10;
    
@bot.command()
async def slot(ctx):
    Slot1 = ':emoji_' + random.randrange(SlotRange) + ':'
    await ctx.send(Slot1)

bot.run(token)
