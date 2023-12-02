import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!help'):
        await message.channel.send('Помоги нам спасти планету! Команды: !org - Организации по спасению планеты, !helpplanet - способы помощи планете, !disasters - Катастрофы загрязнения')
    elif message.content.startswith('!org'):
        await message.channel.send('Организация Team Trees. Сбор средств для посадки деревьев. Пожертвовав 1$ будет посажено 1 дерево. Таким образом было посажено 20 миллионов деревьев')
    elif message.content.startswith('!helpplanet'):
        await message.channel.send('Советы для уменьшение загрязнений. 1) Выбрасывайте мусор в нужных местах или здавайте в специальные приемники. 2) На короткие расстояния пользуйтесь велосипедом вместо машин. 3) Жертвуйте средствами для благотварительних организаций по очищению планеты')
    elif message.content.startswith('!disasters'):
        await message.channel.send('Примеры природных катастроф: 1) Чернобыль - Гигантские выбросы Плутония-239, Америция-241, Цезия-137, Стронция-90. Чтобы Чернобыль стал вновь пригодным для жизни нужно около 24000 лет. А пока Чернобыль не пригоден для жизни.')
    else:
        await message.channel.send("Я не знаю что эта за команда")
client.run("токен")

