import discord
import os
import datetime
import pytz
from keep_alive import keep_alive
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
token = os.getenv('TOKEN', '')

def getTime():
  current_time = datetime.datetime.now(datetime.timezone.utc)
  hst = pytz.timezone('Pacific/Honolulu')
  hawaii_time = current_time.astimezone(hst)
  hours = hawaii_time.hour
  # Determine whether it's AM or PM
  am_pm = "AM" if hours < 12 else "PM"
  # Convert hours from 24-hour format to 12-hour format
  hours %= 12
  # Adjust 0 hours to 12 for AM and format correctly
  hours = 12 if hours == 0 else hours
  return(f"{hours:02d}:{hawaii_time.minute:02d} {am_pm} HST")
                             
@client.event
async def on_ready():
    print('We are on')
    test.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hey back')

    if message.content.startswith('$time'):
        await message.channel.send(getTime())


@tasks.loop(seconds=10)
async def test():
  channel = client.get_channel(1090384168371896431)      
  if isinstance(channel, discord.TextChannel):
      await channel.send(getTime(), tts = True)
  else:
      print("Cannot send messages in non-text channels.")

client.run(token)