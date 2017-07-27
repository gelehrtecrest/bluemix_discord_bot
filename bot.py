import discord

client = discord.Client()

@client.event
async def on_ready():
    print("-"*20)
    print("ユーザー名：", client.user.name)
    print("ユーザーID：", client.user.id)
    print("-"*20)

@client.event
async def on_message(message):
    if not message.author.id == client.user.id:
        await client.send_message(message.channel, message.content)
        print("投稿しました")

    print("投稿者：", message.author)
    print("メッセージ：", message.content)

client.run('Your Key')
