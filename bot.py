import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import datetime
import asyncio
import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import io
import os

bot = commands.Bot(command_prefix = ".")
bot.remove_command('help')

for file in os.listdir('./cogs'):
	if file.endswith('.py'):
		bot.load_extension(f'cogs.{file[:-3]}')

# python C:/python/cb/bot.py

@bot.event
async def on_ready():
	print('Странный Бот включился...')

@bot.event
async def on_message_edit(msg_b, msg_a):
	if msg_b.author.bot:
		return
	if msg_b.content == msg_a.content:
		return
	channel = msg_b.guild.get_channel(738484761055461478)
	web = await channel.create_webhook(name = bot.user.name)
	embed = discord.Embed(
		title = '📝Сообщение изменено',
		colour = discord.Colour.gold()
		)
	embed.add_field(
		name = 'Автор:',
		value = msg_b.author.mention,
		inline = False
		)
	embed.add_field(
		name = 'Канал:',
		value = msg_b.channel.mention,
		inline = False
		)
	embed.add_field(
		name = 'Сообщение до:',
		value = f'{msg_b.content}',
		inline = False
		)
	embed.add_field(
		name = 'Сообщение после:',
		value = f'{msg_a.content}',
		inline = False
		)
	await web.send(embed = embed, avatar_url = bot.user.avatar_url)
	await web.delete()
	return


@bot.event
async def on_command_error(ctx, error):
	pass


@bot.event
async def on_message_delete(message):
	if message.author.bot:
		return
	channel = message.guild.get_channel(738484761055461478)
	web = await channel.create_webhook(name = bot.user.name)
	embed = discord.Embed(
		title = '🚮Сообщение удалено',
		colour = discord.Colour.red()
		)
	embed.add_field(
		name = 'Автор:',
		value = message.author.mention,
		inline = False
		)
	embed.add_field(
		name = 'Канал:',
		value = message.channel.mention,
		inline = False
		)
	embed.add_field(
		name = 'Сообщение:',
		value = f'{message.content}',
		inline = False
		)
	await web.send(embed = embed, avatar_url = bot.user.avatar_url)
	await web.delete()
	return



@bot.command(aliases = ['cls', 'cl'])
@commands.has_role(738480581452496960)
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount: int):
	await ctx.message.delete()
	await ctx.channel.purge(limit = amount)
	emb = discord.Embed(
		description = f'<:check:738641498127597599> Было удалено {amount} сообщений',
		colour = discord.Colour.red()
		)
	await ctx.send(embed = emb, delete_after = 5.0)


@bot.command(aliases = ['icon', 'avatarka', 'ava'])
async def avatar(ctx, member: discord.Member = None):
	if member == None:
		user = ctx.author
	else:
		user = member
	emb = discord.Embed(
		title = f'Аватар `{user.name}#{user.discriminator}`:',
		colour = user.colour
		)
	emb.set_image(url = user.avatar_url)
	await ctx.send(embed = emb)
	
	
@bot.command()
async def rules(ctx):
	web = ctx.channel.create_webhook(name = 'Правила Странный SQUAD' )
	embed = discord.Embed(title = '[1] ПРАВИЛА ТЕКСТОВЫХ КАНАЛОВ', description = '[1.1] Запрещено оскорблять участников севера.\n[1.2] Запрещен капс (80% сообщения, содержащие большые буквы). \n[1.3] Запрещен спам и флуд (флуд: сообщение, содержащее 10+ подряд одинаковых букв/символов).\n[1.4] Запрещена Торговая Площадка (розрешено только в пределах игры за игровую валюту).\n[1.5] Запрещено отправлять NSFW картинки (картинки несущие 18+, шок контент и т.д.)\n[1.6] Запрещен офф-топ (Если для определенных сообщений/команд существует отдельный канал, это считается за офф-топ. Игнорируемые каналы: команды).\n[1.7] Запрещена реклама в ЛЮБОЙ его форме.\n[1.8] Запрещено попрошайничество.\n[1.9] Запрещено устраивать срач в любом чате.\n[1.10] Запрещено спорить/осуждать действия администрации.', colour = 000000)
	embed.set_footer(text = 'Правила Странный SQUAD', icon_url = 'https://cdn.discordapp.com/attachments/734420336954834994/741530902110142504/MOSHED-2020-7-2-0-18-50.jpg')
	emb = discord.Embed(title = '[2] ПРАВИЛА ГОЛОСОВОГО ЧАТА', description = '[2.1] Запрещено создавать сторонние шумы, которые мешают общению.\n[2.2] Запрещено оскорблять/обсуждать участников сервера.', colour = 000000)
	emb.set_footer(text = 'Правила Странный SQUAD', icon_url = 'https://cdn.discordapp.com/attachments/734420336954834994/741530902110142504/MOSHED-2020-7-2-0-18-50.jpg')
	em = discord.Embed(title = '[3] ПРОЧЕЕ', description = '[3.1] Приесоденяясь на сервер, вы автоматически соглашаетесь с правилами сервера.\n[3.2] Незнание правил не освобождает вас от ответственности.\n[3.3] Слив любого участника карается баном.\n[3.4] Ведите себя адекватно.', colour = 000000)
	em.set_footer(text = 'Правила Странный SQUAD', icon_url = 'https://cdn.discordapp.com/attachments/734420336954834994/741530902110142504/MOSHED-2020-7-2-0-18-50.jpg')

	e = discord.Embed(title = '[#] При нарушении правил вам будет выдан мут/кик/бан (зависит от нарушения).', colour = 000000)
	e.set_image(url = 'https://cdn.discordapp.com/attachments/734420336954834994/741539053115015228/MOSHED-2020-7-1-23-49-1-1.gif')
	e.set_footer(text = 'Правила Странный SQUAD | 08.08.2020', icon_url = 'https://cdn.discordapp.com/attachments/734420336954834994/741530902110142504/MOSHED-2020-7-2-0-18-50.jpg')
	await web.send(embed = embed, avatar_url = 'https://cdn.discordapp.com/attachments/734420336954834994/741530902110142504/MOSHED-2020-7-2-0-18-50.jpg')
	await web.send(embed = emb, avatar_url = 'https://cdn.discordapp.com/attachments/734420336954834994/741530902110142504/MOSHED-2020-7-2-0-18-50.jpg')
	await web.send(embed = em, avatar_url = 'https://cdn.discordapp.com/attachments/734420336954834994/741530902110142504/MOSHED-2020-7-2-0-18-50.jpg')
	await web.send(embed = e, avatar_url = 'https://cdn.discordapp.com/attachments/734420336954834994/741530902110142504/MOSHED-2020-7-2-0-18-50.jpg')
	await web.delete()


bot.run('NzM4NjI5MDc4MjEwMzE0MjUw.XyOr7w.7F2tyvUY7k_9bFBmnDWbj6BaPa4')
