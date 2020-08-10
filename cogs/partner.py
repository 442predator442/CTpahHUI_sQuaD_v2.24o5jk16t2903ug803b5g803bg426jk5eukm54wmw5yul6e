import discord
from discord.ext import commands
import os
import asyncio
import time
import datetime

class partner(commands.Cog):
	def __init__(self, bot):
		self.bot = bot



	@commands.command()
	async def partner(self, ctx, partner: discord.Member, amount: int, *, text):
		roles = ctx.author.roles
		role = ctx.guild.get_role(738500512080592896)
		if role in roles:
			
			guild = ctx.message.guild
			schannel = guild.get_channel(738499674784137298)
			nchannel = guild.get_channel(738499742350180474)
			bchannel = guild.get_channel(738499812625743912)
			prole = guild.get_role(738500276742389850)
			message = ctx.message.content.split()
			clock_dt = datetime.datetime.now()
			time = f'{clock_dt.hour}:{clock_dt.minute}'
			if amount < 100:
				if amount < 40:
					web = await schannel.create_webhook(name = partner.name)
					message = ctx.message.content.split()
					for elem in message:
						if elem.startswith("https://") or elem.startswith("http://"):
							embed = discord.Embed(title = 'Приесоденится на сервер (нажми)', url = f'{elem}', description = f'**Партнер:** {partner.mention}\n\n**Текст:**\n{text}')
							embed.set_footer(text = f'ПАРТНЕРКА | {time}')
							await web.send(embed = embed, avatar_url = partner.avatar_url)
					await web.delete()
					e = discord.Embed(title = '<:check:738641498127597599> Партнерка успешно совершена.', colour = discord.Colour.green())
					await ctx.send(embed = e)
					await partner.add_roles(prole)
					await partner.send(f'**Ваша партнерка отправлена на сервере `Странный SQUAD`**\n**Вашу партнерку вы можете найти сдесь: {schannel.mention}**')
				else:
					message = ctx.message.content.split()
					for elem in message:
						if elem.startswith("https://") or elem.startswith("http://"):
							embed = discord.Embed(title = 'Приесоденится на сервер (нажми)', url = f'{elem}', description = f'**Партнер:** {partner.mention}\n\n**Текст:**\n{text}')
							embed.set_footer(text = f'ПАРТНЕРКА | {time}')
							embed.set_author(name = f'{partner.name}#{partner.discriminator}', icon_url = partner.avatar_url)
							msg = await schannel.send(embed = embed)
							await msg.edit(content = f'**Пинг:** @here', embed = embed)
							e = discord.Embed(title = '<:check:738641498127597599> Партнерка успешно совершена.', colour = discord.Colour.green())
							await ctx.send(embed = e)
							await partner.add_roles(prole)
							await partner.send(f'**Ваша партнерка отправлена на сервере `Странный SQUAD`**\n**Вашу партнерку вы можете найти сдесь: {schannel.mention}**')
			elif amount ==100:
				message = ctx.message.content.split()
				for elem in message:
					if elem.startswith("https://") or elem.startswith("http://"):
						embed = discord.Embed(title = 'Приесоденится на сервер (нажми)', url = f'{elem}', description = f'**Партнер:** {partner.mention}\n\n**Текст:**\n{text}')
						embed.set_footer(text = f'ПАРТНЕРКА | {time}')
						embed.set_author(name = f'{partner.name}#{partner.discriminator}', icon_url = partner.avatar_url)
						msg = await schannel.send(embed = embed)
						await msg.edit(content = f'**Пинг:** @here', embed = embed)
						e = discord.Embed(title = '<:check:738641498127597599> Партнерка успешно совершена.', colour = discord.Colour.green())
						await ctx.send(embed = e)
						await partner.add_roles(prole)
						await partner.send(f'**Ваша партнерка отправлена на сервере `Странный SQUAD`**\n**Вашу партнерку вы можете найти сдесь: {schannel.mention}**')

			elif amount > 100:
				if amount < 700:
					message = ctx.message.content.split()
					for elem in message:
						if elem.startswith("https://") or elem.startswith("http://"):
							embed = discord.Embed(title = 'Приесоденится на сервер (нажми)', url = f'{elem}', description = f'**Партнер:** {partner.mention}\n\n**Текст:**\n{text}')
							embed.set_footer(text = f'ПАРТНЕРКА | {time}')
							embed.set_author(name = f'{partner.name}#{partner.discriminator}', icon_url = partner.avatar_url)
							msg = await nchannel.send(embed = embed)
							await msg.edit(content = f'@everyone @here', embed = embed)
							e = discord.Embed(title = '<:check:738641498127597599> Партнерка успешно совершена.', colour = discord.Colour.green())
							await ctx.send(embed = e)
							await partner.add_roles(prole)
							await partner.send(f'**Ваша партнерка отправлена на сервере `Странный SQUAD`**\n**Вашу партнерку вы можете найти сдесь: {nchannel.mention}**')
				elif amount > 700:
					message = ctx.message.content.split()
					for elem in message:
						if elem.startswith("https://") or elem.startswith("http://"):
							embed = discord.Embed(title = 'Приесоденится на сервер (нажми)', url = f'{elem}', description = f'**Партнер:** {partner.mention}\n\n**Текст:**\n{text}')
							embed.set_footer(text = f'ПАРТНЕРКА | {time}')
							embed.set_author(name = f'{partner.name}#{partner.discriminator}', icon_url = partner.avatar_url)
							msg = await bchannel.send(embed = embed)
							await msg.edit(content = f'@everyone @here', embed = embed)
							e = discord.Embed(title = '<:check:738641498127597599> Партнерка успешно совершена.', colour = discord.Colour.green())
							await ctx.send(embed = e)
							await partner.add_roles(prole)
							await partner.send(f'**Ваша партнерка отправлена на сервере `Странный SQUAD`**\n**Вашу партнерку вы можете найти сдесь: {bchannel.mention}**')
		else:
			embed = discord.Embed(title = '<:xmark:738641026209546251> Недостаточно прав использовать данную команду!', colour = discord.Colour.green())
			await ctx.send(embed = embed)


def setup(bot):
	bot.add_cog(partner(bot))
