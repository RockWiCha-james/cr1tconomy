import asyncio, discord, random, json, datetime
import math
from datetime import timedelta, date, time
from discord.ext import commands, tasks
client = commands.Bot(command_prefix=['c ', 'C '])
import os
from keep_alive import keep_alive


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def hunt(ctx):
  hunt_rarity = random.random(1, 10000)
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  try:
    if amounts[uid]['rifle'] >= 1:
      if hunt_rarity <= 4500:
        type_hunt = ["duck", "bunny"]
        hunted = random.randint(1, 10)
        hunt = random.choice(type_hunt)
        description = f"You were able to hunt {hunted} {hunt}s."
      elif hunt_rarity > 4500 and hunt_rarity <= 7500:
        hunted = 0
        hunted = "none"
        description = "You are such a noob that you did not hunt anything during this hunting time."
      elif hunt_rarity > 7500 and hunt_rarity <= 8000:
        hunted = 0
        hunt = "none"
        description = "AHAHAHAHA you broke your rifle."
        amounts[uid]['rifle'] -= 1
      elif hunt_rarity > 8000 and hunt_rarity <= 9000:
        list_of_items = ["deer", "squirrel", "rifle"]
        hunt = random.choice(list_of_items)
        hunted = 1
        description = f"Nice, you got a {hunt}, good job."
      elif hunt_rarity > 9000 and hunt_rarity <= 9750:
        list_of_hunt = ["elephant", "bird"]
        hunted = random.randint(1, 3)
        hunt = random.choice(list_of_hunt)
        description = f"Wow, you are a bit lucky because you were able to hunt {hunted} {hunt}s."
      elif hunt_rarity > 9750 and hunt_rarity <= 9995:
        list_of_hunt = ["dragon", "bobspetduck"]
        hunted = random.randint(1, 2)
        hunt = random.choice(list_of_hunt)
        description = f"Dang you just got very lucky today. You were able to hunt {hunted} {hunt}s."
      else:
        hunt = "bill"
        hunted = 1
        description = f"HOW DID YOU DO THIS. You somehow shot a BILL! He is such a small target. You are literally such a pro at hunting!"
      if hunt != "None":
        try:
          amounts[uid][hunt] += hunted
        except KeyError:
          amounts[uid][hunt] = 0
          _save()
          amounts[uid][hunt] += hunted
      if hunted >= 1:
        color = discord.Colour.green()
      else:
        color = discord.Colour.red()
      await ctx.send(embed = discord.Embed(title = "You hunted", description = description, color = color))
      amounts[uid]['bank-space'] += random.randint(1, 50)
      amounts[uid]['commands'] += 1
      _save()
    else:
      await ctx.send("You need a **Rifle** in order to hunt. You can't just hunt using your hands.")
  except KeyError:
    await ctx.send("You need a **Rifle** in order to hunt. You can't just hunt using your hands.")