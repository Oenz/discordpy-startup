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
    SlotList = list()
    
    for i in range(3):
        SlotStr = ":emoji_" + str(random.randrange(SlotRange)) + ':'
        SlotList.append(SlotStr)
    
    SlotResult = SlotList[0] + ' ' + SlotList[1] + ' ' + SlotList[2]
    
    await ctx.send(SlotResult)

bot.run(token)
