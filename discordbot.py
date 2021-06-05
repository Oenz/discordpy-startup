from discord.ext import commands
import os
import traceback
import random
import pickle

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


SlotRange = ["<:emoji_6:836508451420504124>"
            ,"<:emoji_5:836507600458874942>"
            ,"<:emoji_4:836506871032315924>"
            ,"<:emoji_1:836151022946353162>"
            ,"<:emoji_12:836862989318619137>"
            ,"<:emoji_13:836863002166820896>"
            ,"<:emoji_14:836956978860392479>"
            ,"<:emoji_2:836503348601552896>"
            ,"<:emoji_3:836504640123043870>"
            ]

Hit = [
    "https://tenor.com/view/%E3%81%8A%E3%82%81%E3%81%A7%E3%81%A8%E3%81%86-%E5%AC%89%E3%81%97%E3%81%84-%E3%82%AF%E3%83%A9%E3%83%83%E3%82%AB%E3%83%BC-%E3%81%8A%E7%A5%9D%E3%81%84-%E5%8F%AF%E6%84%9B%E3%81%84-gif-15780951"
    ,"https://tenor.com/view/%E3%81%8A%E3%82%81%E3%81%A7%E3%81%A8%E3%81%86-%E5%AC%89%E3%81%97%E3%81%84-%E7%B4%99%E5%90%B9%E9%9B%AA-%E3%81%8A%E7%A5%9D%E3%81%84-%E5%8F%AF%E6%84%9B%E3%81%84-gif-15876321"
    ,"https://tenor.com/view/krol-gif-19996608"
    ,"https://tenor.com/view/running-shrek-running-late-gif-13251013"
    ]

BigHit = [ "https://media.discordapp.net/attachments/415026071189323780/702809774122860584/partyparrot.gif" ]

def reset(userid, userscore):
    savedata = [userid, userscore]
    with open('save.dat', mode='wb') as f:
        pickle.dump(savedata, f)
    
def get(userid):
    with open('save.dat', mode='rb') as f:
        pickle.load(f)
    return f
    

@bot.command()
async def slot(ctx):
    SlotList = list()
    SlotResult = ' '
    
    #random.randrange(SlotRange)
    for i in range(3):
        SlotStr = str(random.choice(SlotRange))
        SlotList.append(SlotStr)
        SlotResult += ' ' + str(SlotList[i])
    
    await ctx.send(SlotResult)
    
    if SlotList[0] == SlotList[1] == SlotList[2]:
        if SlotList[0] == SlotRange[3]: #JACKPOT
            await ctx.send("------------")
            await ctx.send("|JACKPOT|")
            await ctx.send("------------")
            await ctx.send(random.choice(BigHit))
        else: #WIN
            await ctx.send(random.choice(Hit))

DiceRange = ["O","CHI","U","CO","MA","N"] 
           
@bot.command()
async def dice(ctx):
    DiceList = list()
    DiceResult = ' '
    DiceScore = 0
    for i in range(5):
        DiceStr = str(random.choice(DiceRange))
        DiceList.append(DiceStr)
        DiceResult += ' ' + str(DiceList[i])
    await ctx.send(DiceResult)
    if DiceList.count("U") >= 1 and DiceList.count("N") >= 1 and DiceList.count("CHI") >= 1:
        await ctx.send("***UNCHI***")
        DiceScore += 1000
    if DiceList.count("U") >= 1 and DiceList.count("N") >= 1 and DiceList.count("CO") >= 1:
        await ctx.send("***UNCO***")
        DiceScore += 1000
    if DiceList.count("MA") >= 1 and DiceList.count("N") >= 1 and DiceList.count("CO") >= 1:
        await ctx.send("***MANCO***")
        DiceScore += 1000
    if DiceList.count("O") >= 1 and DiceList.count("U") >= 1 and DiceList.count("N") >= 1 and DiceList.count("CO") >= 1:
        await ctx.send("***OMANCO***")
        DiceScore += 5000
    if DiceList.count("CHI") >= 1 and DiceList.count("N") >= 1 and DiceList.count("CO") >= 1:
        await ctx.send("***CHINCO***")
        DiceScore += 1000
    if DiceList.count("CHI") >= 2 and DiceList.count("N") >= 2:
        await ctx.send("***CHINCHIN***")
        DiceScore += 3000
    if DiceList.count("O") >= 1 and DiceList.count("CHI") >= 2 and DiceList.count("N") >= 2:
        await ctx.send("**=========**")
        await ctx.send("***OCHINCHIN***")
        await ctx.send("**=========**")
        DiceScore += 10000
    DiceScoreResult = "Score : " + str(DiceScore)
    await ctx.send(DiceScoreResult)
    if DiceScore >= 10000: #JACKPOT
        await ctx.send(random.choice(BigHit))
    else if DiceScore >= 5000:
        await ctx.send(random.choice(Hit))
   
    
bot.run(token)
