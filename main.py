from os import system
import os as test
mytitle = "Discord Cloner : By Zionek#0001 : Credits - NotSaksh"
test.system("title "+mytitle)
import psutil
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}
        ██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░  ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
        ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
        ██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║  ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
        ██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║  ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
        ██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝  ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
        ╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
{Style.RESET_ALL}
                                        {Fore.MAGENTA}By Zionek#0001 | Credits - NotSaksh{Style.RESET_ALL}
                                        {Fore.CYAN}OPTIONS: {Style.RESET_ALL}
                                        {Fore.CYAN}1.{Style.RESET_ALL} {Fore.GREEN}Clone Server | Insert into existing server{Style.RESET_ALL}
                                        {Fore.CYAN}2.{Style.RESET_ALL} {Fore.GREEN}Clone Server | Create new server - [NOT WORKING]{Style.RESET_ALL}
                                        
                                        
                                        """)
answer = input(f'                                        Please enter your choice:\n                                        > ')
if not test.path.exists('config.txt'):
    token = input(f'                                        Please enter your token:\n                                        > ')
    with open('config.txt', 'w') as fp:
        fp.write(f'{token}')
        pass
elif test.path.exists('config.txt'):
    with open('config.txt', 'r') as fp:
        token = fp.read()
if answer == "1":
    guild_s = input('                                        Please enter guild id you want to copy:\n                                        > ')
    guild = input('                                        Please enter guild id where you want to instert:\n                                        > ')
    input_guild_id = guild_s  # <-- input guild id
    output_guild_id = guild  # <-- output guild id


    print("  ")
    print("  ")

    @client.event
    async def on_ready():
        extrem_map = {}
        print(f"Logged In as : {client.user}")
        print("Cloning Server")
        guild_from = client.get_guild(int(input_guild_id))
        guild_to = client.get_guild(int(output_guild_id))
        await Clone.guild_edit(guild_to, guild_from)
        await asyncio.sleep(1)
        await Clone.roles_delete(guild_to)
        await asyncio.sleep(1)
        await Clone.channels_delete(guild_to)
        await asyncio.sleep(1)
        await Clone.roles_create(guild_to, guild_from)
        await asyncio.sleep(1)
        await Clone.categories_create(guild_to, guild_from)
        await asyncio.sleep(1)
        await Clone.channels_create(guild_to, guild_from)
        print(f"""{Fore.GREEN}


                                                ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                                ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                                ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
                                                ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
                                                ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
                                                ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░

        {Style.RESET_ALL}""")
        await asyncio.sleep(5)
        await client.close()
elif answer == "2":
    guild_s = input('                                        Please enter guild id you want to copy:\n                                        > ')
    input_guild_id = guild_s  # <-- input guild id


    print("  ")
    print("  ")

    @client.event
    async def on_ready():
        guild = await client.create_guild("My Server!")
        output_guild_id = guild.id
        extrem_map = {}
        print(f"Logged In as : {client.user}")
        print("Cloning Server")
        guild_from = client.get_guild(int(input_guild_id))
        guild_to = client.get_guild(int(output_guild_id))
        await Clone.guild_edit(guild_to, guild_from)
        await asyncio.sleep(1)
        await Clone.roles_delete(guild_to)
        await asyncio.sleep(1)
        await Clone.channels_delete(guild_to)
        await asyncio.sleep(1)
        await Clone.roles_create(guild_to, guild_from)
        await asyncio.sleep(1)
        await Clone.categories_create(guild_to, guild_from)
        await asyncio.sleep(1)
        await Clone.channels_create(guild_to, guild_from)
        print(f"""{Fore.GREEN}


                                                ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                                ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                                ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
                                                ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
                                                ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
                                                ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░

        {Style.RESET_ALL}""")
        await asyncio.sleep(5)
        await client.close()



client.run(token, bot=False)
