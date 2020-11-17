import discord
from discord.ext import commands 
import asyncio
from datetime import datetime
import sys
import json
import os
   
   
os.chdir(r'/home/pi/Nellie/commands/data')
if os.path.isfile("serverlist.json"):
    with open('serverlist.json', encoding='utf8') as f:
        try:
	        slist = json.load(f)
        except ValueError:
            slist = {}
            slist['servers'] = []
else:
    slist = {}
    slist['servers'] = []
    with open('serverlist.json', 'w') as f:
        json.dump(slist, f, indent=4)	
			
client = commands.Bot(command_prefix='n!')

botcolor = 0xffffff

client.remove_command('help')

pass_list = ('474947907913515019')


def is_vale():
    def predicate(ctx):
        return ctx.message.author.id in ["474947907913515019", "408043714854780958", "486988989262462991"]

    return commands.check(predicate)
	
class servers:
    def __init__(self, client):
        self.client = client


    @client.command(pass_context = True)
    @is_vale()  
    async def gatherservers(self, ctx):	
        slist = {}
        slist['servers'] = []
        for server in self.client.servers:
            Bot = list(member.bot for member in server.members if member.bot is True) 
            user = list(member.bot for member in server.members if member.bot is False)
            member = list(member for member in server.members)
            disboard = list(member.bot for member in server.members if member.id =="302050872383242240")
            dbl = list(member.bot for member in server.members if member.id =="422087909634736160")
            discord.me = list(member.bot for member in server.members if member.id =="476259371912003597")
            for current_servers in slist['servers']:
                if current_servers['id'] == server.id:
                    pass
            if str(len(disboard))=="1":
                List1 = "Yes"
            else:
                List1 = "No"
            if str(len(dbl))=="1":
                List2 = "Yes"
            else:
                List2 = "No"
            if str(len(discord.me))=="1":
                List3 = "Yes"
            else:
                List3 = "No"
            if server.owner == None:
                slist['servers'].append({
                'name':server.name,
                'id':server.id,
                'Server Region':str(server.region), 
                'Usercount': str(len(member)),
                'Botcount': str(len(Bot)), 
                'Humancount': str(len(user)),
                'Serverowner': "None",
                'Sicherheitslevel': str(server.verification_level), 
                'Last Update': str(datetime.utcnow()),
                'Disboard': List1, 
                'DBL': List2,
                'Discord.me': List3
                })
            else:
                slist['servers'].append({
                'name':server.name,
                'id':server.id,
                'Server Region':str(server.region),
                'Usercount': str(len(member)),
                'Botcount': str(len(Bot)), 
                'Humancount': str(len(user)),
                'Serverowner': server.owner.name,
                'Sicherheitslevel': str(server.verification_level), 
                'Last Update': str(datetime.utcnow()),
                'Disboard': List1, 
                'DBL': List2,
                'Discord.me': List3
                })
        await asyncio.sleep(1)
        with open('serverlist.json', 'w+') as f:
            json.dump(slist, f, indent=4)
        msg = await self.client.say("Gather Servers sucessfully")
        await asyncio.sleep(60)
        await self.client.delete_message(msg)
 
    @client.event
    async def on_ready(self):
        slist = {}
        slist['servers'] = []
        for server in self.client.servers:
            Bot = list(member.bot for member in server.members if member.bot is True) 
            user = list(member.bot for member in server.members if member.bot is False)
            disboard = list(member.bot for member in server.members if member.id =="302050872383242240")
            dbl = list(member.bot for member in server.members if member.id =="422087909634736160")
            discord.me = list(member.bot for member in server.members if member.id =="476259371912003597")
            for current_servers in slist['servers']:
                if current_servers['id'] == server.id:
                    pass
            if str(len(disboard))=="1":
                List1 = "Yes"
            else:
                List1 = "No"
            if str(len(dbl))=="1":
                List2 = "Yes"
            else:
                List2 = "No"
            if str(len(discord.me))=="1":
                List3 = "Yes"
            else:
                List3 = "No"
            if server.owner == None:
                slist['servers'].append({
                'name':server.name,
                'id':server.id,
                'Server Region':str(server.region), 
                'Usercount': str(len(member)),
                'Botcount': str(len(Bot)), 
                'Humancount': str(len(user)),
                'Serverowner': "None",
                'Sicherheitslevel': str(server.verification_level), 
                'Last Update': str(datetime.utcnow()),
                'Disboard': List1, 
                'DBL': List2,
                'Discord.me': List3
                })
            else:
                slist['servers'].append({
                'name':server.name,
                'id':server.id,
                'Server Region':str(server.region),
                'Usercount': str(len(member)),
                'Botcount': str(len(Bot)), 
                'Humancount': str(len(user)),
                'Serverowner': server.owner.name,
                'Sicherheitslevel': str(server.verification_level), 
                'Last Update': str(datetime.utcnow()),
                'Disboard': List1, 
                'DBL': List2,
                'Discord.me': List3
                })
        await asyncio.sleep(1)
        with open('serverlist.json', 'w+') as f:
            json.dump(slist, f, indent=4) 

    @client.event
    async def on_server_remove(self, server):			
        slist = {}
        slist['botservers'] = []
        for botserver in self.client.servers:
            Bot = list(member.bot for member in botserver.members if member.bot is True) 
            user = list(member.bot for member in botserver.members if member.bot is False)
            member = list(member for member in botserver.members)
            disboard = list(member.bot for member in botserver.members if member.id =="302050872383242240")
            dbl = list(member.bot for member in botserver.members if member.id =="422087909634736160")
            discord.me = list(member.bot for member in botserver.members if member.id =="476259371912003597")
            for current_servers in slist['servers']:
                if current_servers['id'] == server.id:
                    pass
            if str(len(disboard))=="1":
                List1 = "Yes"
            else:
                List1 = "No"
            if str(len(dbl))=="1":
                List2 = "Yes"
            else:
                List2 = "No"
            if str(len(discord.me))=="1":
                List3 = "Yes"
            else:
                List3 = "No" pass
            if server.owner == None:
                slist['servers'].append({
                'name':server.name,
                'id':server.id,
                'Server Region':str(server.region), 
                'Usercount': str(len(member)),
                'Botcount': str(len(Bot)), 
                'Humancount': str(len(user)),
                'Serverowner': "None",
                'Sicherheitslevel': str(server.verification_level), 
                'Last Update': str(datetime.utcnow()),
                'Disboard': List1, 
                'DBL': List2,
                'Discord.me': List3
                })
            else:
                slist['servers'].append({
                'name':server.name,
                'id':server.id,
                'Server Region':str(server.region),
                'Usercount': str(len(member)),
                'Botcount': str(len(Bot)), 
                'Humancount': str(len(user)),
                'Serverowner': server.owner.name,
                'Sicherheitslevel': str(server.verification_level), 
                'Last Update': str(datetime.utcnow()),
                'Disboard': List1, 
                'DBL': List2,
                'Discord.me': List3
                })
        await asyncio.sleep(1)
        with open('serverlist.json', 'w+') as f:
            json.dump(slist, f, indent=4) 
			
    @client.event
    async def on_server_join(self, server):		
        slist = {}
        slist['botservers'] = []
        for botserver in self.client.servers:
            Bot = list(member.bot for member in botserver.members if member.bot is True) 
            user = list(member.bot for member in botserver.members if member.bot is False)
            member = list(member for member in botserver.members)
			disboard = list(member.bot for member in botserver.members if member.id =="302050872383242240")
            dbl = list(member.bot for member in botserver.members if member.id =="422087909634736160")
            discord.me = list(member.bot for member in botserver.members if member.id =="476259371912003597")
            for current_servers in slist['servers']:
                if current_servers['id'] == server.id:
                    pass
            if str(len(disboard))=="1":
                List1 = "Yes"
            else:
                List1 = "No"
            if str(len(dbl))=="1":
                List2 = "Yes"
            else:
                List2 = "No"
            if str(len(discord.me))=="1":
                List3 = "Yes"
            else:
                List3 = "No" pass
            if server.owner == None:
                slist['servers'].append({
                'name':server.name,
                'id':server.id,
                'Server Region':str(server.region), 
                'Usercount': str(len(member)),
                'Botcount': str(len(Bot)), 
                'Humancount': str(len(user)),
                'Serverowner': "None",
                'Sicherheitslevel': str(server.verification_level), 
                'Last Update': str(datetime.utcnow()),
                'Disboard': List1, 
                'DBL': List2,
                'Discord.me': List3
                })
            else:
                slist['servers'].append({
                'name':server.name,
                'id':server.id,
                'Server Region':str(server.region),
                'Usercount': str(len(member)),
                'Botcount': str(len(Bot)), 
                'Humancount': str(len(user)),
                'Serverowner': server.owner.name,
                'Sicherheitslevel': str(server.verification_level), 
                'Last Update': str(datetime.utcnow()),
                'Disboard': List1, 
                'DBL': List2,
                'Discord.me': List3
                })
        await asyncio.sleep(1)
        with open('serverlist.json', 'w+') as f:
            json.dump(slist, f, indent=4)  
		
		



def setup(client):
    client.add_cog(servers(client))