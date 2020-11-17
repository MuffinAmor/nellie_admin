import discord
from discord.ext import commands 
import asyncio
from datetime import datetime
import sys
import random

client = commands.Bot(command_prefix='nl!')

botcolor = 0x00ffff

pass_list = ['552926171537473536', '511531519530106880', '382290709249785857']

class kill:
    def __init__(self, client,):
        self.client = client
########################################################################################################################
    @client.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kill(self, ctx, member:discord.Member):	
        p = ctx.message.author
        if p.bot:
            pass
        if not p.bot: 
            if member.name == "Neko Public":
                msg = await self.client.say("{} kill all of the World with a Bomb of Hate.".format(p.mention))
                await asyncio.sleep(120)
                await self.client.delete_message(msg)
            if member is None:
                msg = await self.client.say("You need to choose a member, buddy!")
                await asyncio.sleep(120)
                await self.client.delete_message(msg)
            if member is p:	 	
                msg = await self.client.say("{} died".format(p.mention))
                await asyncio.sleep(120)
                await self.client.delete_message(msg)
            else:              
                choice = random.randint(1, 75)
                if choice == 1:
                    msg1 = await self.client.say("{0} was killed by a wrecking Ball".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 2:
                    msg1 = await self.client.say("{0} was killed by trying to dive between underwater mines, unfortunately {0} touched one....".format(member.name, member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 3:
                    msg1 = await self.client.say("{0} died because {1} stabbed him a toothbrush in his eye".format(member.name, p.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 4:
                    msg1 = await self.client.say("{0} killed {1}.".format(member.name, p.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 5:
                    msg1 = await self.client.say("{0} ate too much pizza and died.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 6:
                    msg1 = await self.client.say("{0} got killed by Illuminati.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 7:
                    msg1 = await self.client.say("{0} got killed by smoke to much weed".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 8:
                    msg1 = await self.client.say("{0} pressed delete. It deleted {1}.".format(p.name, member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 9:
                    msg1 = await self.client.say("{0} played a game from EA. He payed his live to EA...".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 10:
                    msg1 = await self.client.say("{0} click return. It returns back to the darkness.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 11:
                    msg1 = await self.client.say("{0} dies because he offended Neko".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 12:
                    msg1 = await self.client.say("{0} was murdered by {1} and everyone knows it, but there is no proof.".format(member.name, p.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 13:
                    msg1 = await self.client.say("{0} died from a creeper explosion".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 14:
                    msg1 = await self.client.say("{0} was squashed by a storm of sharks".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 15:
                    msg1 = await self.client.say("{0} decided it was a good idea to fight a tiger while smelling like meat. It did not end well.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 16:
                    msg1 = await self.client.say("{0} is now a meme in the EU".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 17:
                    msg1 = await self.client.say("{0} tried to outrun a train, the train won.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 18:
                    msg1 = await self.client.say("{0} tried to outrun a tank, the tank won.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 19:
                    msg1 = await self.client.say("{0} tried to catch a rocket, the rocket is now red.  ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 20:
                    msg1 = await self.client.say("{0} tried to fight against a shark while smelling like blood. The shark is now full ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 21:
                    msg1 = await self.client.say("{0} tried to fight against Neko. Neko banned him. ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 22:
                    msg1 = await self.client.say("{0} is still alive. But {1} died trying to kill him ".format(member.name, p.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 23:
                    msg1 = await self.client.say("{0} tried to rob a bank. He blowed himselfe up ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 24:
                    msg1 = await self.client.say("{0} failed at russian roulette but {1} died too ".format(member.name, p.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 25:
                    msg1 = await self.client.say("{0} watched so much hentais that his brain exploded.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 26:
                    msg1 = await self.client.say("{0} jumped from a skyscraper. ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 27:
                    msg1 = await self.client.say("{0} opened a window in the submarine while it was diving.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 28:
                    msg1 = await self.client.say("{0} watched so much anime that he starved to dead.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 29:
                    msg1 = await self.client.say("{0} tried to fight with a bear. Little Spoiler the bear won ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 30:
                    msg1 = await self.client.say("{0} was too long in the sauna and dried up ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 31:
                    msg1 = await self.client.say("{1} killed {0} with a fish. ".format(p.name, member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 32:
                    msg1 = await self.client.say("{0} tried to catch a bullet with his head. It wasnt a good Idea... ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 33:
                    msg1 = await self.client.say("{0} tried to brake the worldrekord in eating pizza. He bursted".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 34:
                    msg1 = await self.client.say("{1} hired me to kill {0}. But i wont do that.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 35:
                    msg1 = await self.client.say("{0} tried to code a programm wich allowed him to creat a second Neko Public. Neko killed him befor he finished".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 36:
                    msg1 = await self.client.say("{0} was killed by AaBbCcDdEeFfGgHhIiJj ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 37:
                    msg1 = await self.client.say("{0} was eaten by a giant fly.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 38:
                    msg1 = await self.client.say("{0} was killed by a elephant herd ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 39:
                    msg1 = await self.client.say("{0} met the sharknado. Guess what happened.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 40:
                    msg1 = await self.client.say("{0} was walled up alive. Idk if he is still alive".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 41:
                    msg1 = await self.client.say("{0} tried to understand Apis...his mind blowed up.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 42:
                    msg1 = await self.client.say("{0} has now the live target to wacht every video in the internet.I think tomorrow he is dead ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 43:
                    msg1 = await self.client.say("{0} tried to understand Stephen Hawkins doctoral thesis. His mind exploded.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 44:
                    msg1 = await self.client.say("{0} played grenade tennis with {1}. We have two deaths. ".format(member.name, p.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 45:
                    msg1 = await self.client.say("{0} was cleaning is gun, the gun was loaded and he hited the trigger.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 46:
                    msg1 = await self.client.say("{0} played with a crocodile. The crocodile is now full. ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 47:
                    msg1 = await self.client.say("{0} and {1} played together on the street. Both didnt saw the Bus. ".format(member.name, p.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 48:
                    msg1 = await self.client.say("{0} played CsGo in reallife. He got stabbed buy his teammate.  ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 49:
                    msg1 = await self.client.say("{0} was infected by an virus. A Worm lives in him but now he is dead.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 50:
                    msg1 = await self.client.say("{0} and {1} played baseball with a grenade.".format(member.name, p.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 51:
                    msg1 = await self.client.say("{0} and {1} played football on a minefield.".format(member.name, p.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 52:
                    msg1 = await self.client.say("AIDS. {0} died of AIDS".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 53:
                    msg1 = await self.client.say("{0} heard loud heavy metal and that burst his eardrums. He is dead now".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 54:
                    msg1 = await self.client.say("{0} died because he has stolen a cookie from Neko.".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 55:
                    msg1 = await self.client.say("{0} died because he has stolen Nekos last Pizza. Stolen pizza is not funny, he deserved it. ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 56:
                    msg1 = await self.client.say("{0} died because he insulted the Devs from Neko... ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 57:
                    msg1 = await self.client.say("{0} died because he hated Metal. And I like it so he had to die. ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 58:
                    msg1 = await self.client.say("{0} tried to hack Neko, but Neko killed him before...".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 59:
                    msg1 = await self.client.say("{0} died on a concert while he was crowedsurfing. Sad but True ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 60:
                    msg1 = await self.client.say("{0} and {1} played together Mario party, {2} stole a Star from {3}. So {4} killed him. ".format(p.name, member.name, p.name, member.name, p.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 61:
                    msg1 = await self.client.say("{0} stepped on a Lego stone at night. The Pain was too much".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 62:
                    msg1 = await self.client.say("{0} toke some drugs and thought he can flight...".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 63:
                    msg1 = await self.client.say("{0} tried to survive over 5 days in Water. He he dissolved in the water. ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 64:
                    msg1 = await self.client.say("{0} was thrown into an acid barrel by {1}".format(member.name, p.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice == 65:
                    msg1 = await self.client.say("{0} was thrown into an acid barrel by Neko".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice ==66:
                    msg1 = await self.client.say("{0} slipped on pedalos and broke his neck".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice ==67:
                    msg1 = await self.client.say("{0} was cleaning up is room but felt down the stairs".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice ==68:
                    msg1 = await self.client.say("{0} wanted to cook something but burned himself".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice ==69:
                    msg1 = await self.client.say("{0} died while watched Two Girls and... ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice ==70:
                    msg1 = await self.client.say("{0} died because he forgot to change the acid with the water ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice ==71:
                    msg1 = await self.client.say("{0} tried to outran Neko. He made it but just before the finish line he was killed by Neko ".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice ==72:
                    msg1 = await self.client.say("{0} died because he wanted to see every subreddit..that was too much for his hearth".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice ==73:
                    msg1 = await self.client.say("{0} died because he stole Nekos code...".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice ==74:
                    msg1 = await self.client.say("{0} got killed by AaBbCcDdEeFfGgHhIiJj".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
                if choice ==75:
                    msg1 = await self.client.say("{0} got killed by Niko".format(member.name))
                    await asyncio.sleep(120)
                    await self.client.delete_message(msg1)
 
					
def setup(client):
    client.add_cog(kill(client))