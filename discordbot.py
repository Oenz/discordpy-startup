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


SlotRange = [ 1, 2, 3, 4, 5, 6, 12, 13, 14 ];
SlotWin = [
    "https://tenor.com/view/%E3%81%8A%E3%82%81%E3%81%A7%E3%81%A8%E3%81%86-%E5%AC%89%E3%81%97%E3%81%84-%E3%82%AF%E3%83%A9%E3%83%83%E3%82%AB%E3%83%BC-%E3%81%8A%E7%A5%9D%E3%81%84-%E5%8F%AF%E6%84%9B%E3%81%84-gif-15780951"
    ,"https://tenor.com/view/%E3%81%8A%E3%82%81%E3%81%A7%E3%81%A8%E3%81%86-%E5%AC%89%E3%81%97%E3%81%84-%E7%B4%99%E5%90%B9%E9%9B%AA-%E3%81%8A%E7%A5%9D%E3%81%84-%E5%8F%AF%E6%84%9B%E3%81%84-gif-15876321"
    ,"https://tenor.com/view/krol-gif-19996608"
    ]

@bot.command()
async def slot(ctx):
    SlotList = list()
    #random.randrange(SlotRange)
    for i in range(3):
        SlotStr = ":emoji_" + str(random.choice(SlotRange)) + ':'
        SlotList.append(SlotStr)
        await ctx.send(i)
        if i > 0:
            SlotResult += ' '
            
        SlotResult += SlotList[i]
    
    await ctx.send(SlotResult)
    
    if SlotList[0] == SlotList[1] == SlotList[2]:
        await ctx.send(random.choice(SlotWin))

bot.run(token)
