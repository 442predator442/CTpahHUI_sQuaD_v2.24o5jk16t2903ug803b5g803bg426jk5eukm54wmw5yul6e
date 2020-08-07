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


@bot.event
async def on_member_join(member):
	guild = member.guild
	channel = guild.get_channel(738483468333219870)
	img = Image.open("fon.png")	

	responc = Image.open('image.png')
	responc = responc.convert('RGB')
	responc = responc.resize((420,420), Image.ANTIALIAS)

	url = str(member.avatar_url)
	responce = requests.get(url, stream = True)
	responce = Image.open(io.BytesIO(responce.content))
	responce = responce.convert('RGBA')
	responce = responce.resize((380,380), Image.ANTIALIAS)
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("19471.ttf", 80)
	font1 = ImageFont.truetype("12.ttf", 80)
	font2 = ImageFont.truetype("arial.ttf", 60)
	font3 = ImageFont.truetype("123.ttf", 50)
	font4 = ImageFont.truetype("1234.ttf", 40)
	img.paste(responc, (60, 60, 480, 480))
	img.paste(responce, (80, 80, 460, 460))
	draw.text((560, 70), 'Приветствуем!', font = font)
	draw.text((500, 200), 'У нас новенький(-ая),', font = font1)
	draw.text((500, 300), f'{member.name}#{member.discriminator}', font = font2)
	draw.text((100, 510), f'#{len(member.guild.members)}-ый участник', font = font3)
	draw.text((800, 570), f'{member.guild.name}', font = font4)
	img.save('fon1.png')
	await channel.send(file  = discord.File("fon1.png"))


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
async def help(ctx, module = None):
	await ctx.send('В розроботке...')


bot.run('NzM4NjI5MDc4MjEwMzE0MjUw.XyOr7w.7F2tyvUY7k_9bFBmnDWbj6BaPa4')
