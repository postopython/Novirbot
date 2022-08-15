from discord.ext import commands
import random


client = commands.Bot( command_prefix = '#') #you can choose other prefix
language = ''  #Choose language. Now avaible 'ru' - russian and 'eng' - english

#бросок кубика/dice roll
@client.command(Pass_context = True)
async def roll(ctx): #command: #roll d20.
    result = []
    raw_result = []
    plus = 0
    minus = 0
    count = 1
    message = ctx.message
    lis = list(message.content)
    lis = lis[5:]
    lis = [au for au in lis if au != ' ']
    ind = lis.index('d')
    if ind > 0:
        if count == '+':
            plus = 1
        else:
            count = lis[:ind]
            count = ''.join(count)
            count = int(count)
    li = lis[ind:]
    li = li[1:]
    number = ''
    for i, v in enumerate(li):
        if v == '+':
            plus = li[i:]
            plus = ''.join(plus)
            plus = int(plus)
            break
        elif v == '-':
            minus = li[i:]
            minus = ''.join(plus)
            minus = int(plus)
            break
        else:
            number += v
    number = ''.join(number)
    number = int(number)
    ans = []
    ans.append(count)
    ans.append(number)
    ans.append(plus)
    ans.append(minus)
    for i in range(ans[0]):
        raw = random.randint(1, ans[1])
        raw_result.append(raw)
        res = raw + ans[2]
        res = raw - ans[3]
        result.append(res)
    if language == 'ry':
        await ctx.send(f'С куба: {raw_result} Итого: {result}')
    else:
        await ctx.send(f'Cube: {raw_result} Result: {result}')



client.run() #paste token there