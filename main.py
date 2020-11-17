import asyncio

import discord
from discord.ext import commands

TOKEN = ''

client = commands.Bot(command_prefix="nl!")

botcolor = 0xffffff

client.remove_command('help')


########################################################################################################################
def is_vale():
    def predicate(ctx):
        return ctx.message.author.id in ["474947907913515019"]

    return commands.check(predicate)


extensions = ['commands.admin', 'commands.info', 'commands.member', 'commands.ping', 'commands.owner', 'commands.warn',
              'commands.sowner', 'commands.auto', 'commands.help', 'commands.login', 'commands.kill',
              'commands.pokefuchs', 'commands.wordblocker', 'commands.altacc', 'commands.servers', 'commands.tenor',
              'commands.help1', 'commands.nsfw']


@client.event
async def on_ready():
    print('Bot is ready.')
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    client.loop.create_task(status_task())


########################################################################################################################
async def status_task():
    while True:
        user = sum(len(s.members) for s in client.servers)
        servers = list(server for server in client.servers if not server.id == '264445053596991498')
        await client.change_presence(game=discord.Game(name='nl!help | Nellie'), status=discord.Status.online)
        await asyncio.sleep(30)
        await client.change_presence(game=discord.Game(name='Neko Codings', type=3),
                                     status=discord.Status.do_not_disturb)
        await asyncio.sleep(30)
        await client.change_presence(game=discord.Game(name='nl!help | Nellie'), status=discord.Status.online)
        await asyncio.sleep(30)
        await client.change_presence(game=discord.Game(name='to {0} server'.format(str(len(servers))), type=3),
                                     status=discord.Status.do_not_disturb)
        await asyncio.sleep(30)
        await client.change_presence(game=discord.Game(name='nl!help | Nellie'), status=discord.Status.online)
        await asyncio.sleep(30)
        await client.change_presence(game=discord.Game(name='some on her Phone', type=3),
                                     status=discord.Status.do_not_disturb)
        await asyncio.sleep(30)
    ########################################################################################################################


@client.command()
@is_vale()
async def load(extension):
    try:
        client.load_extension(extension)
        print('{} wurde geladen.'.format(extension))
        embed = discord.Embed(
            title='{} wurde geladen.'.format(extension),
            color=botcolor
        )
        msg = await client.say(embed=embed)
        await asyncio.sleep(5)
        await client.delete_message(msg)
    except Exception as error:
        print('{} konnte nicht geladen werden. [{}]'.format(extension, error))
        embed = discord.Embed(
            title='{} konnte nicht geladen werden. [{}]'.format(extension, error),
            color=botcolor
        )
        msg = await client.say(embed=embed)
        await asyncio.sleep(5)
        await client.delete_message(msg)


########################################################################################################################
@client.command()
@is_vale()
async def unload(extension):
    try:
        client.unload_extension(extension)
        print('{} wurde deaktiviert.'.format(extension))
        embed = discord.Embed(
            title='{} wurde deaktiviert.'.format(extension),
            color=botcolor
        )
        msg = await client.say(embed=embed)
        await asyncio.sleep(5)
        await client.delete_message(msg)
    except Exception as error:
        print('{} konnte nich deaktiviert werden. [{}]'.format(extension, error))
        embed = discord.Embed(
            title='{} konnte nicht deaktiviert werden. [{}]'.format(extension, error),
            color=botcolor
        )
        msg = await client.say(embed=embed)
        await asyncio.sleep(5)
        await client.delete_message(msg)


########################################################################################################################
@client.command()
@is_vale()
async def reload(extension):
    client.unload_extension(extension)
    try:
        client.load_extension(extension)
        embed = discord.Embed(title='{} wurde neu geladen.'.format(extension), color=botcolor)
        msg = await client.say(embed=embed)
        await asyncio.sleep(5)
        await client.delete_message(msg)
    except Exception as error:
        embed = discord.Embed(
            title='{} konnte nicht geladen werden. [{}]'.format(extension, error),
            color=botcolor
        )
        msg = await client.say(embed=embed)
        await asyncio.sleep(5)
        await client.delete_message(msg)


########################################################################################################################
if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} konnte nicht geladen werden. [{}]'.format(extension, error))

client.run(TOKEN)
