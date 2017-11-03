import asyncio
import discord
import os
import time
import traceback
from crontab import CronTab

client = discord.Client()

async def speak(interval, channel, text):
    await client.wait_until_ready()
    cron = CronTab(interval)
    while True:
        await asyncio.sleep(cron.next())
        try:
            await client.send_message(channel, text)
        except:
            print(f'I could not send `{text}` to `{channel}` :(')

@client.event
async def on_ready():
    for line in os.environ['DISCORD_CRON_CRONTAB'].split('\n'):
        try:
            interval, channel, text = line.split(',', 2)

            channel = client.get_channel(channel.strip())
            text = text.strip()

            print(f'Scheduling `{text}` with schedule `{interval.strip()}`')
            client.loop.create_task(speak(interval, channel, text))
        except:
            print('Could not schedule task.')
            traceback.format_exc()

try:
    client.run(os.environ['DISCORD_CRON_USER'], os.environ['DISCORD_CRON_PASS'])
except KeyError:
    client.run(os.environ['DISCORD_CRON_TOKEN'])

