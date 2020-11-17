import discord
from discord.ext import commands
import datetime
from datetime import datetime
import asyncio
import json
import urllib
import random
import requests
import aiohttp


client = commands.Bot(command_prefix='nl! ')

botcolor = 0x7CFC00

apikey = ""

lmt = 8

client.remove_command('help')

class tenor:
    def __init__(self, client):
        self.client = client

    @client.command(pass_context = True)
    @commands.cooldown(3, 30, commands.BucketType.user)
    async def tenor(self, ctx, *search):
        r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % apikey)

        if r.status_code == 200:
            anon_id = json.loads(r.content)["anon_id"]         #load the anon_id form cookies
        else:
            anon_id = ""

        search_term = search                                #search for ...

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s" % (search_term, apikey, lmt, anon_id))
    
        if r.status_code == 200:
            await self.client.send_typing(ctx.message.channel)
            top_8gifs = json.loads(r.content)
            post_to_pick = random.randint(1, len(top_8gifs["results"]))
            for i in range(1, post_to_pick):
                url = top_8gifs['results'][i]['media'][0]['gif']['url'] 
            try:
                embed = discord.Embed(color=ctx.message.author.color)
                embed.add_field(name="Tenor", value="[Not show? Click me]({0})".format(url), inline=False)
                embed.set_image(url=url)
                embed.set_footer(text='Tenor was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                await self.client.say(embed=embed)
            except ValueError:
                msg = await self.client.send_message(ctx.message.channel, "Please choose a other title. I found nothing")
            except Exception as error:
                await self.client.say(error)
        else:
            top_8gifs = None
#######################################################################################################################################
    @client.command(pass_context = True)
    @commands.cooldown(3, 30, commands.BucketType.user)
    async def hug(self, ctx, member:discord.Member=None):
        if member is None:
            msg = await self.client.say("Please tag a hugged Member")
            return
        r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % apikey)

        if r.status_code == 200:
            anon_id = json.loads(r.content)["anon_id"]         #load the anon_id form cookies
        else:
            anon_id = ""

        search_term = "hug"                                #search for ...

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s" % (search_term, apikey, lmt, anon_id))
    
        choice = random.randint(1, 1)
        if choice == 1:
            if r.status_code == 200:
                await self.client.send_typing(ctx.message.channel)
                trending_gifs = json.loads(r.content)
                post_to_pick = random.randint(1, len(trending_gifs["results"]))
                for i in range(1, post_to_pick):
                    url = trending_gifs['results'][i]['media'][0]['gif']['url'] 
                try:
                    embed = discord.Embed(color=ctx.message.author.color)
                    embed.add_field(name="{0} hugs {1}".format(ctx.message.author.name, member.name), value="[Not show? Click me]({0})".format(url), inline=False)
                    embed.set_image(url=url)
                    embed.set_footer(text='Hug was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                    embed.timestamp = datetime.utcnow()
                    await self.client.say(embed=embed)
                except Exception as error:
                    await self.client.say(error)
            else:
                trending_gifs = None
#######################################################################################################################################			
    @client.command(pass_context = True)
    @commands.cooldown(3, 30, commands.BucketType.user)
    async def pat(self, ctx, member:discord.Member):
        r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % apikey)

        if r.status_code == 200:
            anon_id = json.loads(r.content)["anon_id"]         #load the anon_id form cookies
        else:
            anon_id = ""

        search_term = "patting"                                #search for ...

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s" % (search_term, apikey, lmt, anon_id))
    

        if r.status_code == 200:
            await self.client.send_typing(ctx.message.channel)
            trending_gifs = json.loads(r.content)
            post_to_pick = random.randint(1, len(trending_gifs["results"]))
            for i in range(0, post_to_pick):
                url = trending_gifs['results'][i]['media'][0]['gif']['url'] 
            try:
                embed = discord.Embed(color=ctx.message.author.color)
                embed.add_field(name="{0} pats {1}".format(ctx.message.author.name, member.name), value="[Not show? Click me]({0})".format(url), inline=False)
                embed.set_image(url=url)
                embed.set_footer(text='Pat was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                await self.client.say(embed=embed)
            except Exception as error:
                await self.client.say(error)
        else:
            trending_gifs = None
#######################################################################################################################################			
    @client.command(pass_context=True)
    async def giphy(self, ctx, *, search):
        embed = discord.Embed(colour=discord.Colour.blue())
        session = aiohttp.ClientSession()

        if search == '':
            response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=5vmXcGaBWhf01e10n31n0LezLDehhLYf')
            data = json.loads(await response.text())            
            embed.set_image(url=data['data']['images']['original']['url'])
        else:
            search.replace(' ', '+')
            response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=5vmXcGaBWhf01e10n31n0LezLDehhLYf&limit=10')
            gif_choice = random.randint(0, 9)
            embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

        data = json.loads(await response.text())  
        await session.close()

        await self.client.send_message(embed=embed)
#######################################################################################################################################
    
########################################################################################################################
def setup(client):
    client.add_cog(tenor(client))
