import discord
from discord.ext import commands
import datetime
from datetime import datetime
import asyncio
import praw
import random
import os
import json


bot = commands.Bot(command_prefix='nl!')

botcolor = 0x7CFC00

bot.remove_command('help')

reddit = praw.Reddit(client_id='CFfgp9jESrgbLA',
                     client_secret='HZhSLIsgRMlgP379vA_7YNHQdaU',
                     user_agent='windows:com:Neko Public:reddit.3.22.0(by /u/<MuffinAmor88919>)')

def is_vale():
    def predicate(ctx):
        return ctx.message.author.id in ["474947907913515019", "486988989262462991", "343109361595318276"]

    return commands.check(predicate)
	
class eigthteen:
    def __init__(self, bot):
        self.bot = bot
########################################################################################################################				
    @bot.command(pass_context=True)
    async def porn(self, ctx):
        if not ctx.message.author.bot:
            if ctx.channel.is_nsfw:
                await self.bot.send_typing(ctx.message.channel)
                memes_submissions = reddit.subreddit('porn').top()
                post_to_pick = random.randint(1, 100)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)
                embed = discord.Embed(color=ctx.message.author.color)
                embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                embed.set_image(url=submission.url)
                embed.set_footer(text='Thanks to Reddit')
                msg = await ctx.send(embed=embed)
                #await self.bot.add_reaction(msg, "❎")
       
    @bot.command(pass_context=True)
    async def lesbians(self, ctx):
        if not ctx.message.author.bot:
            if ctx.channel.is_nsfw:
                await self.bot.send_typing(ctx.message.channel)
                memes_submissions = reddit.subreddit('lesbains').top()
                post_to_pick = random.randint(1, 100)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)
                embed = discord.Embed(color=ctx.message.author.color)
                embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                embed.set_image(url=submission.url)
                embed.set_footer(text='Thanks to Reddit')
                msg = await ctx.send(embed=embed)
                #await self.bot.add_reaction(msg, "❎")

    @bot.command(pass_context=True)
    async def boobs(self, ctx): 
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('boobs').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")

    @bot.command(pass_context=True)
    async def ass(self, ctx):
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('ass').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")

    @bot.command(pass_context=True)
    async def rearpussy(self, ctx):
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('rearpussy').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")

    @bot.command(pass_context=True)
    async def rule34(self, ctx):
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('rule34').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")

    @bot.command(pass_context=True)
    async def booty(self, ctx):
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('booty').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")

    @bot.command(pass_context=True)
    async def hentai(self, ctx): 
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('hentai').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")
							
    @bot.command(pass_context=True)
    async def porngif(self, ctx):
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('porngif').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")

    @bot.command(pass_context=True)
    async def cumsluts(self, ctx):
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('cumsluts').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")

    @bot.command(pass_context=True)
    async def hentai_gif(self, ctx):
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('HENTAI_GIF').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")

    @bot.command(pass_context=True)
    async def pokeporn(self, ctx):
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('pokeporn').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")

    @bot.command(pass_context=True)
    async def tiny(self, ctx):
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('dirtysmall').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")

    @bot.command(pass_context=True)
    async def futanari(self, ctx):
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('futanari').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")

    @bot.command(pass_context=True)
    async def hentaibeast(self, ctx):
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('HentaiBeast').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")

    @bot.command(pass_context=True)
    async def ahegao(self, ctx):
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('ahegao').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")

    @bot.command(pass_context=True)
    async def gayporn(self, ctx):
        if not ctx.message.author.bot:
            for setting in nsfw['data']:
                if setting['id'] == ctx.message.server.id:
                    channel = ' '.join(setting['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.bot.send_typing(ctx.message.channel)
                        memes_submissions = reddit.subreddit('gayporn').top()
                        post_to_pick = random.randint(1, 100)
                        for i in range(0, post_to_pick):
                            submission = next(x for x in memes_submissions if not x.stickied)
                        embed = discord.Embed(color=ctx.message.author.color)
                        embed.add_field(name=submission.title, value="[Not show? Click me]({0})".format(submission.url), inline=False)
                        embed.set_image(url=submission.url)
                        embed.set_footer(text='Thanks to Reddit')
                        msg = await ctx.send(embed=embed)
                        #await self.bot.add_reaction(msg, "❎")



########################################################################################################################
def setup(bot):
    bot.add_cog(eigthteen(bot))