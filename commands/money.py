import discord
from discord.ext import commands
import json
import os
import asyncio
os.chdir(r'/home/pi/Network/data')

client = commands.Bot(command_prefix='nl!')
botcolor = 0x00ff00

def is_vale():
    def predicate(ctx):
        return ctx.message.author.id in ["474947907913515019", "486988989262462991", "406479076048633857"]

    return commands.check(predicate)
	
blocklist = ['264445053596991498']

client.remove_command('help')
class money:
    def __init__(self, client):
        self.client = client

    @client.command(pass_context=True) 
    @commands.cooldown(3, 60, commands.BucketType.user)
    async def exp(self, ctx):	
        embed = discord.Embed(
        description="You have {} GlobalCredits💰!".format(get_xp(ctx.message.author.id)),
            color=ctx.message.author.color)
        await self.client.send_message(ctx.message.channel, embed=embed)
		

    @client.event
    async def on_message(self, message):
        if not message.author.bot:
            if not message.server.id in blocklist:
                server = message.server
                total = await self.client.get_user_info("533372604350988299")#Neko Public
                user_add_xp(message.author.id, 1)
########################################################################################################################
def setup(client):
    client.add_cog(money(client))

def user_add_xp(user_id: int, money: int,):
    if os.path.isfile("money.json"):
        try:
            with open('money.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['money'] += money
            with open('money.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('money.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['money'] = money
            with open('money.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['money'] = money
        with open('money.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)
########################################################################################################################
def get_xp(user_id: int):
    if os.path.isfile('money.json'):
        with open('money.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['money']
    else:
        return 0
########################################################################################################################
def user_remove_money(user_id: int, money: int):
    if os.path.isfile("money.json"):
        try:
            with open('money.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['money'] -= money
            with open('money.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('money.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['money'] = 0
            with open('money.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['money'] = 0
        with open('money.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)
########################################################################################################################			


