import os
import discord
import string
from discord.utils import get
from discord.ext import commands
from discord import Permissions
import asyncio
from time import sleep
import requests
import sys
from colorama import Fore , Style
import base64
import json
import random
from discord_webhook import DiscordWebhook


os.system("title C:WINDOWNS\System32\cmd.exe")
os.system("cls")
os.system("color fc")


os.system("cls")
print(f"""{Fore.LIGHTBLACK_EX}``````¶0````1¶1_```````````````````````````````````````
```````¶¶¶0_`_¶¶¶0011100¶¶¶¶¶¶¶001_````````````````````
````````¶¶¶¶¶00¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶0_````````````````
`````1_``¶¶00¶0000000000000000000000¶¶¶¶0_`````````````
`````_¶¶_`0¶000000000000000000000000000¶¶¶¶¶1``````````
```````¶¶¶00¶00000000000000000000000000000¶¶¶_`````````
````````_¶¶00000000000000000000¶¶00000000000¶¶`````````
`````_0011¶¶¶¶¶000000000000¶¶00¶¶0¶¶00000000¶¶_````````
```````_¶¶¶¶¶¶¶00000000000¶¶¶¶0¶¶¶¶¶00000000¶¶1````````
``````````1¶¶¶¶¶000000¶¶0¶¶¶¶¶¶¶¶¶¶¶¶0000000¶¶¶````````
```````````¶¶¶0¶000¶00¶0¶¶`_____`__1¶0¶¶00¶00¶¶````````
```````````¶¶¶¶¶00¶00¶10¶0``_1111_`_¶¶0000¶0¶¶¶````````
``````````1¶¶¶¶¶00¶0¶¶_¶¶1`_¶_1_0_`1¶¶_0¶0¶¶0¶¶````````
````````1¶¶¶¶¶¶¶0¶¶0¶0_0¶``100111``_¶1_0¶0¶¶_1¶````````
```````1¶¶¶¶00¶¶¶¶¶¶¶010¶``1111111_0¶11¶¶¶¶¶_10````````
```````0¶¶¶¶__10¶¶¶¶¶100¶¶¶0111110¶¶¶1__¶¶¶¶`__````````
```````¶¶¶¶0`__0¶¶0¶¶_¶¶¶_11````_0¶¶0`_1¶¶¶¶```````````
```````¶¶¶00`__0¶¶_00`_0_``````````1_``¶0¶¶_```````````
``````1¶1``¶¶``1¶¶_11``````````````````¶`¶¶````````````
``````1_``¶0_¶1`0¶_`_``````````_``````1_`¶1````````````
``````````_`1¶00¶¶_````_````__`1`````__`_¶`````````````
````````````¶1`0¶¶_`````````_11_`````_``_``````````````
`````````¶¶¶¶000¶¶_1```````_____```_1``````````````````
`````````¶¶¶¶¶¶¶¶¶¶¶¶0_``````_````_1111__``````````````
`````````¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶01_`````_11____1111_```````````
`````````¶¶0¶0¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1101_______11¶_```````````
``````_¶¶¶0000000¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶0¶0¶¶¶1````````````
`````0¶¶0000000¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1`````````````
````0¶0000000¶¶0_````_011_10¶110¶01_1¶¶¶0````_100¶001_`
```1¶0000000¶0_``__`````````_`````````0¶_``_00¶¶010¶001
```¶¶00000¶¶1``_01``_11____``1_``_`````¶¶0100¶1```_00¶1
``1¶¶00000¶_``_¶_`_101_``_`__````__````_0000001100¶¶¶0`
``¶¶¶0000¶1_`_¶``__0_``````_1````_1_````1¶¶¶0¶¶¶¶¶¶0```
`_¶¶¶¶00¶0___01_10¶_``__````1`````11___`1¶¶¶01_````````
`1¶¶¶¶¶0¶0`__01¶¶¶0````1_```11``___1_1__11¶000`````````
`1¶¶¶¶¶¶¶1_1_01__`01```_1```_1__1_11___1_``00¶1````````
``¶¶¶¶¶¶¶0`__10__000````1____1____1___1_```10¶0_```````
``0¶¶¶¶¶¶¶1___0000000```11___1__`_0111_```000¶01```````
```¶¶¶00000¶¶¶¶¶¶¶¶¶01___1___00_1¶¶¶`_``1¶¶10¶¶0```````
```1010000¶000¶¶0100_11__1011000¶¶0¶1_10¶¶¶_0¶¶00``````
10¶000000000¶0________0¶000000¶¶0000¶¶¶¶000_0¶0¶00`````
¶¶¶¶¶¶0000¶¶¶¶_`___`_0¶¶¶¶¶¶¶00000000000000_0¶00¶01````
¶¶¶¶¶0¶¶¶¶¶¶¶¶¶_``_1¶¶¶00000000000000000000_0¶000¶01```
1__```1¶¶¶¶¶¶¶¶¶00¶¶¶¶00000000000000000000¶_0¶0000¶0_``
```````¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶00000000000000000000010¶00000¶¶_`
```````0¶¶¶¶¶¶¶¶¶¶¶¶¶¶00000000000000000000¶10¶¶0¶¶¶¶¶0`
````````¶¶¶¶¶¶¶¶¶¶0¶¶¶00000000000000000000010¶¶¶0011```
````````1¶¶¶¶¶¶¶¶¶¶0¶¶¶0000000000000000000¶100__1_`````
`````````¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶000000000000000000¶11``_1``````
`````````1¶¶¶¶¶¶¶¶¶¶¶0¶¶¶00000000000000000¶11___1_`````
``````````¶¶¶¶¶¶0¶0¶¶¶¶¶¶¶0000000000000000¶11__``1_````
``````````¶¶¶¶¶¶¶0¶¶¶0¶¶¶¶¶000000000000000¶1__````__```
``````````¶¶¶¶¶¶¶¶0¶¶¶¶¶¶¶¶¶0000000000000000__`````11``
`````````_¶¶¶¶¶¶¶¶¶000¶¶¶¶¶¶¶¶000000000000011_``_1¶¶¶0`
`````````_¶¶¶¶¶¶0¶¶000000¶¶¶¶¶¶¶000000000000100¶¶¶¶0_`_
`````````1¶¶¶¶¶0¶¶¶000000000¶¶¶¶¶¶000000000¶00¶¶01`````
`````````¶¶¶¶¶0¶0¶¶¶0000000000000¶0¶00000000011_``````_
````````1¶¶0¶¶¶0¶¶¶¶¶¶¶000000000000000000000¶11___11111
````````¶¶¶¶0¶¶¶¶¶00¶¶¶¶¶¶000000000000000000¶011111111_
```````_¶¶¶¶¶¶¶¶¶0000000¶0¶00000000000000000¶01_1111111
```````0¶¶¶¶¶¶¶¶¶000000000000000000000000000¶01___`````
```````¶¶¶¶¶¶0¶¶¶000000000000000000000000000¶01___1````
``````_¶¶¶¶¶¶¶¶¶00000000000000000000000000000011_111```
``````0¶¶0¶¶¶0¶¶0000000000000000000000000000¶01`1_11_``
``````¶¶¶¶¶¶0¶¶¶0000000000000000000000000000001`_0_11_`
``````¶¶¶¶¶¶¶¶¶00000000000000000000000000000¶01``_0_11`
``````¶¶¶¶0¶¶¶¶00000000000000000000000000000001```_1_11




▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒
▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒
▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒             ▒█▀▀▀█ ░█▀▀█ ▒█▀▀▀ ▀█▀ ▒█▀▀█ ░█▀▀█    ▒█▀▀▀█ ▒█▀▀▀ ▒█░░░ ▒█▀▀▀ ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ 
▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒             ░▀▀▀▄▄ ▒█▄▄█ ▒█▀▀▀ ▒█░ ▒█▄▄▀ ▒█▄▄█    ░▀▀▀▄▄ ▒█▀▀▀ ▒█░░░ ▒█▀▀▀ ▒█▀▀▄ ▒█░░▒█ ░▒█░░ 
▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒             ▒█▄▄▄█ ▒█░▒█ ▒█░░░ ▄█▄ ▒█░▒█ ▒█░▒█    ▒█▄▄▄█ ▒█▄▄▄ ▒█▄▄█ ▒█░░░ ▒█▄▄█ ▒█▄▄▄█ ░▒█░░
▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒
▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒
▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒
▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒
▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒
▒░░░░░░░░████████████████████████░░░░░░░░░░▒
▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒
▐██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒
▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒
▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒
▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒
▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒
▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████
▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████
▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████
▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████
████████████████████████████████████████████




Seja bemvindo(a) ao selfbot do saddy!
""")
os.system("color f")
r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
y = Fore.YELLOW
m = Fore.MAGENTA
w = Fore.LIGHTWHITE_EX
print(f"### {r}D{b}e{y}f{g}i{r}n{m}i{g}{b}r {w}###")
token = "NTA2MjA4ODQzODczOTEwNzg3.YEIpIA.cvhNb3Cpw2P1zZyIoXvR8kqZhKk"
prefix = '.'
cor = 0x00eeff


client = commands.Bot(command_prefix = prefix, self_bot=True)
client.remove_command('help')
versao = "1.0"
import requests





@client.event
async def on_ready():
    print(Fore.LIGHTBLUE_EX +f"Seja bemvindo(a) {client.user.name}{Fore.BLUE}#{client.user.discriminator}")
    os.system("cls")
    print(f"""{Fore.LIGHTCYAN_EX}
____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__________¶¶¶____¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
________¶¶¶__¶¶__¶¶_¶¶¶¶_¶¶¶¶___¶¶¶¶¶¶_¶¶¶¶¶
______¶¶¶__¶¶¶__¶¶__¶¶¶¶_¶¶¶¶___¶¶¶¶¶¶__¶¶¶¶¶¶
____¶¶¶___¶¶¶___¶¶_¶¶¶¶¶_¶¶¶¶____¶¶¶¶¶¶___¶¶¶¶¶
___¶¶___¶¶¶¶¶__¶¶__¶¶¶¶¶_¶¶¶¶____¶¶¶¶¶¶¶____¶¶¶¶¶
_¶¶____¶¶¶¶¶___¶¶__¶¶¶¶¶_¶¶¶¶_____¶¶¶¶¶¶_____¶¶¶¶¶¶
¶¶¶¶¶_____¶¶__¶¶__¶¶¶¶¶¶_¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                ▒█▀▀▀█ ░█▀▀█ ▒█▀▀▀ ▀█▀ ▒█▀▀█ ░█▀▀█    ▒█▀▀▀█ ▒█▀▀▀ ▒█░░░ ▒█▀▀▀ ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ 
__¶¶¶¶¶¶¶____¶¶¶__¶¶¶¶¶¶_¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                  ░▀▀▀▄▄ ▒█▄▄█ ▒█▀▀▀ ▒█░ ▒█▄▄▀ ▒█▄▄█    ░▀▀▀▄▄ ▒█▀▀▀ ▒█░░░ ▒█▀▀▀ ▒█▀▀▄ ▒█░░▒█ ░▒█░░ 
___¶¶¶___¶¶¶¶¶¶__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                   ▒█▄▄▄█ ▒█░▒█ ▒█░░░ ▄█▄ ▒█░▒█ ▒█░▒█    ▒█▄▄▄█ ▒█▄▄▄ ▒█▄▄█ ▒█░░░ ▒█▄▄█ ▒█▄▄▄█ ░▒█░░
_____¶¶__¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶
_______¶¶_¶¶¶_¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶
________¶¶__¶¶_¶¶__¶¶¶¶¶_¶¶¶______¶¶¶¶___¶¶¶
__________¶¶_¶¶_¶¶__¶¶¶¶_¶¶¶_____¶¶¶¶__¶¶¶
___________¶¶_¶¶_¶¶_¶¶¶¶__¶¶____¶¶¶¶__¶¶¶
_____________¶¶_¶_¶¶_¶¶¶__¶¶___¶¶¶¶_¶¶¶                 
_______________¶_¶_¶¶_¶¶__¶¶__¶¶¶¶_¶¶¶                {Fore.GREEN}█▀ ▄▀█ █▀▄ █▀▄ █▄█{Fore.LIGHTCYAN_EX}
________________¶¶__¶__¶__¶¶__¶¶¶¶¶¶                  {Fore.GREEN}▄█ █▀█ █▄▀ █▄▀ ░█░{Fore.LIGHTCYAN_EX}
__________________¶__¶____¶¶_¶¶¶¶¶¶                   Logado em : {client.user.name}#{client.user.discriminator}     
___________________¶¶_¶___¶¶¶¶¶¶¶                     Versão : {versao}
_____________________¶¶¶__¶¶¶¶¶¶¶                     Prefixo : {prefix}
______________________¶¶¶_¶¶¶¶                        Cor : {cornome}
________________________¶¶¶¶¶
__________________________¶
    """) 





link = "https://discord.gg/5cnxsxuG"
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v6/invite/" + str(link)
headers={
'Authorization': token
                }
requests.post(apilink, headers=headers)

os.system("cls")


@client.command()
async def raid(ctx):
    await ctx.message.delete()

    embed = discord.Embed(title="✩｡:•.─────  ❁ Saddy ❁  ─────.•:｡✩", color = cor)

    embed.add_field(name="Derrubar canais", value=f"`{prefix}nuke`", inline=False)

    embed.add_field(name="Criar canais", value=f"`{prefix}canais`", inline=False)

    embed.add_field(name="Mudar nomme do servidor", value=f"`{prefix}svnome`", inline=False)

    embed.add_field(name="Floodar", value=f"`{prefix}flood`", inline=False)
    
    embed.add_field(name="Criar varios cargos", value=f"`{prefix}criarcargos`", inline=False)

    embed.add_field(name="Deletar cargos", value=f"`{prefix}delcargos`", inline=False)

    embed.set_thumbnail(url="https://media.discordapp.net/attachments/816721719158243369/816724545107918878/a_fdee45f3dd142d1b9853038be3e16c16.gif?width=430&height=430")
    
    embed.set_footer(icon_url = 'https://cdn.discordapp.com/attachments/815033573207441428/816720535496818718/3.gif', text = f"Saddy on fire 💜 | https://youtube.com/saddy0001 ")
    
    await ctx.send(embed=embed)

@client.command()
async def delcargos(ctx):

    for z in ctx.guild.roles:
        print(Fore.GREEN + f"Cargo deletado : {z}")
        try:
            await z.delete()
        except Exception as e:
            print(Fore.RED + "Ocorreu um erro.")

@client.command()
async def criarrole(ctx, arg):
    guild = ctx.guild
    nome = ctx.message.content[len(prefix)+11:]
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 

    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())

    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())

    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())

    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 

    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())

    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.purple()) 
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.red())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.blue())
    await guild.create_role(name = nome, reason = 'saddy', color = discord.Colour.green())


@criarrole.error
async def criarrole_error(ctx, error):
    embed = discord.Embed(color=0xe74c3c)
    if isinstance(error, commands.CheckFailure):
        embed.set_author(
            name="Você não tem permissão para usar esse comando",
            icon_url='https://images-ext-2.discordapp.net/external/t8PErzxZqjlSh8TAykcMcwdlttwCs4Esrl-1pGA7OiY/%3Fwidth%3D300%26height%3D300/https/images-ext-2.discordapp.net/external/Hty31doO0MgNcegnlzbSAB2axLYkictP0mIyp1gTgns/https/images-ext-2.discordapp.net/external/S5rhb87hLGFBp657rzrXbWh_GvoR2K0dLs8NThOCiDU/%25253Fsize%25253D2048/https/cdn.discordapp.com/icons/779864878080458773/a_e26026b912d90683788e5144d881fc55.gif'
        ) 
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"<@{ctx.author.id}> Ops deu erro **ERRO** : `Você não especificou o nome dos cargos a serem criados. `")

@client.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="✩｡:•.─────  ❁ Saddy ❁  ─────.•:｡✩", color = cor)
    embed.set_image(url="https://cdn.discordapp.com/attachments/816720169765568562/816720200752955422/wallpaper.png")
    embed.add_field(name="Comandos de Raid", value=f"`{prefix}raid`", inline=False)
    embed.add_field(name="Comandos de Clear", value=f"`{prefix}helpclear`", inline=False)
    embed.add_field(name="Comandos de Pornô", value=f"`{prefix}nsfw`", inline=False)
    embed.add_field(name="Limpar cmd", value=f"`{prefix}limparcmd`", inline=False)
    embed.add_field(name="Comandos de Webhook", value=f"`{prefix}webhook`", inline=False)
    embed.add_field(name="Gerar wallpaper", value=f"`{prefix}wallpaper`", inline=False)
    embed.add_field(name="Créditos e status", value=f"`{prefix}status`", inline=False)
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/816720169765568562/816720200752955422/wallpaper.png?width=240&height=150')
    embed.set_footer(icon_url = 'https://cdn.discordapp.com/attachments/815033573207441428/816720535496818718/3.gif', text = f"Saddy on fire 💜 | https://youtube.com/saddy0001 ")
    await ctx.send(embed=embed)

@client.command()
async def helpclear(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="✩｡:•.─────  ❁ Saddy ❁  ─────.•:｡✩", color = cor)
    embed.add_field(name="Clear Lento (Limpa 30 mensagens)", value=f"`{prefix}clear`", inline=False)
    embed.add_field(name="Clear Rapido (Limpa 30 mensagens)", value=f"`{prefix}clear1`", inline=False)
    embed.add_field(name="Clear Lento (Limpa Tudo)", value=f"`{prefix}clearv2`", inline=False)
    embed.add_field(name="Clear Rapido (Limpa Tudo)", value=f"`{prefix}clearv3`", inline=False)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/816721719158243369/816724545107918878/a_fdee45f3dd142d1b9853038be3e16c16.gif?width=430&height=430")
    embed.set_footer(icon_url = 'https://cdn.discordapp.com/attachments/815033573207441428/816720535496818718/3.gif', text = f"Saddy on fire 💜 | https://youtube.com/saddy0001 ")
    await ctx.send(embed=embed)

@client.command()
async def nsfw(ctx):
    await ctx.message.delete()

    embed = discord.Embed(title="✩｡:•.─────  ❁ Saddy ❁  ─────.•:｡✩", color = cor)

    embed.add_field(name="Peito", value=f"`{prefix}peitos`", inline=False)

    embed.add_field(name="Buceta", value=f"`{prefix}buceta`", inline=False)

    embed.add_field(name="Hentai", value=f"`{prefix}hentai`", inline=False)

    embed.set_thumbnail(url="https://media.discordapp.net/attachments/816721719158243369/816724545107918878/a_fdee45f3dd142d1b9853038be3e16c16.gif?width=430&height=430")
    
    embed.set_footer(icon_url = 'https://cdn.discordapp.com/attachments/815033573207441428/816720535496818718/3.gif', text = f"Saddy on fire 💜 | https://youtube.com/saddy0001 ")
    
    await ctx.send(embed=embed)
@client.command()
async def webhook(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="✩｡:•.─────  ❁ Saddy ❁  ─────.•:｡✩", color = cor)
    embed.add_field(name="Deletar Webhook", value=f"`{prefix}deletewebhook`", inline=False)
    embed.add_field(name="Raidar webhook)", value=f"`{prefix}raidwebhook`", inline=False)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/816721719158243369/816724545107918878/a_fdee45f3dd142d1b9853038be3e16c16.gif?width=430&height=430")
    embed.set_footer(icon_url = 'https://cdn.discordapp.com/attachments/815033573207441428/816720535496818718/3.gif', text = f"Saddy on fire 💜 | https://youtube.com/saddy0001 ")
    await ctx.send(embed=embed)
@client.command()
async def nomecmd(ctx):
    os.system(f"title {ctx.message.content[len(prefix)+8:]}")
    await ctx.send(f"Titulo do cmd mudado para : {ctx.message.content[len(prefix)+8:]}")

@client.command(aliases=["Raidwebhook"])
async def raidwebhook(ctx, *, arg):
    from discord_webhook import DiscordWebhook
    headers = {'Content-Type': 'application/json', 'authorization': ctx.message.content[len(prefix)+12:]}
    url = ctx.message.content[len(prefix)+12:]
    re = requests.get(url, headers=headers)
    if re.status_code == 200:
	     await ctx.send("**Webhook valida! , Raidando webhook.**")
    else:
         await ctx.send("Webhook invalida")
    def raidarwebhook():
        webhook = DiscordWebhook(url=ctx.message.content[len(prefix)+12:], content="<a:zCaveiraCDF:809854311014203434> Webhook Raidada pelo selfbot Premium do saddy v6.5 Premium! @everyone!\né o saddy queimando sua webhook https://youtube.com/saddy0001" , avatar_url="https://cdn.discordapp.com/attachments/796043993263505430/809831061495873556/image0.jpg" , username = "saddy é o trem")
        response = webhook.execute()


    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    raidarwebhook()
    await ctx.send("Webhook raidada com suscesso!")

@client.command()
async def msgamigos(ctx): 
   for user in client.user.friends:
      try:
          await user.send(ctx.message.content[len(prefix)+10:])
          print(Fore.GREEN + f"Enviado para : {user.name}")
      except:
          print(Fore.RED + f"Não enviado: {user.name}")

@client.command()
async def wallpaper(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/wallpaper")
    res = r.json()
    embed1 = discord.Embed(title = "Wallpaper Gerado\nSelfbot do saddy v6.5 cosmos", color = cor)
    embed1.set_image(url=res['url'])
    embed1.set_thumbnail(url='https://cdn.discordapp.com/attachments/731888577872658462/809792660923088916/image0.gif')
    embed1.set_footer(icon_url = 'https://cdn.discordapp.com/attachments/731888577872658462/809792660923088916/image0.gif', text = f"Cosmos Selfbot by Saddy | https://youtube.com/saddy0001 Versão 6.5 PREMIUM! 🔥")
    await ctx.send(embed=embed1)


@client.command()
async def peito(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    embed1 = discord.Embed(title = "Peito", color = cor)
    embed1.set_image(url=res['url'])
    embed1.set_thumbnail(url='https://cdn.discordapp.com/attachments/731888577872658462/809792660923088916/image0.gif')
    embed1.set_footer(icon_url = 'https://cdn.discordapp.com/attachments/731888577872658462/809792660923088916/image0.gif', text = f"Cosmos Selfbot by Saddy | https://youtube.com/saddy0001 Versão 6.5 PREMIUM! 🔥")
    await ctx.send(embed=embed1)

@client.command()
async def buceta(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    embed1 = discord.Embed(title = "Buceta", color = cor)
    embed1.set_image(url=res['url'])
    embed1.set_thumbnail(url='https://cdn.discordapp.com/attachments/731888577872658462/809792660923088916/image0.gif')
    embed1.set_footer(icon_url = 'https://cdn.discordapp.com/attachments/731888577872658462/809792660923088916/image0.gif', text = f"Cosmos Selfbot by Saddy | https://youtube.com/saddy0001 Versão 6.5 PREMIUM! 🔥")
    await ctx.send(embed=embed1)

@client.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hentai")
    res = r.json()
    embed1 = discord.Embed(title = "Hentai", color = cor)
    embed1.set_image(url=res['url'])
    embed1.set_thumbnail(url='https://cdn.discordapp.com/attachments/731888577872658462/809792660923088916/image0.gif')
    embed1.set_footer(icon_url = 'https://cdn.discordapp.com/attachments/731888577872658462/809792660923088916/image0.gif', text = f"Cosmos Selfbot by Saddy | https://youtube.com/saddy0001 Versão 6.5 PREMIUM! 🔥")
    await ctx.send(embed=embed1)

@client.command()
async def arte(ctx, *, art: str):
    import aiohttp 
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://artii.herokuapp.com/make?text={art}") as r:
         arte = await r.text()
         await ctx.send('```\n' + arte + '```\n')

@client.command()
async def canais(ctx ,args):
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=ctx.message.content[len(prefix)+7:])
        except:
            return     

@client.command(pass_context=True)
async def deletewebhook(ctx):
        await ctx.send("Checkando webhook!")
        webhook = DiscordWebhook(url=ctx.message.content[len(prefix)+14:], content="<a:zCaveiraCDF:809854311014203434> Webhook Deletada pelo selfbot Premium do saddy v6.5 Premium! @everyone!\né o saddy queimando sua webhook https://youtube.com/saddy0001" , avatar_url="https://cdn.discordapp.com/attachments/796043993263505430/809831061495873556/image0.jpg" , username = "saddy é o trem")
        response = webhook.execute()
        requests.delete(ctx.message.content[len(prefix)+14:])
        await ctx.send("webhook Deletada com **sucesso**")


@deletewebhook.error
async def delete_error(ctx, error):
    embed = discord.Embed(color=0xe74c3c)
    if isinstance(error, commands.CheckFailure):
        embed.set_author(
            name="Você não tem permissão para usar esse comando",
            icon_url='https://images-ext-2.discordapp.net/external/t8PErzxZqjlSh8TAykcMcwdlttwCs4Esrl-1pGA7OiY/%3Fwidth%3D300%26height%3D300/https/images-ext-2.discordapp.net/external/Hty31doO0MgNcegnlzbSAB2axLYkictP0mIyp1gTgns/https/images-ext-2.discordapp.net/external/S5rhb87hLGFBp657rzrXbWh_GvoR2K0dLs8NThOCiDU/%25253Fsize%25253D2048/https/cdn.discordapp.com/icons/779864878080458773/a_e26026b912d90683788e5144d881fc55.gif'
        ) 
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"<@{ctx.author.id}> Ops deu erro **ERRO** : `Você não especificou qual a webhook checkar. `")

@canais.error
async def canais_error(ctx, error):
    embed = discord.Embed(color=0xe74c3c)
    if isinstance(error, commands.CheckFailure):
        embed.set_author(
            name="Você não tem permissão para usar esse comando",
            icon_url='https://images-ext-2.discordapp.net/external/t8PErzxZqjlSh8TAykcMcwdlttwCs4Esrl-1pGA7OiY/%3Fwidth%3D300%26height%3D300/https/images-ext-2.discordapp.net/external/Hty31doO0MgNcegnlzbSAB2axLYkictP0mIyp1gTgns/https/images-ext-2.discordapp.net/external/S5rhb87hLGFBp657rzrXbWh_GvoR2K0dLs8NThOCiDU/%25253Fsize%25253D2048/https/cdn.discordapp.com/icons/779864878080458773/a_e26026b912d90683788e5144d881fc55.gif'
        ) 
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"<@{ctx.author.id}> Ops deu erro **ERRO** : `Você não especificou o nome dos canais a serem criados. `")



@client.command()
async def nuke(ctx, arg):
    await ctx.message.delete()
    canaldetexto = ctx.message.content[len(prefix)+5:]
    for channel in ctx.guild.channels:
    	await channel.delete()
    	print(f'Canal deletado : {channel}')
    await ctx.guild.create_text_channel(name=canaldetexto)
    await ctx.guild.edit(name= canaldetexto + " By Safire Selfbot.")

@nuke.error
async def nuke_error(ctx, error):
    embed = discord.Embed(color=0xe74c3c)
    if isinstance(error, commands.CheckFailure):
        embed.set_author(
            name="Você não tem permissão para usar esse comando",
            icon_url='https://images-ext-2.discordapp.net/external/t8PErzxZqjlSh8TAykcMcwdlttwCs4Esrl-1pGA7OiY/%3Fwidth%3D300%26height%3D300/https/images-ext-2.discordapp.net/external/Hty31doO0MgNcegnlzbSAB2axLYkictP0mIyp1gTgns/https/images-ext-2.discordapp.net/external/S5rhb87hLGFBp657rzrXbWh_GvoR2K0dLs8NThOCiDU/%25253Fsize%25253D2048/https/cdn.discordapp.com/icons/779864878080458773/a_e26026b912d90683788e5144d881fc55.gif'
        ) 
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"<@{ctx.author.id}> Ops deu erro **ERRO** : `Você não especificou o nome dos canais a serem criados. `")


@client.command()
async def limparcmd(ctx):
    os.system("cls")
    print(f"""{Fore.LIGHTCYAN_EX}
____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__________¶¶¶____¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
________¶¶¶__¶¶__¶¶_¶¶¶¶_¶¶¶¶___¶¶¶¶¶¶_¶¶¶¶¶
______¶¶¶__¶¶¶__¶¶__¶¶¶¶_¶¶¶¶___¶¶¶¶¶¶__¶¶¶¶¶¶
____¶¶¶___¶¶¶___¶¶_¶¶¶¶¶_¶¶¶¶____¶¶¶¶¶¶___¶¶¶¶¶
___¶¶___¶¶¶¶¶__¶¶__¶¶¶¶¶_¶¶¶¶____¶¶¶¶¶¶¶____¶¶¶¶¶
_¶¶____¶¶¶¶¶___¶¶__¶¶¶¶¶_¶¶¶¶_____¶¶¶¶¶¶_____¶¶¶¶¶¶
¶¶¶¶¶_____¶¶__¶¶__¶¶¶¶¶¶_¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                ▒█▀▀▀█ ░█▀▀█ ▒█▀▀▀ ▀█▀ ▒█▀▀█ ░█▀▀█    ▒█▀▀▀█ ▒█▀▀▀ ▒█░░░ ▒█▀▀▀ ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ 
__¶¶¶¶¶¶¶____¶¶¶__¶¶¶¶¶¶_¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                  ░▀▀▀▄▄ ▒█▄▄█ ▒█▀▀▀ ▒█░ ▒█▄▄▀ ▒█▄▄█    ░▀▀▀▄▄ ▒█▀▀▀ ▒█░░░ ▒█▀▀▀ ▒█▀▀▄ ▒█░░▒█ ░▒█░░ 
___¶¶¶___¶¶¶¶¶¶__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                   ▒█▄▄▄█ ▒█░▒█ ▒█░░░ ▄█▄ ▒█░▒█ ▒█░▒█    ▒█▄▄▄█ ▒█▄▄▄ ▒█▄▄█ ▒█░░░ ▒█▄▄█ ▒█▄▄▄█ ░▒█░░
_____¶¶__¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶
_______¶¶_¶¶¶_¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶
________¶¶__¶¶_¶¶__¶¶¶¶¶_¶¶¶______¶¶¶¶___¶¶¶
__________¶¶_¶¶_¶¶__¶¶¶¶_¶¶¶_____¶¶¶¶__¶¶¶
___________¶¶_¶¶_¶¶_¶¶¶¶__¶¶____¶¶¶¶__¶¶¶
_____________¶¶_¶_¶¶_¶¶¶__¶¶___¶¶¶¶_¶¶¶                 
_______________¶_¶_¶¶_¶¶__¶¶__¶¶¶¶_¶¶¶                {Fore.GREEN}█▀ ▄▀█ █▀▄ █▀▄ █▄█{Fore.LIGHTCYAN_EX}
________________¶¶__¶__¶__¶¶__¶¶¶¶¶¶                  {Fore.GREEN}▄█ █▀█ █▄▀ █▄▀ ░█░{Fore.LIGHTCYAN_EX}
__________________¶__¶____¶¶_¶¶¶¶¶¶                   Logado em : {client.user.name}#{client.user.discriminator}     
___________________¶¶_¶___¶¶¶¶¶¶¶                     Versão : {versao}
_____________________¶¶¶__¶¶¶¶¶¶¶                     Prefixo : {prefix}
______________________¶¶¶_¶¶¶¶                        Cor : {cornome}
________________________¶¶¶¶¶
__________________________¶
    """) 
    await ctx.send("cmd limpo com suscesso!")

@client.command()
async def svnome(ctx , arg):
    await ctx.guild.edit(name=ctx.message.content[len(prefix)+6:])
    await ctx.send(f"Nome do servidor alterado para : **{ctx.message.content[len(prefix)+6:]}** ")

@client.command()
async def canal(ctx , arg):
    await ctx.guild.create_text_channel(name=ctx.message.content[len(prefix)+6:])
    await ctx.message.delete()
    await ctx.send(f"Canal criado : **{ctx.message.content[len(prefix)+6:]}**")

@svnome.error
async def mudarsv_error(ctx, error):
    embed = discord.Embed(color=0xe74c3c)
    if isinstance(error, commands.CheckFailure):
        embed.set_author(
            name="Você não tem permissão para usar esse comando",
            icon_url='https://images-ext-2.discordapp.net/external/t8PErzxZqjlSh8TAykcMcwdlttwCs4Esrl-1pGA7OiY/%3Fwidth%3D300%26height%3D300/https/images-ext-2.discordapp.net/external/Hty31doO0MgNcegnlzbSAB2axLYkictP0mIyp1gTgns/https/images-ext-2.discordapp.net/external/S5rhb87hLGFBp657rzrXbWh_GvoR2K0dLs8NThOCiDU/%25253Fsize%25253D2048/https/cdn.discordapp.com/icons/779864878080458773/a_e26026b912d90683788e5144d881fc55.gif'
        ) 

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"<@{ctx.author.id}> Ops deu erro **ERRO** : `Você não especificou qual o novo nome do servidor. `")

@client.command()
async def servidores(ctx):
    await ctx.send(f'Você está em **{len(client.guilds)}** Servidores!')
    async for guild in client.fetch_guilds(limit=150):
        await ctx.send(f"Nome do servidor **`{guild.name}`**")
        sleep(2)




@client.command()
async def flood(ctx ,arg):
    await ctx.send("Insira a quantidade de mensagens no console.")
    amount = int(input("Insira a quantidade de mensagens a serem floodadas:\n")) 
    value = 1
    while value <= amount:
        flood = ctx.message.content[len(prefix)+6:]
        await ctx.send(flood) 
        value += 1
    await ctx.send("Mensagens Floodadas.")



@flood.error
async def flood_error(ctx, error):
    embed = discord.Embed(color=0xe74c3c)
    if isinstance(error, commands.CheckFailure):
        embed.set_author(
            name="Você não tem permissão para usar esse comando",
            icon_url='https://images-ext-2.discordapp.net/external/t8PErzxZqjlSh8TAykcMcwdlttwCs4Esrl-1pGA7OiY/%3Fwidth%3D300%26height%3D300/https/images-ext-2.discordapp.net/external/Hty31doO0MgNcegnlzbSAB2axLYkictP0mIyp1gTgns/https/images-ext-2.discordapp.net/external/S5rhb87hLGFBp657rzrXbWh_GvoR2K0dLs8NThOCiDU/%25253Fsize%25253D2048/https/cdn.discordapp.com/icons/779864878080458773/a_e26026b912d90683788e5144d881fc55.gif'
        ) 

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"<@{ctx.author.id}> Ops deu erro **ERRO** : `Você não especificou oque floodar use {prefix}flood e sua mensagem. `")

@client.command()
async def clear(ctx, limit: int=None):
    async for message in ctx.message.channel.history(limit=30).filter(lambda m: m.author == client.user):
            try:
                await message.delete()
                print(f"Mensagem deletada : {message.content}")
                sleep(0.5)
            except:
                pass

@client.command()
async def clear1(ctx, limit: int=None):
    async for message in ctx.message.channel.history(limit=30).filter(lambda m: m.author == client.user):
            try:
                await message.delete()
                print(f"Mensagem deletada : {message.content}")
            except:
                pass
                

@client.command()
async def clearv2(ctx, limit: int=None):
    async for message in ctx.message.channel.history(limit=None).filter(lambda m: m.author == client.user):
            try:
                await message.delete()
                print(f"Mensagem deletada : {message.content}")
                sleep(1.5)
            except:
                pass

@client.command()
async def clearv3(ctx, limit: int=None):
    async for message in ctx.message.channel.history(limit=None).filter(lambda m: m.author == client.user):
            try:
                await message.delete()
                print(f"Mensagem deletada : {message.content}")
            except:
                pass
    




@canal.error
async def canal_error(ctx, error):
    embed = discord.Embed(color=0xe74c3c)
    if isinstance(error, commands.CheckFailure):
        embed.set_author(
            name="Você não tem permissão para usar esse comando",
            icon_url='https://images-ext-2.discordapp.net/external/t8PErzxZqjlSh8TAykcMcwdlttwCs4Esrl-1pGA7OiY/%3Fwidth%3D300%26height%3D300/https/images-ext-2.discordapp.net/external/Hty31doO0MgNcegnlzbSAB2axLYkictP0mIyp1gTgns/https/images-ext-2.discordapp.net/external/S5rhb87hLGFBp657rzrXbWh_GvoR2K0dLs8NThOCiDU/%25253Fsize%25253D2048/https/cdn.discordapp.com/icons/779864878080458773/a_e26026b912d90683788e5144d881fc55.gif'
        ) 
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"<@{ctx.author.id}> Ops deu erro **ERRO** : `Você não especificou o nome do canal a ser criado. `")



































try:
    client.run(token, bot=False)
except discord.LoginFailure:
    os.system("cls")
    print("Token invalido!")
except discord.HTTPException:
    os.system("cls")
    print("Ocorreu um erro desconhecido")
