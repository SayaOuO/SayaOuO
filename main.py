import keep_alive
import re
import pandas as pd
from pandas import DataFrame
import discord

client = discord.Client()


@client.event
async def on_ready():
    print('目前登入身份：', client.user)
    #print(time.localtime())


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('ID'):
        str = message.content
        tmp = re.split('：|\n|:', str)
        if len(tmp) == 4:
            count = int(tmp[3])
            data = pd.read_excel('KaiSen.xlsx', index_col='ID')
            data.loc[tmp[1], 'Count'] = count
            df = DataFrame(data)
            df.to_excel('KaiSen.xlsx')
        else:
            await message.channel.send('格式錯誤')
            return
    if message.content.startswith('總和'):
        data = pd.read_excel('KaiSen.xlsx')
        df = DataFrame(data)
        await message.channel.send(df['Count'].sum())
    if message.content.startswith('清單'):
        data = pd.read_excel('KaiSen.xlsx')
        await message.channel.send(data)
    if message.content.startswith('防守'):
        data = pd.read_excel('KaiSen.xlsx')
        df = DataFrame(data)
        a = (df['Count'].sum()) * 2
        if a - 25 >= 1560:
            await message.channel.send('單城20分守城成功')
        elif a - 25 >= 1260:
            await message.channel.send('單城25分守城成功')
        elif a - 25 >= 960:
            await message.channel.send('單城30分守城成功')
        if a - 50 >= 3000:
            await message.channel.send('雙城20分守城成功')
        elif a - 50 >= 2400:
            await message.channel.send('雙城25分守城成功')
        elif a - 50 >= 1800:
            await message.channel.send('雙城30分守城成功')
        else:
            await message.channel.send('雙城30分守城失敗，依幹部指示協調防守')

if __name__ == "__main__":
    keep_alive.keep_alive()
    client.run(
        'OTg2NTE3MzE3NzA4MDUwNDMy.GG2nXq.Ddx1h25VnU5x1k6PnmX2NIB2UBII5izG981u74'
    )
