import asyncio
import discord
import os
import time
import traceback

client = discord.Client()

async def speak(interval, channel, text):
    await client.wait_until_ready()
    while True:
        print(f'Typing `{text}` to `{channel}`')
        time_start = time.time()

        try:
            await client.send_message(channel, text)
        except:
            print(f'I could not send `{text}` to `{channel}` :(')

        time_sleep = float(interval) - (time.time() - time_start)
        if time_sleep > 0:
            await asyncio.sleep(time_sleep)

@client.event
async def on_ready():
    for line in os.environ['DISCORD_CRON_CRONTAB'].split('\n'):
        try:
            interval, channel, text = line.split(',', 2)
            interval = float(interval.strip())
            channel = client.get_channel(channel.strip())
            text = text.strip()

            print(f'Scheduling `{text}` every {interval}s.')
            client.loop.create_task(speak(interval, channel, text))
        except:
            print('Could not schedule task.')
            traceback.format_exc()

try:
    client.run(os.environ['DISCORD_CRON_USER'], os.environ['DISCORD_CRON_PASS'])
except KeyError:
    client.run(os.environ['DISCORD_CRON_TOKEN'])

