import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Bot Online')
    print(client.user.name)
    print(client.user.id)
    game = discord.Game("!엘지 명령어")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!엘지 명령어":
        await message.channel.send("!나이")
        await message.channel.send("!혈액형")
        await message.channel.send("!사는곳")
        await message.channel.send("!방송계기")
        await message.channel.send("!트위치")
        await message.channel.send("!유튜브")
        await message.channel.send("!디코")
    if message.content == "!나이":
        await message.channel.send("09년생")
    if message.content == "!혈액형":
        await message.channel.send("O형")
    if message.content == "!사는곳":
        await message.channel.send("대한민국")
    if message.content == "!방송계기":
        await message.channel.send("다른 스트리머가 게임하면서 방송하는게 멋있어서")
    if message.content == "!트위치":
        await message.channel.send("https://www.twitch.tv/cozy06242021")
    if message.content == "!유튜브":
        await message.channel.send("https://www.youtube.com/channel/UCXPOGWwjH-noqWCn_URbWGA")
    if message.content == "!디코":
        await message.channel.send("게임방 디스코드 방 : https://discord.gg/SFw3xdT")
        await message.channel.send("트위치 디스코드 방 : https://discord.gg/tEEXa39")
        await message.channel.send("유튜브 디스코드 방 : https://discord.gg/wXTWKws")
    
client.run("ODAzNDU4MjgzMTY3NDE2MzMw.YA-E1g.hUMh0aSdVxtBoUNI8sUEwp8az0s")


















