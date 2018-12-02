from bs4 import BeautifulSoup
import requests
import discord
import time
import datetime
import re
from urllib.parse import urljoin

client = discord.Client()

#STARTUP MESSAGE WHEN READY
@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('Made by Sh00t with ❤')
    print('Twitter - https://twitter.com/learningszn')
    print('------')

#STASHBOT
@client.event
async def on_message(message):
    if message.content.startswith("/stash"):
        user_stash = message.content[1:len(message.content)]

        stash = requests.get('https://stashpedia.com/search?terms=' + user_stash).text

        soup = BeautifulSoup(stash, 'lxml')

        stash_main = soup.find('div', class_='col-lg-3 col-md-4 col-sm-6 col-xs-6 no-gutter-mobi formatItem')
        #print(main)

        stash_title = stash_main.find('img', class_='img-responsive gridImage')['alt']
        #print(title)

        stash_picture = stash_main.find('img', class_='img-responsive gridImage')['src']
        #print(picture)

        stash_popvalue = stash_main.find('span', class_='gridValue')
        #print(popvalue)

        stash_link = stash_main.find('a', class_='fill-height')['href']
        #print(link)

        embed = discord.Embed(title="Click here for more information!", url='https://stashpedia.com'+stash_link, color=0x067BE5)
        embed.add_field(name="Pop Name", value=stash_title, inline=True)
        embed.add_field(name="Average Price", value=stash_popvalue.text, inline=False)
        embed.set_image(url='https://stashpedia.com' + stash_picture)
        embed.set_footer(text="Made by Sh00t ❤", icon_url="https://cdn.discordapp.com/attachments/475456573976739852/476111984467640322/face-with-cowboy-hat_1f920_1.png")
        embed.timestamp = datetime.datetime.utcnow()
        
        await client.send_message(message.channel, embed=embed)

#RUN COMMAND W/ TOKEN
client.run("ENTER BOT TOKEN HERE")
