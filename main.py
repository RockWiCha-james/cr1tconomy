import asyncio, discord, random, json, datetime
import math
from datetime import timedelta, date, time
from discord.ext import commands, tasks
client = commands.Bot(command_prefix=['c ', 'C '])
import os
from keep_alive import keep_alive

"""
1st Value is item name
2nd Value is description
3rd value is the price to buy and 4th value is the price to sell
5th Value is if you can buy it
6th Value is if it is useable
7th value is the ID for the item
"""
great_shop = [
  ["Cube <:cube:950467818015584306> ", "A fun collectible you can use to get cubing", "200", "35", True, False, "cube"],
  
  ["Laptop <:laptop:950468257993883690> ", "A laptop used for certain commands such as ``c pcp``", "3000", "1000", True, False, "laptop"], 
  
  ["Fishing Pole <:fishingpole:950470121015640074> ", "An item that is very important when you want to fish (obviously)", "4000", "400", True, False, "fishingpole"], 
  
  ["Alcohol <:alcohol:950468550936641566> ", "What you can use to bet on certain commands and get more coins if you win but lose more coins if you lose!", "8000", "2500", True, True, "alcohol"], 
  
  ["Padlock <:padlock:950469023735365823> ", "Use this item to protect yourself from getting robbed", "10000", "3500", True, True, "padlock"], 
  
  ["Textbook <:textbook:950469701715251220> ", "An item that will help you get better jobs: check the list using ``c work list``", "15000", "4000", True, False, "book"], 
  
  ["Trout", "A fish that you can get and is common", "You can't buy this.", "50", False, False, "trout"], 
  
  ["Mackeral", "A fish that you can get and is also common", "You can't buy this", "75", False, False, "mackeral"], 
  
  ["A Shoe", "A shoe that is kinda rare, no you cant eat it (bob)", "You can't buy this", "400", False, False, "shoe"], 
  
  ["Jellyfish", "An aquatic creature that is quite rare", "You can't buy this", "900", False, False, "jellyfish"], 
  
  ["Octopus", "An aquatic creature that is rare and can be sold for some money", "You can't buy this", "999", False, False, "octopus"], 
  
  ["Whale", "A legendary fish that for some reason people can't catch", "You can't buy this", "7500", False, False, "whale"], 
  
  ["Shark", "A totally uncommon fish that you came across and was actually able to get.", "You can't buy this item.", "15500", False, False, "shark"], 

  ["Coin Fish", "The most epic fish in the world that almost no one has seen", "You can't buy this", "275830", False, False, "coinfish"],

  ["Hunting Rifle <:rifleeeee:950808039114563624>  ", "An item that is very important when you want to hunt (if u wanna know why its upside down its because its sleeping)", "5000", "500", True, False, "rifle"], 

  ["Duck", "Just a normal duck, nothing special about it", "You can't buy this.", "80", False, False, "duck"], 

  ["Bunny", "A harmless vunerable cute meal that you can eat and is tasty", "You can't buy this.", "110", False, False, "bunny"],

  ["Deer", "A deer that ran into your shot, you didnt even mean to kill it.", "You can't buy this", "420", False, False, "deer"],

  ["Squirrel", "Why would you kill this you sick bozo", "You can't buy this", "690", False, False, "squirrel"],

  ["Elephant", "**Fat.**", "You can't buy this", "1111", False, False, "elephant"],

  ["Bird", "You shot both its wings at once. Nice shot!", "You can't buy this", "1420", False, False, "bird"], 

  ["Dragon", "Dragon these balls across your face", "You can't buy this", "7500", False, False, "dragon"], 

  ["Bob's Pet Duck", "YOU MONSTER! Bob wont be very happy about this, no more nuggies for you.", "You can't buy this item.", "16000", False, False, "bobspetduck"], 
  
  ["Bill", "You somehow hit the smallest target. Thank god he's gone.", "You can't buy this item.", "275830", False, False, "bill"], 
  
  ["Game :video_game: ", "A collectible in which you can collect games to be a great gamer!", "50000", "18000", True, False, "game"], 
  
  ["Bob's Nuggie <:bobsnuggie:950445708861923368> ", "A rare collectible that is very tasty and cool", "1500000", "500000", True, False, "bobnuggie"], 
  
  ["Bob's Golden Nuggie <:goldennuggie:950446494840926208> ", "The biggest, juiciest most golden nuggie in existance.", "24999999", "7500000", True, False, "bobgoldnuggie"], 
  
  ["Fabian's Golden Pierogi <:fabiansgoldenpierogi:950451611971506206>  ", "Yes i didnt know what it was either, it do be shiny tho.", "25000000", "7500000", True, False, "fabiansgoldpierogi"], 
  
  ["Rock's Golden Rock <:rocksgoldenrock:950448867973943356> ", "Its just a cool rock ya know.", "25000000", "7500000", True, False, "rocksgoldrock"]
             ]

@client.event
async def on_ready():
    global amounts
    try:
      with open('amounts.json') as f:
            amounts = json.load(f)
    except FileNotFoundError:
        amounts = {}
    print("Bot online!")

@client.remove_command("help")
@client.command(aliases=['help_command'])
async def help(ctx, type_help = "None", page=1):
  if type_help == "None":
    embed = discord.Embed(title="Help Command", description = "Welcome to the Help Command. Look at what commands the bot has to offer! If there is a <> around some words, that means that what you put to substitute those words are optional Also [] around some words means that an input is required. However, first you need to choose what category you need help with. Type in the page number if you want also.", color = discord.Colour.green())
    embed.add_field(name = "``c help currency``", value = "Used if you need help with the currency system for the bot.", inline = False)
    embed.add_field(name = "``c help work``**__*(currently work in progress)*__**", value = "Work has its own category because this bot has to do with business. Commands have to do with work. It can overlap with ``c help currency`` but not really.\n ***Bot made by __Fabianpro__ & __RockWiCha__***", inline = False)
  elif type_help == "currency":
    if page == 1:
      embed = discord.Embed(title="Help Currency Command", description = "Here are all the commands having to do with currency and about them: ", color = discord.Colour.green())
      embed.add_field(name = "c bal <user>", value = "See how much money you have in your wallet and bank or what other users have in their wallet and bank.", inline = False)
      embed.add_field(name = "c beg", value = "When you want more money and you hope that someone gives some to you by using this command.", inline = False)
      embed.add_field(name = "c buy [item] <amount>", value = "Just buy an item from the shop, that's all.", inline = False)
      embed.add_field(name = "c betbot", value = "Bet against the bot a certain amount of coins.", inline = False)
      embed.add_field(name = "c betplayer <player>", value = "Bet some coins against a player. Follow the instructions that the bot says in order to see what outcome you have.", inline = False)
      embed.add_field(name = "c daily", value = "Be glad to get your daily number of coins.", inline = False)
      embed.add_field(name = "c dep [amount]", value = "Deposit money into your bank based on how much money you want to go in your bank", inline = False)
      embed.add_field(name = "c fish", value = "Get some fish using your trusty fishing pole.", inline = False)
      embed.add_field(name = "c hunt", value = "Get some dinner using your trusty hunting rifle.", inline = False)
      embed.add_field(name = "c hackathon", value = "Participate in some hackathons that you might have to pay for to get coins. You don't have to do anything for this just watch what results you get. However, if you do get a lot of coins and use this command, this command could possibly make you lose lots and lots of coins so just be careful and you might get lucky.")
      embed.add_field(name = "c inv", value = "See what items you have in your inventory", inline = False)
      embed.add_field(name = "c pcp", value = "Just post some coding projects not only for upvotes but for coins.", inline = False)
      embed.add_field(name = "c rich", value = "See who the richest people are using the bot ~~so you can rob them~~")
      embed.set_footer(text=f"Page {page} out of 2")
    elif page == 2:
      embed = discord.Embed(title="Help Currency Command", description = "Here are all the commands having to do with currency and about them: ", color = discord.Colour.green())
      embed.add_field(name = "c rob", value = "Rob someone because they have a lot of coins or some other reason. Try not to get caught by the police!", inline = False)
      embed.add_field(name = "c search", value = "When you go to a certain place to look for some coins.", inline = False)
      embed.add_field(name = "c shop", value = "When you go into the great shop and look for items you might want to buy", inline = False)
      embed.add_field(name = "c stats <user>", value = "See your\'s or other\'s stats (like money and number of commands)", inline = False)
      embed.add_field(name = "c stream", value = "Stream a video, post it, and see how many views, likes or dislikes, and coins you get. This command can be risky though so watch out...")
      embed.add_field(name = "c with [amount]", value = "Withdraw money out from the bank and put it into your wallet", inline = False)
    else:
      await ctx.send(f"Um no such page number as {page}")
  elif type_help == "moderation":
    if page == 1:
      embed = discord.Embed(title = "Help Moderation Command", description = "Here are all the commands that have to with moderating a server and about them: ", color = discord.Colour.green())
      embed.add_field(name = "c suggest [suggestion]", value = "Suggest things that will be able to help the bot or improve the server.", inline = False)
      embed.add_field(name = "c decision [number] [accepted?] <reason>", value = "Decide if a suggestion is approved or rejected and why that decision was made.", inline = False)
      embed.set_footer(text=f"Page {page} out of 1")
    else:
      await ctx.send(f"Um no such page number as {page}")
  elif type_help == "work":
    embed = discord.Embed(title = "Help Work Command", description = "Here are all the commands that have to do with the collection of work commands and about them:", color = discord.Colour.green())
    if page == 1:
      embed.add_field(name = "c work list", value = "Simply look at the work list too see what job you want to take on and the requirements you need to take on the job", inline = False)
      embed.set_footer(text = f"Page {page} out of 1")
    else:
      await ctx.send(f"Um no such page number as {page}")
  else:
    embed = discord.Embed(title = "What?", description = f"There is no category named {type_help} for help so look back at the ``c help`` command to see what categories you can look at.")
  await ctx.send(embed=embed)

@client.command()
async def stats(ctx, user:discord.Member=None):
  user=ctx.author if not user else user
  uid = str(user.id)
  if not uid in amounts:
    amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': '0'}
  embed = discord.Embed(title=f"{user.name}\'s Stats", description = "Here are your stats with this bot:", color = discord.Colour.blue())
  embed.add_field(name = "Balance Stats", value = f"Wallet: {amounts[uid]['coins']} \nBank: {amounts[uid]['bank-coins']}/{amounts[uid]['bank-space']}", inline = False)
  embed.add_field(name = "Command Stats", value = f"Total Commands: {amounts[uid]['commands']}")
  string = ""
  if amounts[uid]['job'] == "None":
    string = "Currently doesn't have a job"
  else:
    string = f"Currently works as a {amounts[uid]['job']}"
  embed.add_field(name = "Current Job", value = string, inline = False)
  await ctx.send(embed=embed)
  _save()
   
@client.command(aliases=['bal', 'money'])
async def balance(ctx, user:discord.Member=None):
    user=ctx.author if not user else user
    uid = str(user.id)
    if not uid in amounts:
        amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
    await ctx.send(embed = discord.Embed(title=f"{user.name}\'s Balance", description=f'{user.name} has **{amounts[uid]["coins"]}** coins in their wallet.\n{user.name} has **{amounts[uid]["bank-coins"]}/{amounts[uid]["bank-space"]}** coins in their bank.\n{user.name} has a total amount of **{amounts[uid]["coins"] + amounts[uid]["bank-coins"]}** coins.', color = discord.Colour.green()))
    amounts[uid]['bank-space'] += random.randint(1, 50)
    amounts[uid]['commands'] += 5
    _save()  

@client.command()
async def shop(ctx):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  embed = discord.Embed(title="The Great CR1TCONOMY Store", description = "Where you can buy items", color = discord.Colour.blue())
  for i in range(len(great_shop)):
    if great_shop[i][4] == True:
      embed.add_field(name=(great_shop[i][0] + " - " + great_shop[i][2] + " coins - ID: ``" + great_shop[i][6] + "``"), value = great_shop[i][1], inline = False)
  amounts[uid]['bank-space'] += random.randint(1, 50)
  amounts[uid]['commands'] += 1
  await ctx.send(embed=embed)
  _save()

@client.command()
async def buy(ctx, item, amount=1):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  for i in range(len(great_shop)):
    if great_shop[i][6].lower() == item.lower():
      if str(amount).isdigit():
        if amounts[uid]['coins'] >= (int(great_shop[i][2]) * int(amount)) and amount >= 1:
          try:
            amounts[uid][great_shop[i][6].lower()] += amount
          except KeyError:
            amounts[uid][great_shop[i][6].lower()] = 0
            _save()
            amounts[uid][great_shop[i][6].lower()] += amount
          amounts[uid]['bank-space'] += random.randint(1, 50)
          amounts[uid]['commands'] += 1
          await ctx.send(embed = discord.Embed(title="Transaction Complete", description=f"You got {amount} {(great_shop[i][0]).lower()}s for {int(great_shop[i][2]) * amount} coins.", color = discord.Colour.green()))
          amounts[uid]['coins'] -= (int(great_shop[i][2]) * int(amount))
          _save()
          break
        else:
          await ctx.send("Are you ok? Because you don't have enough money to buy this many items or you can't buy 0 or negative number of items.")
          break
      else:
        await ctx.send("You need to enter in an integer stupid.")
        break
    elif great_shop[i][6].lower() != item.lower() and i == len(great_shop) - 1:
      await ctx.send("You should check the shop using ``c shop`` in order to buy items because you put in an item that does not exist.")

@client.command(aliases=['inventory'])
async def inv(ctx):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  keys_list = list(amounts[uid])
  values = amounts[uid].values()
  values_list = list(values)
  embed = discord.Embed(title="Your Inventory:", description="Here are what items you have in your inventory: ", color = discord.Colour.blue())
  embed1 = discord.Embed(title = "Your Inventory:", description="Unfortunately, you have nothing in your inventory.", color = discord.Colour.orange())
  inventory_items = False
  for i in range(9, len(amounts[uid])):
    if values_list[i] != 0:
      inventory_items = True
      embed.add_field(name=f"{keys_list[i]}", value = f"{values_list[i]} owned", inline = False)
  if inventory_items == False:
    await ctx.send(embed=embed1)
  else:
    await ctx.send(embed=embed)
  amounts[uid]['bank-space'] += random.randint(1, 50)
  amounts[uid]['commands'] += 1
  _save()

@client.command()
async def sell(ctx, item, amount=1):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  for i in range(len(great_shop)):
    if great_shop[i][6].lower() == item.lower():
      if str(amount).isdigit():
        if amount <= amounts[uid][great_shop[i][6].lower()]:
          earn_coins = int(great_shop[i][3]) * amount
          amounts[uid][great_shop[i][6].lower()] -= amount
          amounts[uid]['coins'] += earn_coins
          await ctx.send(embed=discord.Embed(title="Transaction Complete", description=f"You sold {amount} {(great_shop[i][0]).lower()}s for a total of {earn_coins} coins.", color = discord.Colour.green()))
          amounts[uid]['bank-space'] += random.randint(1, 50)
          amounts[uid]['commands'] += 1
          _save()
          break
        else:
          await ctx.send("Are you ok? Check your items using ``c inv`` next time because you don't even have that many items.")
          break
      else:
        await ctx.send("Stupid for the amount you need to put **a number that is at least 1**")
        break
    elif great_shop[i][6].lower() != item.lower() and i == len(great_shop) - 1:
      await ctx.send("Seroiusly you need to check the shop using ``c shop`` to find the id that you are using because the item you put does not exist.")
  _save()

@client.command()
async def use(ctx, item):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  for i in range(len(great_shop)):
    try:
      if great_shop[i][6] == item and great_shop[i][5] == True and amounts[uid][great_shop[i][6]] >= 1:
        name = item + "_use"
        if amounts[uid][name] == False:
          amounts[uid][great_shop[i][6]] -= 1
          amounts[uid][name] = True
          title = f"You successfully used the {great_shop[i][6]} item!"
          color = discord.Colour.green()
          if great_shop[i][6] == "alcohol":
            amounts[uid]['alcohol_times'] = 10
            description = "You used the alcohol item and you are not drunk! Now for the next 10 bets or whatever gambling command you use, you can earn twice the money if you win but lose twice the money if you lose."
            break
          elif great_shop[i][6] == "padlock":
            description = "Nice, you used the padlock item. Now the person who robs you next time will only have a 0.1% chance of being able to rob your wallet!"
            break
        else:
          await ctx.send(f"You are already using the {great_shop[i][6]} item!")
          break
      elif great_shop[i][6] != item and great_shop[i][5] != True and amounts[uid]  [great_shop[i][6]] == 0 and i == len(great_shop) - 1:
        print("f")
        print(i)
        title = "What?"
        description = "I have no clue you need to check your inventory or something cause you can't use this item or don't have the item."
        color = discord.Colour.orange()
    except KeyError:
      title = "What?"
      description = "I have no clue you need to check your inventory cause you can't use this item or don't have the item."
      color = discord.Colour.orange()
  _save()
  await ctx.send(embed=discord.Embed(title=title, description=description, color=color))

"""
1st item is job name
2nd item is the description
3rd item is the salary
4th item is the wallet req
5th item is the bank space req
6th item is the book req
7th item is a dictionary of req items
8th item is the id
9th item is the page number
"""
jobs = [["Student", "You are a student and just learning things.", "100 - 500", "0", "50", "0", {"cube": 1}, "student", "1"], ["Youtuber", "Go on YouTube and stream some nice videoes.", "250 - 1000", "250", "150", "0", {"cube": 3}, "youtuber", "1"], ["Internet Surfer", "You are a random person who took on a job in which you surf the Internet idk.", "750 - 1500", "1000", "1500", "0", {"cube": 5, "laptop": 2}, "surfer", "2"]]

@client.command()
async def work(ctx, job_action = "none", page = "1"):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  if job_action == "list":
    embed = discord.Embed(title = "The Great Job List", description = "This is called CR1TCONOMY for a reason. The work commands will be one of the largest commands that this bot has to offer. To pick the jobs you want, simply do ``c work [id]`` Here are the possible jobs you can get with this bot:\n", color = discord.Colour.blue())
    job_found = False
    for i in range(len(jobs)):
      if page == jobs[i][8]:
        job_found = True
        list_of_items = ""
        for a in range(len(jobs[i][6])):
          keys_list = list(jobs[i][6].keys())
          values_list = list(jobs[i][6].values())
          list_of_items += f"\n{keys_list[a].capitalize()}: {values_list[a]}"
        embed.add_field(name = f"==============================================\n__{jobs[i][0]}__", value = f"Description: {jobs[i][1]}\nSalary: {jobs[i][2]}\n\n**Requirements:**\nWallet Coins: {jobs[i][3]}\nBankspace Needed: {jobs[i][4]}\nBooks Needed: {jobs[i][5]}\n\n**Items Needed:** {list_of_items}\n\n**Getting ID:**\nIf you want to get this job use the id ``{jobs[i][7]}``.", inline = False)
        embed.set_footer(text = f"Page {page} out of 2")
      elif page != jobs[i][8] and i == len(jobs) - 1 and job_found == False:
        await ctx.send(f"Currently, there is no page {page} so I have no clue what you are doing...")
      if i == len(jobs) - 1 and job_found == True:
        await ctx.send(embed=embed)
  elif job_action == "resign":
    await ctx.send("In Progress")
  elif job_action == "none":
    await ctx.send("In Progress")
  else:
    for i in range(len(jobs)):
      if job_action == jobs[i][7]:
        list_of_req = ""
        for b in range(len(jobs[i][6])):
          keys_list = list(jobs[i][6].keys())
          values_list = list(jobs[i][6].values())
          try:
            if amounts[uid][keys_list[b]] >= values_list[b]:
              await ctx.send("Yes")
            else:
              list_of_req += f"\nYou need {values_list[b] - amounts[uid][keys_list[b]]} more {keys_list[b]} items."
            print(list_of_req)
          except KeyError:
            list_of_req += f"You need {values_list[b] - amounts[uid][keys_list[b]]} more {keys_list[b]} items."
            print(list_of_req)
        break
      elif job_action != jobs[i][7] and i == len(jobs) - 1:
        await ctx.send(f"Look at the list by typing in the command ``c job list`` again because apparently, there is no id name ``{job_action}`` in the job list.")

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

@client.command()
async def daily(ctx):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  if amounts[uid]['dailytime'] == 0:
    coins = random.randint(2500, 5000)
    await ctx.send(f"Here you have like {coins} coins.")
    amounts[uid]['dailytime'] = myconverter(datetime.datetime.now())
    amounts[uid]['coins'] += coins
    amounts[uid]['bank-space'] += random.randint(1, 50)
    amounts[uid]['commands'] += 1
  else:
    time_conversion = datetime.datetime.strptime(str(amounts[uid]['dailytime']), "%Y-%m-%d %H:%M:%S.%f")
    time_conversion1 = datetime.datetime.strptime(myconverter(datetime.datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
    change_day = time_conversion + timedelta(days=1)
    time_difference = change_day - time_conversion1
    total_seconds1 = round(time_difference.total_seconds())
    if total_seconds1 < 0:
      coins = random.randint(5000, 10000)
      await ctx.send(f"Here you have like {coins} coins.")
      amounts[uid]['dailytime'] = (myconverter(datetime.datetime.now()))
      amounts[uid]['coins'] += coins
      amounts[uid]['bank-space'] += random.randint(1, 50)
      amounts[uid]['commands'] += 1
    else:
      coins = 0
      hours = math.floor(total_seconds1/3600)
      minutes = math.floor(((total_seconds1) - (hours * 3600))/60)
      seconds = round((total_seconds1) - (hours*3600) - (minutes*60))
      await ctx.send(embed = discord.Embed(title="Cooldown Active", description=f"Stop using this command because literally it\'s called daily for a reaosn. Wait {hours} hours, {minutes} minutes, {seconds} seconds before getting your daily number of coins.", color = discord.Colour.orange()))
    coins = 0
  _save()

@client.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def rob(ctx, user:discord.Member="None"):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  if user == "None":
    await ctx.send("You need to provide a **user** to rob because you can't just rob no one.")
  elif user.name == ctx.author.name:
    await ctx.send("Don't even try robbing yourself because you already own the coins and blah blah blah do you have common sense?")
  else:
    if amounts[uid]['coins'] < 1500:
      await ctx.send("You need at least 1500 coins to rob.")
    else:
      if amounts[str(user.id)]['coins'] < 1500:
        await ctx.send("The person you are robbing is too poor don't try it.")
      else:
        if amounts[str(user.id)]['padlock_use'] == True:
          amounts[str(user.id)]['padlock_use'] = False
          coin_chances = random.random()
          if coin_chances <= 0.7:
            loss_percentage = random.randint(10, 50)
            coins1 = int(amounts[uid]['coins'] * (loss_percentage/100) * -1)
            coins2 = coins1 * -1
            title = "The person you tried to rob had a padlock and you didn't succeed getting the money!"
            description = f"You at least broke the padlock but it took too long because suddenly look who was standing in front of you {user.name}. The user demanded you gave some coins to the person and if you won't you will get tortured. You had no choice but to give the person {loss_percentage}% of your coins (aka {coins1 * -1} coins). Now you had {int(amounts[uid]['coins'] + coins1)} coins while {user.name} has {int(amounts[str(user.id)]['coins'] + coins2)} coins."
            color = discord.Colour.red()
            await user.send(f"{ctx.author.name} tried to rob you, but you had a padlock active and cool they had to pay you {coins2} coins!")
          elif coin_chances > 0.7 and coin_chances <= 0.9:
            loss_percentage = random.randint(10, 50)
            coins1 = int(amounts[uid]['coins'] * (loss_percentage/100) * -1)
            coins2 = 0
            title = "The person you tried to rob had a padlock and you didn't succeed getting the money!"
            description = f"Well, at least you broke the padlock. But you took too long because as soon as you know it, the police were there. You ended up having to pay a fine of {coins1 * -1} coins which is {loss_percentage}% less coins than what you had before and now you have {int(amounts[uid]['coins'] + coins1)} coins."
            color = discord.Colour.red()
            await user.send(f"{ctx.author.name} tried to rob you, but you had a padlock active and the police caught the user!")
          else:
            gain_percentage = random.randint(10, 50)
            coins2 = int(amounts[str(user.id)]['coins'] * (gain_percentage/100)) * -1
            coins1 = coins2 * -1
            if gain_percentage <= 25:
              title = "You stole a small chunk of the person's money!"
            else:
              title = "You stole a nice chunk of the person's money!"
            description = f"Nice, you were able to break the padlock and had enough time to get coins. However, you felt rushed because you didn't want the police to come so you stole {gain_percentage}% (aka {coins1} coins) of their coins now making them have {amounts[str(user.id)]['coins'] + coins2} coins and you having {amounts[uid]['coins'] + coins1} coins."
            color = discord.Colour.green()
            await user.send(f"{ctx.author.name} tried to rob you, but you had a padlock active **but** they were able to break it and get away with {coins1} coins.")
        else:
          coin_chances = random.random()
          if coin_chances <= 0.45:
            loss_percentage = random.randint(10, 50)
            coins1 = int(amounts[uid]['coins'] * (loss_percentage/100)) * -1
            coins2 = coins1 * -1
            title = "You tried to steal and the person didn't have a padlock but you failed!"
            description = f"Apparently, you tried to steal some money from the wallet except suddenly when you looked behind you saw {user.name} behind you! {user.name} threatened to give them some money so you ended giving the person {loss_percentage}% of the money (aka {coins2} coins) so now you have {amounts[uid]['coins'] + coins1} while {user.name} has a good amount of {amounts[str(user.id)]['coins'] + coins2}"
            color = discord.Colour.red()
            await user.send(f"{ctx.author.name} tried to rob you, and luckily they had to pay you {coins2} coins because they didn't succeed.")
          elif coin_chances > 0.45 and coin_chances <= 0.75:
            loss_percentage = random.randint(10, 50)
            coins1 = int(amounts[uid]['coins'] * (loss_percentage/100)) * -1
            coins2 = 0
            title = "You tried to steal and the person didn't have a padlock but you still failed!"
            description = f"You tried to steal money from their wallet and then suddenly you were handcuffed by the police and taken to jail. You had to pay a fine of {coins1 * -1} coins so therefore you have {loss_percentage}% less coins and now have {amounts[uid]['coins'] + coins1} coins."
            color = discord.Colour.red()
            await user.send(f"{ctx.author.name} tried to rob you, and luckily the police caught the user and the user had to pay a fine!")
          else:
            gain_percentage = random.randint(5, 90)
            coins2 = int(amounts[str(user.id)]['coins'] * (gain_percentage/100)) * -1
            coins1 = coins2 * -1
            if gain_percentage <= 25:
              title = "You stole a small chunk of the person's money."
            elif gain_percentage > 25 and gain_percentage <= 50:
              title = "You stole a nice chunk of the person's money."
            elif gain_percentage > 50 and gain_percentage <= 80:
              title = "You stole a good chunk of the person's money."
            else:
              title = "You stole a big chunk of the person's money."
            description = f"You stole their money easily and you did not take too long to steal it. Also, no one caught you robbing so that was great! You stole {gain_percentage}% of their money so now {user.name} has {amounts[str(user.id)]['coins'] + coins2} while you have {amounts[uid]['coins'] + coins1} coins."
            color = discord.Colour.green()
            await user.send(f"{ctx.author.name} robbed you and the user succeeded! They got away with {coins1} coins!")
        amounts[uid]['coins'] += coins1
        amounts[str(user.id)]['coins'] += coins2
        amounts[uid]['bank-space'] += random.randint(1, 50)
        amounts[uid]['commands'] += 1
        await ctx.send(embed=discord.Embed(title = title, description = description, color = color))
        _save()


@client.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def betplayer(ctx, user:discord.Member="None"):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  def check1(msg):
    try:
      return msg.content.lower() == "accept bet" and msg.author.id != int(uid) and amounts[str(msg.author.id)]['coins'] >= 1000
    except KeyError:
      return False
  def check2(msg):
    return msg.content.lower() == "accept bet" and msg.author.id == user.id
  def check3(msg):
    return msg.content.isdigit() and msg.author.id == ctx.author.id and int(msg.content) <= 500000 and int(amounts[uid]['coins']) > int(msg.content) and int(msg.content) >= 1000
  def check4(msg):
    try:
      return msg.content.isdigit() and msg.author.id == user.id and int(msg.content) <= 500000 and int(amounts[str(user.id)]['coins']) > int(msg.content) and int(msg.content) >= 1000
    except AttributeError:
      return msg.content.isdigit() and msg.author.id == author and int(msg.content) <= 500000 and int(amounts[str(msg.author.id)]['coins']) > int(msg.content) and int(msg.content) >= 1000
  person_good = False
  if amounts[uid]['coins'] >= 1000:
    try:
      if user == "None":
        message = await ctx.send(f"No players were requested. Anyone can type ``accept bet`` to bet against {ctx.author.name}. Whoever wants to do this has 1 minute to do so. The person must have at least 1,000 coins.")
        msg = await client.wait_for("message", timeout=60, check=check1)
        person_good = True
      elif user != "None" and amounts[str(user.id)]['coins'] >= 1000 and user.id != ctx.author.id:
        message = await ctx.send(f"{user.mention} was requested for the bet. {user.name}, please type in ``accept bet`` if you accept this bet. You have 1 minute to do so.")
        msg = await client.wait_for("message", timeout=60, check=check2)
        person_good = True
      else:
        await ctx.send("The person doesn't have **1000** coins like you do so you can't bet with them. You need to try again. Also, another reason why you could have gotten this message is because you can't bet with yourself.")
      if person_good == True:
        try:
          message = await ctx.send(f"{user.mention} has accepted the bet! {ctx.author.mention}, you will go first. You need to choose a number between 1000 and 500,000.")
        except AttributeError:
          message = await ctx.send(f"{msg.author.mention} has accepted the bet! {ctx.author.mention}, you will go first. You need to choose a number between 1000 and 500,000. You have 30 seconds to do so.")
        sum_of_bet = 0
        msg1 = await client.wait_for("message", timeout=30, check=check3)
        msg1 = int(msg1.content)
        if amounts[uid]['alcohol_use'] == True:
          msg1 = msg1 * 2
          amounts[uid]['alcohol_times'] -= 1
          if amounts[uid]['alcohol_times'] == 0:
            amounts[uid]['alcohol_use'] = False
          await ctx.send(f"Well, you had alcohol so your bet actually came up to {msg1} coins.")
        try:
          message = await ctx.send(f"Cool, so now it is {user.mention}'s turn to choose a bet number. This will be added up at the end. Again, this has to be a number between 1000 and 500,000. Also, you have 30 seconds to do this.")
        except AttributeError:
          message = await ctx.send(f"Cool, so now it is {msg.author.mention}'s turn to choose a bet number. This will be added up at the end. Again, this has to be a number between 1000 and 500,000. Also, you have 30 seconds to do this.")
        author = msg.author.id
        msg2 = await client.wait_for("message", timeout=30, check=check4)
        msg2 = int(msg2.content)
        if amounts[str(msg.author.id)]['alcohol_use'] == True:
          msg2 = msg2 * 2
          amounts[str(msg.author.id)]['alcohol_times'] -= 1
          if amounts[str(msg.author.id)]['alcohol_times'] == 0:
            amounts[str(msg.author.id)]['alcohol_use'] = False
          await ctx.send(f"Well, you had alcohol so your bet actually came up to {msg2} coins.")
        sum_of_bet = msg1 + msg2
        person1_roll = random.randint(1, 2)
        person2_roll = random.randint(1, 2)
        if person1_roll > person2_roll:
          coins1 = sum_of_bet
          coins2 = msg2 * -1
          title = f"{ctx.author.name} won!"
          description = f"Congratulations {ctx.author.name}, you won the bet! The total money that was betted is {sum_of_bet} coins. While {ctx.author.name} gets {amounts[uid]['coins'] + sum_of_bet} coins, unfortunately {msg.author.name} now has {amounts[uid]['coins'] - msg2} coins. Here are the results: \n\n{ctx.author.name} rolled {person1_roll}\n{msg.author.name} rolled {person2_roll}"
          description = f"Congratulations {ctx.author.name}, you won the bet! The total money that was betted is {sum_of_bet} coins. While {ctx.author.name} now has {amounts[uid]['coins'] + sum_of_bet} coins, unfortunately {msg.author.name} now has {amounts[str(msg.author.id)]['coins'] - msg2} coins. Here are the results: \n\n{ctx.author.name} rolled {person1_roll}\n{msg.author.name} rolled {person2_roll}"
          color = discord.Colour.green()
        elif person1_roll < person2_roll:
          coins1 = msg1 * -1
          coins2 = sum_of_bet
          title = f"{msg.author.name} won!"
          description = f"Congratulations {msg.author.name}, you won the bet! The total money that was betted is {sum_of_bet} coins. While {msg.author.name} now has {amounts[str(msg.author.id)]['coins'] + sum_of_bet} coins, unfortunately {ctx.author.name} has {amounts[uid]['coins'] - msg1} coins. Here are the results: \n\n{ctx.author.name} rolled {person1_roll}\n{msg.author.name} rolled {person2_roll}"
          color = discord.Colour.green()
        else:
          coins1 = int(sum_of_bet/4)
          coins2 = int(sum_of_bet/4)
          title = f"{ctx.author.name} and {msg.author.name} did not win or lose!"
          description = f"In fact, both of you got the same number. Therefore, we will divide the sum of the bet, {sum_of_bet}, by 2 and split it up for each of you. Therefore, each of you will get {int(sum_of_bet/4)} coins. {ctx.author.name} now has {amounts[uid]['coins'] + int(sum_of_bet/4)} coins while {msg.author.name} now has {amounts[str(msg.author.id)]['coins'] + int(sum_of_bet/4)} coins. Here are the results: \n\nBoth of you got {person1_roll}."
          color = discord.Colour.orange()
        amounts[uid]['coins'] += coins1
        amounts[str(msg.author.id)]['coins'] += coins2
        if amounts[uid]['coins'] < 0:
          await ctx.send(f"{ctx.author.name}, you had a negative amount of money. You already have insurance for this so they already paid your debt for you. You now have 0 coins again.")
          amounts[uid]['coins'] = 0
        elif amounts[str(msg.author.id)]['coins'] < 0:
          await ctx.send(f"{msg.author.name}, you had a negative amount of money. You already have insurance for this so they already paid your debt for you. You now have 0 coins again.")
          amounts[str(msg.author.id)]['coins'] = 0
        await ctx.send(embed=discord.Embed(title=title, description=description, color=color))
        amounts[uid]['bank-space'] += random.randint(1, 50)
        amounts[uid]['commands'] += 1
        _save()
    except asyncio.TimeoutError:
      await message.edit(content="No one ended up responding so the player bet was cancelled.")
  else:
    await ctx.send("You need **1000** coins to bet against a player are you fine?")

@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def betbot(ctx, amount):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  if amount == "all":
    if amounts[uid]['coins'] >= 500000:
      amount = 500000
    else:
      amount = amounts[uid]['coins']
  if int(amount) < 1000:
    await ctx.send("Bruh, you have to bet at least 1000 coins for this.")
  elif int(amount) > 500000:
    await ctx.send("Bruh you can't even bet that many coins at once so you have to bet at most 500,000 coins.")
  elif amounts[uid]['coins'] < int(amount):
    await ctx.send("Are you ok? You don't even have that many coins!")
  else:
    bot_roll = random.randint(3, 20)
    person_roll = random.randint(1, 20)
    if person_roll < bot_roll:
      color = discord.Colour.red()
      title = "You lost against the bot and lost your coins!"
      coins = (int(amount) * -1)
      add = False
      if amounts[uid]['alcohol_use'] == True:
        amounts[uid]['alcohol_times'] -= 1
        coins = coins * 2
        add = True
        if amounts[uid]['alcohol_times'] == 0:
          amounts[uid]['alcohol_use'] = False
      description = f"\n\nYou noob you lost to the bot! Your bet was **{amount}** coins so therefore you ended up losing those coins and now you have **{str(int(amounts[uid]['coins'] - int(amount)))}** coins. Here were the results: \n\nYou rolled {person_roll}. \nCR1TCONOMY rolled {bot_roll}."
      if add == True:
        description += f"\n\nYou also had some alcohol so uh OOF now you have **{amounts[uid]['coins'] + int(coins)}** coins (because you lost 2 times more coins for your bet since really you did a bet of **{str(int(coins) * -1)}** coins)"
    elif person_roll > bot_roll:
      percentage_win = random.randint(5, 100)
      color = discord.Colour.green()
      title = "You won against the bot and won coins!"
      original_amount = amount
      amount = int(amount) * (percentage_win/100)
      coins = amount
      add = False
      if amounts[uid]['alcohol_use'] == True:
        amounts[uid]['alcohol_times'] -= 1
        percentage_win1 = percentage_win * 2
        coins = coins * 2
        add = True
        if amounts[uid]['alcohol_times'] == 0:
          amounts[uid]['alcohol_use'] = False
      description = f"You won against the bot nice and now you get **{percentage_win}%** more coins compared to your bet. Your bet was **{original_amount}** coins so therefore you now have **{str(int(amounts[uid]['coins'] + amount))}** coins. Here were the results: \n\nYou rolled {person_roll}. \nCR1TCONOMY rolled {bot_roll}."
      if add == True:
        description += f"\n\nYou also had some alcohol so big money big money. Now the percentage that you go was actually **{percentage_win1}%** so NICE (because you had some nice alcohol). Anyways now you have **{str(int(amounts[uid]['coins'] + int(coins)))}** coins."
    else:
      color = discord.Colour.orange()
      title = "You tied against the bot and unfortunately lost some coins."
      percentage_lose = random.randint(25, 75)
      original_amount = amount
      amount = int(amount) * (percentage_lose/100) * -1
      coins = amount
      add = False
      if amounts[uid]['alcohol_use'] == True:
        amounts[uid]['alcohol_times'] -= 1
        add = True
        if amounts[uid]['alcohol_times'] == 0:
          amounts[uid]['alcohol_use'] = False
      description = f"You tied against the bot so you ended up losing **{percentage_lose}%** of your coins compared to your bet! Your bet was **{original_amount}** and now you have **{str(int(amounts[uid]['coins'] + coins))}** coins. Here were the results: \n\nBoth of you got {person_roll}."
      if add == True:
        description += f"\n\nOOF! You had alcohol but guess what? You actually tied so yeah for this situation alcohol didn't matter. You still have the same number of coins you had before. However, you still lost a chance. (like one of your ten chances)"
    amounts[uid]['coins'] += int(coins)
    if amounts[uid]['coins'] < 0:
      amounts[uid]['coins'] = 0
      await ctx.send("You can't have debt for this so your insurance took care of your debt.")
    await ctx.send(embed=discord.Embed(title=title, description=description, color=color))
    amounts[uid]['bank-space'] += random.randint(1, 50)
    amounts[uid]['commands'] += 1
  _save()

@client.command()
async def rich(ctx):
  uid = str(ctx.author.id)
  rich_people = {}
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  for a in range(len(amounts)):
    keys_list = list(amounts)
    values_list = list(amounts[keys_list[a]].values())
    rich_people[keys_list[a]] = int(values_list[0])
  rich_people = sorted(rich_people.items(), key=lambda rich: rich[1], reverse=True)
  embed = discord.Embed(title = "Richest People with the Currency Bot", description = f"A list of the richest people who are using the Currency Bot", color = discord.Colour.blue())
  i = 0
  for a in range(len(rich_people)):
    try:
      username = client.get_user(int(rich_people[a][0])).name
      i += 1
    except AttributeError:
      continue
    if i == 1:
      embed.add_field(name = f":first_place: {username}: ", value = f"{rich_people[a][1]} coins", inline = False)
    elif i == 2:
      embed.add_field(name = f":second_place: {username}: ", value = f"{rich_people[a][1]} coins", inline = False)
    elif i == 3:
      embed.add_field(name = f":third_place: {username}: ", value = f"{rich_people[a][1]} coins", inline = False)
    else:
      digits_list = list(str(i))
      string = ""
      for j in range(len(digits_list)):
        if digits_list[j] == "0":
          string += ":zero:"
        elif digits_list[j] == "1":
          string += ":one:"
        elif digits_list[j] == "2":
          string += ":two:"
        elif digits_list[j] == "3":
          string += ":three:"
        elif digits_list[j] == "4":
          string += ":four:"
        elif digits_list[j] == "5":
          string += ":five:"
        elif digits_list[j] == "6":
          string += ":six:"
        elif digits_list[j] == "7":
          string += ":seven:"
        elif digits_list[j] == "8":
          string += ":eight:"
        elif digits_list[j] == "9":
          string += ":nine:"
      embed.add_field(name = f"{string} {username}:", value = f"{rich_people[a][1]} coins", inline = False)
    amounts[uid]['bank-space'] += random.randint(1, 50)
    amounts[uid]['commands'] += 1
    _save()
  await ctx.send(embed=embed)

@commands.cooldown(1, 60, commands.BucketType.user)
@client.command()
async def hackathon(ctx):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  try:
    if amounts[uid]['laptop'] >= 5:
      times = 1
      if amounts[uid]['coins'] >= 5000:
        times += 1
        if amounts[uid]['coins'] >= 20000:
          times += 1
          if amounts[uid]['coins'] >= 100000:
            times += 1
            if amounts[uid]['coins'] >= 500000:
              times += 1
      random_competition = random.randint(1, times)
      if random_competition == 1:
        coin_chance = random.random()
        if coin_chance <= 0.9:
          coins = random.randrange(10, 50, 5)
          description = f"You ended up participating in a free hackathon. You didn't do so well on it but since you at least participated you got {coins} coins."
        elif coin_chance > 0.9 and coin_chance <= 0.96:
          coins = random.randrange(100, 250, 10)
          description = f"You participated in a free hackathon and got 3rd place! The prize for 3rd place in this competition is {coins} coins."
        elif coin_chance > 0.96 and coin_chance < 0.995:
          coins = random.randrange(350, 750, 10)
          description = f"You participated in a free hackathon and got 2nd place! The prize for 2nd place in this competition is {coins} coins."
        else:
          coins = random.randrange(1000, 2500, 50)
          description = f"You participated in a free hackathon and got 1st place! The grand prize for the competition is {coins} coins."
      elif random_competition == 2:
        coin_chance = random.random()
        coin_fee = random.randrange(2500, 5000, 100)
        if coin_chance <= 0.95:
          coins = random.randrange(100, 500, 10)
          description = f"You participated in a hackathon that had around 50 - 100 people in it. There was a coin fee for this one which is {coin_fee} coins and unfortunately you didn't win. However, for participation, you got {coins} coins."
        elif coin_chance > 0.95 and coin_chance <= 0.985:
          coins = coin_fee + random.randrange(1000, 2000, 10)
          description = f"You participated in a kind of small hackathon which had a coin fee of {coins} coins. However, congratulations because you got 3rd place in it. Therefore you ended up getting {coins} coins because of your postition."
        elif coin_chance > 0.985 and coin_chance < 0.9985:
          coins = coin_fee + random.randrange(3000, 7500, 50)
          description = f"You participated in a kind of small hackathon which had a fee of {coins} coins. However, you did very well and was able to get 2nd place which led you getting out of the hackathon with {coins} coins."
        else:
          coins = coin_fee + random.randrange(10000, 25000, 100)
          description = f"You participated in a kind of small hackathon which had a fee of {coins} coins. However, you did so well that you were the winner of the hackathon and won the grand prize of {coins} coins."
        coins -= coin_fee
      elif random_competition == 3:
        coin_chance = random.random()
        coin_fee = random.randrange(10000, 20000, 100)
        if coin_chance <= 0.925:
          coins = 0
          description = f"You participated in a statewide hackathon which had a massive fee of {coin_fee} coins. Unfortunately, you were not able to get a good position and there will no coins for participation."
        elif coin_chance > 0.925 and coin_chance <= 0.97:
          coins = 0
          description = f"You participated in a statewide hackathon which had a massive fee of {coin_fee} coins. Unfortunately, you got a trash position and you got so triggered that you broke your laptop AHAHAHAHAHAHAAHHAHAHA."
          amounts[uid]['laptop'] -= 1
        elif coin_chance > 0.97 and coin_chance <= 0.99:
          coins = coin_fee + random.randrange(8000, 15000, 50)
          description = f"You participated in a statewide hackathon that had a fee of {coin_fee} coins. Congratulations cause somehow you were so good that you got 3rd place and walked out with {coins} coins."
        elif coin_chance > 0.99 and coin_chance < 0.99997:
          coins = coin_fee + random.randrange(20000, 45000, 100)
          description = f"You participated in a statewide hackathon that had a fee of {coin_fee} coins. Fortunately, you did so well that you got 2nd place and ended up walking out of the place with a massive amount of {coins} coins."
        else:
          coins = coin_fee + random.randrange(50000, 100000, 100)
          description = f"You participated in a statewide hackathon with a fee of {coin_fee} coins and yet SOMEHOW YOU GOT 1ST LIKE HOW WERE YOU LIKE CHEATING OR SOMETHING? Ok that doesn't matter because anyways the grand prize was {coins} coins so uh yeah."
        coins -= coin_fee
      elif random_competition == 4:
        coin_chance = random.random()
        coin_fee = random.randrange(40000, 100000, 200)
        if coin_chance <= 0.91:
          coins = 0
          description = f"You participated in a nationwide hackathon and did not get a good position. However, you weren't triggered but you didn't any coins. In fact, the fee was really high when you got in and it was like {coin_fee} coins literally."
        elif coin_chance > 0.91 and coin_chance <= 0.9825:
          coins = 0
          description = f"You participated in a nationwide hackathon and got a terrible position. This nationwide hackathon cost {coin_fee} coins and you were so triggered about how much money you wasted that you broke you laptop AHAHAHAHAHA"
          amounts[uid]['laptop'] -= 1
        elif coin_chance > 0.9825 and coin_chance <= 0.994:
          coins = coin_fee + random.randrange(20000, 50000, 100)
          description = f"You participated in a nationwide hackathon that cost {coin_fee} coins and you SOMEHOW GOT 3RD PLACE I MEAN LIKE HOW! Anyways you ended up getting {coins} coins."
        elif coin_chance > 0.994 and coin_chance <= 0.999999:
          coins = coin_fee + random.randrange(75000, 200000)
          description = f"You participated in a nationwide hackathon that cost {coin_fee} coins and you GOT 2ND PLACE DANG YOU HACKER! You got {coins} coins that you were able to put in your wallet."
        else:
          coins = coin_fee + random.randrange(100000, 500000, 1000)
          description = f"You participated in a nationwide hackathon that cost {coin_fee} and you just WERE BEING SUCH A HACKER BECAUSE THERE'S NO WAY YOU COULD HAVE GOTTEN FIRST PLACE I MEAN LIKE HOW!!!!!! Anyways, the grand prize was {coins} coins so be glad you got coins."
        coins -= coin_fee
      else:
        coin_chance = random.random()
        coin_fee = random.randrange(200000, 500000)
        if coin_chance <= 0.875:
          coins = 0
          description = f"You are high because you actually participated in an international competition and it is obvious that you did not win. However you did well but it cost you {coin_fee} coins and you did not get any more coins."
        elif coin_chance > 0.875 and coin_chance <= 0.993:
          coins = 0
          description = f"You are high because you actually participated in an international competition and obviously got a bad position. However, you got so triggered you broke your laptop AHAHAHAHAHA"
          amounts[uid]['laptop'] -= 1
        elif coin_chance > 0.993 and coin_chance <= 0.9985:
          coins = coin_fee + random.randrange(50000, 100000, 500)
          description = f"You are really high because you actually participated in an international competition and YOU WERE LIKE SO SKILLED SOMEHOW I DON'T KNOW HOW BUT SO SKILLED THAT YOU ENDED UP GETTING THIRD PLACE :open_mouth: Therefore, you were able to go home with {coins} coins and also the fee was {coin_fee} coins to participate in this so NICE."
        elif coin_chance > 0.9985 and coin_chance <= 0.99999999:
          coins = coin_fee + random.randrange(250000, 750000, 500)
          description = f"You are hyper because you actually participated in an international competition and HOW DID YOU GET SO GOOD I MEAN LIKE YOU ARE COMPETEING AGAINST PEOPLE ALL OVER THE WORLD LIKE YOU GOT SO GOOD I CAN'T BELIEVE THERE'S NO WAY YOU COULD HAVE POSSIBLY GOTTEN 2nd PLACE I MEAN LIKE I DON'T KNOW HOW YOU DID THAT AND I AM SO SURPRISED THAT I AM NOT RAMBLING...Anyways, that international competition cost {coin_fee} coins but you ended up going home with {coins} coins so uh NICE."
        else:
          coins = coin_fee + random.randrange(1000000, 10000000, 1000)
          description = f"You are very very hyper cause you participated in an international competition and I mean like HOW IS THIS EVEN POSSIBLE WHAT RANK YOU GOT I MEAN LIKE HOW DID YOU DO THIS YOU END UP WALKING INTO AN INTERNATIONAL COMPETITION AGAINST THE WHOLE WORLD AND ENDED UP GETTING THIS CRAZY RANKING AND NOW I AM GOING SO MAD THAT I AM GOING TO IAWHPFIOHWVBOIBHOIQHWAPOIHOIPWHBOIHOIhwHIOUGIUGIOYFUYTDTDYIUHPOIUGYFHGKIUFGHUYGIOUYFGHIOUYTDFGUIHYOUFTDFGUIHOYUTFGUIHOYUFGUIHOYUFGUHIOUYGFDTGFIUHOYUGFGIHOYUGFUGHYGFYUGHIOYTUFGIHOGUFYGHIGUVHIGUFYVHIOJUGYFGIHOUGFYVHGIOGUFYVHIOGUYFGIH...YEAH I KNOW THAT IS RANDOM BUT I MEAN LIKE I STILL DON'T HOW YOU WERE ABLE TO ACCOMPLISH WHAT YOU DID... anyways, in simple terms, you got 1st place by walking into an international competition that cost {coin_fee} coins and now you won the grand prize of {coins} coins."
        coins -= coin_fee
      amounts[uid]['coins'] += coins
      amounts[uid]['bank-space'] += random.randint(1, 50)
      amounts[uid]['commands'] += 1
      await ctx.send(embed=discord.Embed(title = "You participated in a hackathon!", description = description, color = discord.Colour.green()))
      _save()
    else:
      await ctx.send("You need **5 laptop** to participate in a hackathon. What do you think you are going to use, a mobile device that doesn't store a lot of data?")
  except KeyError:
    await ctx.send("You need **5 laptop** to participate in a hackathon. What do you think you are going to use, a mobile device that doesn't store a lot of data?")

@client.command()
@commands.cooldown(1, 45, commands.BucketType.user)
async def stream(ctx):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  try:
    if amounts[uid]['laptop'] >= 3:
      coin_chance = random.random()
      if coin_chance <= 0.65:
        views = random.randint(10000, 100000)
        likes = random.randint(2000, 5000)
        coins = random.randint(50, 1000)
        description = f"You streamed a video and posted it. In the end, you got {views} views and {likes} likes. You also got {coins} coins from your fans."
      elif coin_chance > 0.65 and coin_chance <= 0.85:
        views = random.randint(5000, 20000)
        dislikes = random.randint(1000, 2500)
        coins = 0
        description = f"You streamed a video and posted it. Unfortunately, your video was trash because you ended up getting only {views} views and {dislikes} dislikes. Therefore, you got no coins from your fans."
      elif coin_chance > 0.85 and coin_chance <= 0.91:
        views = random.randint(5000, 50000)
        dislikes = random.randint(2500, 4900)
        coins = 0
        description = f"You streamed a video and posted it. Unfortunately, the video was so bad that you got {views} views and {dislikes} dislikes. Your fans were so mad that they staged a raid and stole your laptop!"
        amounts[uid]['laptop'] -= 1
      elif coin_chance > 0.91 and coin_chance <= 0.92:
        views = random.randint(5000, 10000)
        coins = 0
        description = f"You streamed a video and posted it. Unfortunately, your video was like the worst ever since you got {views} views and all of them gave you dislikes. Your fans were so triggered by how bad the video was that they ended up raiding your house and stole all of your laptops you were using to post your videos!"
        amounts[uid]['laptop'] -= 3
      elif coin_chance > 0.92 and coin_chance <= 0.9993:
        views = random.randint(100000, 1000000)
        likes = random.randint(50000, 90000)
        coins = random.randint(2500, 5500)
        description = f"You streamed a video and posted it. A lot of people liked your video and it came in trending. After the popularity of the video died down, you got {views} views in total and the likes were at {likes}. So many of your fans liked it that in total you got {coins} coins."
      else:
        views = random.randint(5000000, 1000000000)
        likes = random.randint(500000, 3550000)
        coins = random.randint(3000, 7000)
        bonus_coins = random.randint(3000, 5000)
        description = f"You streamed a video and posted it. Everyone liked it and watched the video like a hundred times or something. Anyways, it took a while for the popularity to die down and when it did, you had {views} views and {likes} likes. At first, you had {coins} coins from your fans but one of them was so impressed that they gave you an extra {bonus_coins} coins."
        coins += bonus_coins
      amounts[uid]['coins'] += coins
      amounts[uid]['bank-space'] += random.randint(1, 50)
      amounts[uid]['commands'] += 1
      if coins == 0:
        color = discord.Colour.orange()
      else:
        color = discord.Colour.green()
      await ctx.send(embed = discord.Embed(title = "You streamed a video and posted it!", description = description, color = color))
      _save()
    else:
      await ctx.send("You need **2 laptops** for some reason to stream a video.")
  except KeyError:
    await ctx.send("You need a **2 laptops** for some reason to stream a video.")

@client.command(aliases=['post_coding_thing'])
@commands.cooldown(1, 40, commands.BucketType.user)
async def pcp(ctx):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  try:
    if amounts[uid]['laptop'] >= 1:
      coin_possible = random.random()
      if coin_possible <= 0.575:
        coins = random.randint(10, 500)
        upvotes = random.randint(1, 500)
        choices_of_post = ["game", "mini-game", "simulator"]
        description = f"You ended up posting a {random.choice(choices_of_post)}. Luckily, you were able to get {upvotes} upvotes and you got {coins} coins from your fans!"
      elif coin_possible > 0.575 and coin_possible <= 0.95:
        coins = 0
        downvotes = random.randint(1, 500)
        choices_of_post = ["game", "mini-game", "simulator", "an old project you found"]
        description = f"You ended up posting a {random.choice(choices_of_post)}. Unfortunately, no one liked your post so you got {downvotes} downvotes and therefore no one gave you any coins."
      elif coin_possible > 0.95 and coin_possible <= 0.9675:
        coins = 0
        downvotes = random.randint(1000, 5000)
        choices_of_post = ["begginer's concept", "project with lots of mistakes", "a hacker game"]
        description = f"You ended up posting a {random.choice(choices_of_post)}. Everyone hated your post so much because you got {downvotes} downvotes and all your fans staged a raid on you and took your laptop LMAO."
        amounts[uid]['laptop'] -= 1
      elif coin_possible > 0.9675 and coin_possible <= 0.9997:
        coins = random.randint(150, 300)
        bonus_coins = random.randint(500, 1000)
        upvotes = random.randint(1000, 6000)
        choices_of_post = ["epic game", "cool simulator", "cool project"]
        description = f"You ended up posting a {random.choice(choices_of_post)}. A lot of people liked the post a lot so you got {upvotes} upvotes and gave you {coins} coins. One of your fans were so proud of you that the person gave you an extra {bonus_coins} coins!"
        coins += bonus_coins
      else:
        coins = random.randint(750, 1111)
        upvotes = random.randint(10000, 100000)
        bonus_coins = random.randint(2000, 4000)
        description = f"You ended up posting a surreal project. You got so many upvotes ({upvotes} of them) and your project got featured for weeks in a magazine called Best Coding Projects of the Week. You got {coins} coins at first and then one fan was so impressed that the person gave you {bonus_coins} more coins!"
        coins += bonus_coins
      amounts[uid]['coins'] += coins
      if coins == 0:
        color = discord.Colour.orange()
      else:
        color = discord.Colour.green()
      await ctx.send(embed = discord.Embed(title = "You posted a coding project!", description = description, color = color))
      amounts[uid]['bank-space'] += random.randint(1, 50)
      amounts[uid]['commands'] += 1
      _save()
    else:
      await ctx.send("You need a **laptop** in order to post some coding projects or things.")
  except KeyError:
    await ctx.send("You need a **laptop** in order to post some coding projects or things.")

@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def fish(ctx):
  fish_rarity = random.random()
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  try:
    if amounts[uid]['fishingpole'] >= 1:
      if fish_rarity <= 0.6:
        type_fish = ["trout", "mackeral"]
        fishes = random.randint(1, 10)
        fish = random.choice(type_fish)
        description = f"You were able to catch {fishes} {fish}s."
      elif fish_rarity > 0.6 and fish_rarity <= 0.92:
        fishes = 0
        fish = "none"
        description = "You are such a noob that you did not catch anything during this fishing time."
      elif fish_rarity > 0.92 and fish_rarity <= 0.94:
        fishes = 0
        fish = "none"
        description = "AHAHAHAHA you broke your fishingpole."
        amounts[uid]['fishingpole'] -= 1
      elif fish_rarity > 0.94 and fish_rarity <= 0.975:
        list_of_items = ["shoe", "cube", "fishingpole"]
        fish = random.choice(list_of_items)
        fishes = 1
        description = f"Nice, you got a {fish}."
      elif fish_rarity > 0.975 and fish_rarity <= 0.995:
        list_of_fish = ["jellyfish", "octopus"]
        fishes = random.randint(1, 3)
        fish = random.choice(list_of_fish)
        description = f"Wow, you got lucky because you were able to catch {fishes} {fish}s."
      elif fish_rarity > 0.995 and fish_rarity <= 0.9995:
        list_of_fish = ["whale", "shark"]
        fishes = random.randint(1, 2)
        fish = random.choice(list_of_fish)
        description = f"Dang you just got so lucky today. You were able to catch {fishes} {fish}s."
      else:
        fish = "coinfish"
        fishes = 1
        description = f"HOW DID YOU DO THIS BECAUSE THIS IS LITERALLY IMPOSSIBLE! (Not really but still) You somehow caught a COIN FISH! You are literally such a pro at fishing!"
      if fish != "None":
        try:
          amounts[uid][fish] += fishes
        except KeyError:
          amounts[uid][fish] = 0
          _save()
          amounts[uid][fish] += fishes
      if fishes >= 1:
        color = discord.Colour.green()
      else:
        color = discord.Colour.red()
      await ctx.send(embed = discord.Embed(title = "You fished", description = description, color = color))
      amounts[uid]['bank-space'] += random.randint(1, 50)
      amounts[uid]['commands'] += 1
      _save()
    else:
      await ctx.send("You need a **Fishing Pole** in order to fish. You can't just fish using your hands.")
  except KeyError:
    await ctx.send("You need a **Fishing Pole** in order to fish. You can't just fish using your hands.")

""""""

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def hunt(ctx):
  hunt_rarity = random.random()
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  try:
    if amounts[uid]['rifle'] >= 1:
      if hunt_rarity <= 0.6:
        type_hunt = ["duck", "bunny"]
        hunted = random.randint(1, 10)
        hunt = random.choice(type_hunt)
        description = f"You were able to hunt {hunted} {hunt}s."
      elif hunt_rarity > 0.6 and hunt_rarity <= 0.92:
        hunted = 0
        hunted = "none"
        description = "You are such a noob that you did not hunt anything during this hunting time."
      elif hunt_rarity > 0.92 and hunt_rarity <= 0.94:
        hunted = 0
        hunt = "none"
        description = "AHAHAHAHA you broke your rifle."
        amounts[uid]['rifle'] -= 1
      elif hunt_rarity > 0.94 and hunt_rarity <= 0.975:
        list_of_items = ["deer", "squirrel", "rifle"]
        hunt = random.choice(list_of_items)
        hunted = 1
        description = f"Nice, you got a {hunt}, good job."
      elif hunt_rarity > 0.975 and hunt_rarity <= 0.995:
        list_of_hunt = ["elephant", "bird"]
        hunted = random.randint(1, 3)
        hunt = random.choice(list_of_hunt)
        description = f"Wow, you are a bit lucky because you were able to hunt {hunted} {hunt}s."
      elif hunt_rarity > 0.995 and hunt_rarity <= 0.9995:
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

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    donators = ["Bob", "Rock", "Fabian", "a person", "your ego", "the world", 'putera', "Jeff", "Joe", "the other begger", "the 10 IQ person", "god", "everyone", "a gamer", "your friend", "ewk's missing dad", "putera's only friend", "jeff bezos", "Elon musk", "yoda", "muhi", "**__*bob's sugar daddies*__**", "billy willy", "a police man", "a police cat", "**the letter p**", "Fabian's missing irn bru can", "Rocks's missing rock", "pebble", "bills roblox account", "ikea", "lilwilli", "dwayne the rockwicha johnson", "dank memer", "santa", "**the letter e**", "James", "MrBeast", "**the letter s**", "a doughnut", "FORTNITE BATTLE PASS", "dad that works at epic games", "**the letter n**", "bob's drinking problems", "fabian's chicken", "a farmer", "**the letter i**", "pepe", "Roblox CEO", "a rich person", "rocks rock", "not rocks rock", "bobs nuggie", "not bobs nuggie", "pierogi", "not your dad", ]
    messages = ["go away", "be quiet", "stop begging your life is not going to change", "shut up and stop begging", "no you", "wait I have some money...oh nvm I don't", "you are too rich right now go away", "beggers are people who have low IQ", "The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.", "WEE WOO WEE WOO", "oops i dropped my money, give that back bozo", "sorry, i need to buy some irn bru with this", "i need this money to buy bob some nuggies", "balls", "do you like bill? i will guess that you dont", "get the frick out of my face im playing minecraft", "you smell like cheese", "i like maltesers", "touch grass is not an insult towards gamers, rather it is advice for them. When participating in intense periods of gaming, the human hand has a tendency to get sweaty. The sweat causes the hand to become slick, and it b becomes more difficult to retain a grip on the gamers gaming mouse, thus making it more difficult to perform well in intense gaming moments. By touching grass with the gamers hand, the grass will impart a layer of particulate onto the gamers hand, the particulate can be made of a variety of dusts, dirts and other natural matter. This particulate will then act in a similar form to climbers chalk, absorbing the sweat and drying out the gamers hand. With dry hands, the gamer can now perform to their maximum when gaming. This is why when an enemy or teammate tells you to touch grass, they are simply trying to assist you in performing better.", "bye", "bill is a roblox pro", "i hate you", "get a job", "ha, poor", "get good", "no", "you are so ugly you make me sick", "imagine being poor", "call the police its a poor person", "can you help me find my dad?", "i love bees", "bob is so cool", "go play fortnite", "you are so poor you cant even afford a freddo", "here have a coin... joking, give that back"] 
    uid = str(ctx.author.id)
    if not uid in amounts:
        amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
    if random.random()<=0.5:
        profit = random.randint(15, 120)
        await ctx.send(embed = discord.Embed(title=f"{ctx.author.name} begged and a person gave the user some coins!", description=f'You got {profit} coins from {random.choice(donators)}.', color = discord.Colour.green()))
    else:
        profit = 0
        await ctx.send(embed = discord.Embed(title=f'Oof! No one gave {ctx.author.name} any coins!', description=f'{random.choice(donators)} told you {random.choice(messages)}.', colour = discord.Colour.red()))
    amounts[uid]['coins'] += profit
    amounts[uid]['bank-space'] += random.randint(1, 50)
    amounts[uid]['commands'] += 1
    _save()

@client.command()
@commands.cooldown(1, 45, commands.BucketType.user)
async def search(ctx):
    places = ["fireplace", "couch", "bedroom", "car", "living room", "sewer", "office", "park"]
    places_chosen = []
    uid = str(ctx.author.id)
    if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
    for i in range(5):
      random_place = random.randint(0, (len(places) - 1))
      places_chosen.append(places[random_place])
      del places[random_place]
    message = await ctx.send(embed=discord.Embed(title=f"{ctx.author.name}\'s Search", description=f"Here are your choices to for where you can search for coins:\n``{places_chosen[0]}`` |  ``{places_chosen[1]}`` |  ``{places_chosen[2]}`` |  ``{places_chosen[3]}`` |  ``{places_chosen[4]}``", color = discord.Colour.blue()))
    try:
      def check(msg):
        return msg.author.id == int(uid)
      msg = await client.wait_for("message", timeout=10, check=check)
      message_content = msg.content
      search_correct = False
      for i in range(len(places_chosen)):
        if message_content.lower() == places_chosen[i]:
          search_correct = True
      if search_correct == True and message_content.lower() == "fireplace":
        chance_of_coins = random.random()
        if chance_of_coins <= 0.1:
          coins = random.randint(1000, 1500)
          embed = discord.Embed(title="You searched the fireplace and got coins!", description=f"You were extremely lucky that you didn't burn. You were also lucky to find coins that were not burned. Also what crazy person would leave their coins in a fireplace? Anyways, you found {coins} of unburned coins.", color = discord.Colour.green())
        elif chance_of_coins > 0.1 and chance_of_coins <= 0.3:
          coins = 0
          embed = discord.Embed(title="You searched the fireplace and didn't get any coins!", description="You were extremely lucky that you didn't burn. Unfortunately, there was no use to going in because there were no coins in the fireplace. It looks like either no one left coins in the fireplace or someone used the fireplace and burned them all up.", color = discord.Colour.orange())
        elif chance_of_coins > 0.4 and chance_of_coins <= 0.65:
          coins = random.randint(-500, -50)
          embed = discord.Embed(title="You searched the fireplace but got some burns.", description=f"You went into the fireplace but unfortunately it was at the wrong time. You were so into getting coins that you didn't realize the fireplace was burning. Therefore, you ended up getting burned for a little bit before you realized and went out. Luckily, it was an open fireplace. However, you still had to go to the hospital and pay them {coins * -1} coins.", color = discord.Colour.red())
        elif chance_of_coins > 0.65 and chance_of_coins <= 0.99:
          coins = random.randint(-5000, -1000)
          embed = discord.Embed(title="You searched the fireplace and got major burns.", description=f"You went into the fireplace while there was a fire in there. You were so into getting coins that you didn't realize this. For some reason, you were also so obsessed with getting coins that you never realized and someone had to pull you out. You had to go to the hospital to get those treated and had to pay then {coins * -1} coins.", color = discord.Colour.red())
        else:
          coins = amounts[uid]['coins'] * -1
          embed = discord.Embed(title="You searched the fireplace and died.", description=f"In order to get to the firepalce, you had to climb the chimney in order to get down and start searching. However, when you went down the chimney and into the fireplace, you suddenly realized that something was burning inside. You tried to get out but there was no use. You died in the fireplace and also lost all your coins.")
          amounts[uid]['bank-coins'] = 0
          amounts[uid]['bank-space'] = 0
      elif search_correct == True and message_content.lower() == "couch":
        coins = random.randint(5, 200)
        embed = discord.Embed(title="You searched the couch.", description=f"You searched the couch and for some reason you found {coins} coins. What does this person think a couch is, a bank?", color = discord.Colour.green())
      elif search_correct == True and message_content.lower() == "bedroom":
        chance_of_more_coins = random.random()
        if chance_of_more_coins <= 0.999:
          coins = random.randint(1, 500)
          embed = discord.Embed(title="You searched the bedroom.", description=f"You searched your bedroom and you still had some leftover allowance that you never used and put in your wallet. In addition, you also found some coins scattered on the floor. Those coins made you get {coins} coins.", color = discord.Colour.green())
        else:
          coins = random.randint(1000, 5000)
          embed = discord.Embed(title="You searched the bedroom and got very lucky! :money_mouth: :open_mouth:", description=f"You searched your bedroom and found some leftover allowance you never put in your wallet and some coins that were scattered. However, when you looked under your bed, you suddenly saw a bedroom demon under there. That bedroom demon was kind of rich and gave you most of their coins. After that you ended up with {coins} more coins to add to your wallet.", color = discord.Colour.green())
      elif search_correct == True and message_content.lower() == "car":
        chance_of_coins = random.random()
        if chance_of_coins <= 0.35:
          coins = random.randint(1, 1000)
          embed = discord.Embed(title="You searched a car and succeeded! :open_mouth:", description=f"Since you didn\'t own a car, you had to go steal coins from one. You got lucky because no one caught you. Therefore, you were able to run away with {coins} coins.", color = discord.Colour.green())
        else:
          coins = random.randint(-2000, -50)
          embed = discord.Embed(title="You searched a car but failed!", description=f"Since you didn\'t own a car, you had to go steal coins from one. Unfortunately, someone saw you while you were trying to rob the person\'s money in the car. That person phoned the police so while you were running away, the police were able to get you. You unfortunately had to pay {coins * -1} coins in fines.", color = discord.Colour.red())
      elif search_correct == True and message_content.lower() == "living room":
        coins = random.randint(10, 350)
        embed = discord.Embed(title="You searched the living room!", description=f"You searched the living room and found {coins} coins. I wonder why a person would drop it...", color = discord.Colour.green())
      elif search_correct == True and message_content.lower() == "sewer":
        chance_of_more_coins = random.random()
        if chance_of_more_coins <= 0.9:
          coins = random.randint(25, 500)
          embed = discord.Embed(title="You searched the sewer and got coins!", description=f"You searched the sewer and found {coins} coins. I wonder why coins would be in the sewer and why you would go in there.", color = discord.Colour.green())
        else:
          earn_coins = random.randint(400, 420)
          lose_coins = random.randint(280, 400)
          coins = earn_coins - lose_coins
          embed = discord.Embed(title="You searched the sewer, found coins, and lost some.", description=f"You searched the sewer and got {earn_coins} coins! However, while going in the dirty water, you suddenly lost your balance and fell. You were able to get back up, but you lost {lose_coins} of your coins (because you were still carrying them). However, you ended up getting out of the sewer with {coins} more coins.", color = discord.Colour.orange())
      elif search_correct == True and message_content.lower() == "office":
        coins = random.randint(10, 250)
        embed = discord.Embed(title="You searched the office!", description=f"You searched **an** office and got {coins} coins. Since you saw that the **an** was bold, I wonder if this office was yours (as in workspace for school or something) or your parents...", color = discord.Colour.green())
      elif search_correct == True and message_content.lower() == "park":
        coins = random.randint(5, 300)
        embed = discord.Embed(title="You searched the park!", description = f"You searched the park and was able to gather {coins} coins that were on the ground. Looks like you were trying to save the environment (while being greedy and getting more coins).", color = discord.Colour.green())
      else:
        await message.edit(content="That is not an option.")
      if amounts[uid]['coins'] + coins >= 0:
        amounts[uid]['coins'] += coins
      else:
        amounts[uid]['coins'] = 0
      amounts[uid]['bank-space'] += random.randint(1, 50)
      amounts[uid]['commands'] += 1
      await ctx.send(embed=embed)
      _save()
    except asyncio.TimeoutError:
      await message.edit(content="Are you ok? You can\'t just not respond after typing in ``c search``")

@client.command(aliases=['deposit'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def dep(ctx, amount):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  if amount == "all":
    if amounts[uid]['bank-space'] - amounts[uid]['bank-coins'] >= amounts[uid]['coins']:
      coins = amounts[uid]['coins']
      amounts[uid]['bank-coins'] += amounts[uid]['coins']
      amounts[uid]['coins'] = 0
    else:
      coins = amounts[uid]['bank-space'] - amounts[uid]['bank-coins']
      amounts[uid]['bank-coins'] += coins
      amounts[uid]['coins'] -= coins
    embed = discord.Embed(title = f"{ctx.author.name} deposited coins!", description = f"You deposited {coins} coins to your bank!", color = discord.Color.green())
  elif amount.isdigit():
    coins = amount
    if int(amounts[uid]['bank-space']) - int(amounts[uid]['bank-coins']) >= int(amount):
      amounts[uid]['bank-coins'] += int(amount)
      amounts[uid]['coins'] -= int(coins)
      embed = discord.Embed(title = f"{ctx.author.name} deposited coins!", description = f"You deposited {coins} coins to your bank!", color = discord.Color.green())
    else:
      embed = discord.Embed(title = f"Are you ok?", description = f"Are you actually ok? Because you literally don't have that many coins in your wallet to deposit into your bank.", color = discord.Color.orange())
  else:
    embed = discord.Embed(title = "What?", description = "I have no clue what you put but let me just tell you after you write ``c dep`` that you have to put in an integer or the word all if you want to fill up the whole bank.", color = discord.Colour.orange())
  amounts[uid]['commands'] += 1
  await ctx.send(embed=embed)
  _save()

@client.command(aliases=['with'])
async def withdraw(ctx, amount):
  uid = str(ctx.author.id)
  if not uid in amounts:
      amounts[uid] = {'coins': 0, 'bank-coins': 0, 'bank-space': 0, 'commands': 0, 'dailytime': 0, 'job': "None", 'alcohol_use': False, 'alcohol_times': 0, 'padlock_use': False}
  if amount == "all":
    coins = amounts[uid]['bank-coins']
    amounts[uid]['bank-coins'] = 0
    amounts[uid]['coins'] += coins
    embed = discord.Embed(title = f"{ctx.author.name} withdrawed coins!", description = f"You withdrawed {coins} coins from the bank and now those coins are in your wallet.", color = discord.Colour.green())
  elif amount.isdigit():
    if int(amount) <= int(amounts[uid]['bank-coins']):
      amounts[uid]['bank-coins'] -= int(amount)
      amounts[uid]['coins'] += int(amount)
      embed = discord.Embed(title = f"{ctx.author.name} withdrawed coins!", description = f"You with drawed {amount} coins from the bank and now those coins are in your wallet.", color = discord.Colour.green())
    else:
      await ctx.send("Um you don't have that much money in your bank.")
  else:
    await ctx.send("Stupid you need to respond with ``c with all`` or ``c with`` and then an integer that has to be less than how many bank coins you have.")
  amounts[uid]['commands'] += 1
  await ctx.send(embed = embed)
  _save()

@client.command()
@commands.has_any_role()
async def ban(ctx, user:discord.Member="None",*, reason = "No reason provided."):
  ban = True
  if user == "None" or user == ctx.message.author or user.bot == True:
    embed = discord.Embed(title = "You unsuccessfully banned.", description = "I wonder why...oh yeah its because you need to put in a member and not just yourself so don't be so stupid. It also could have been because you put the name of a bot.", color = discord.Colour.orange())
    ban = False
  if ban == True:
    embed = discord.Embed(title = "You successfully banned.", description = f"{user.mention} was banned.", color = discord.Colour.green())
    embed1 = discord.Embed(title = "You were banned.", description = f"Reason: {reason}", color = discord.Colour.red())
    await user.send(embed = embed1)
    await user.ban(reason=reason)
  await ctx.send(embed = embed)

@client.command()
@commands.has_any_role()
async def unban(ctx, *, member):
  BanList = await ctx.guild.bans()
  MemberDiscrim = member.split('#')
  MemberName = member.split('#' + MemberDiscrim[0])
  user_found = False
  for BanEntry in BanList:
    user = BanEntry.user
    if (MemberName[0]) == (user.name): 
      await ctx.guild.unban(user)
      await ctx.send(embed = discord.Embed(title = "You successfully unbanned!", description = f'{user.mention} has been unbanned by {ctx.author.name}', color = discord.Colour.green()))
      user_found = True
      break
  if user_found == False:
    await ctx.send(embed = discord.Embed(title = "User not found", description = "The user was either probably not banned or is not in this server", color = discord.Colour.orange()))

@client.command()
@commands.has_any_role("The Bot Owner", "Moderator", "Owner", "Administrator")

#errors ----

@beg.error
async def beg_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed = discord.Embed(title="Just Stop Begging", description=(f'Begging more won\'t do anything for you. Use this command again after {round(error.retry_after)} seconds.'), color = discord.Colour.orange()))
    else:
      raise error 

@search.error
async def search_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed = discord.Embed(title="Why are you searching so much?", description=f"Don't search around too much you might tire youself. Wait {round(error.retry_after)} seconds before using this command again.", color = discord.Colour.orange()))
    else:
      raise error

@dep.error
async def dep(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed = discord.Embed(title="Cooldown Active", description=f"Why are you going to the bank so much? Wait {round(error.retry_after)} seconds before using this command again.", color = discord.Colour.orange()))
    else:
      raise error

@fish.error
async def fish(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed = discord.Embed(title="Why are you fishing so much?", description=f"If you fish this much, there won't be any fishes to fish from later. Wait {round(error.retry_after)} seconds before using this command again.", color = discord.Colour.orange()))
    else:
      raise error

@hunt.error
async def hunt(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed = discord.Embed(title="Why are you hunting so much?", description=f"If you hunt this much, there won't be any animals to kill from later. Wait {round(error.retry_after)} seconds before using this command again.", color = discord.Colour.orange()))
    else:
      raise error

@pcp.error
async def pcp(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed = discord.Embed(title="Why you post?", description=f"It takes time to code a good project. Wait {round(error.retry_after)} seconds before using this command again.", color = discord.Colour.orange()))
    else:
      raise error

@stream.error
async def stream(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed = discord.Embed(title="Why you post video?", description=f"It takes time to make good videos that people would like. Wait {round(error.retry_after)} seconds before using this command again.", color = discord.Colour.orange()))
    else:
      raise error

@hackathon.error
async def hackathon_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed = discord.Embed(title="Cooldown Active", description=f"There aren't any hackathons that you can go participate in right now. Wait {round(error.retry_after)} seconds before participating in another one.", color = discord.Colour.orange()))
    else:
      raise error

@betbot.error
async def betbot_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("You need to **specify** the amount ok? You can't just put no number that you will bet on.")
  elif isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed = discord.Embed(title="Cooldown Active", description=f"If you bet that much, you will be poor in a matter of minutes! Wait {round(error.retry_after)} seconds before using this command again.", color = discord.Colour.orange()))
  else:
    raise error

@betplayer.error
async def betplayer_error(ctx, error):
    minutes = math.floor(round(error.retry_after)/60)
    seconds = round(error.retry_after) - minutes * 60
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed = discord.Embed(title="Cooldown Active", description=f"If you bet this much, you will literally be poor. Wait {minutes} minutes and {seconds} seconds betting with another player.", color = discord.Colour.orange()))
    else:
      raise error

@rob.error
async def rob_error(ctx, error): 
    if isinstance(error, commands.BadArgument):
      await ctx.send("Bruh, I don't know what you put but the member was not found.")
    elif isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed = discord.Embed(title="Cooldown Active", description=f"If you rob too many times, you or the person who you are trying will be poor! Wait {round(error.retry_after)} seconds using this command again.", color = discord.Colour.orange()))
    else:
      raise error

@stats.error
async def stats_error(ctx, error):
  if isinstance(error, commands.BadArgument):
    await ctx.send(embed=discord.Embed(title="Excuse me, who?", description="Like what the title says wait who are you talking about?", color = discord.Colour.orange()))
  else:
    raise error

@balance.error
async def balance_error(ctx, error):
  if isinstance(error, commands.BadArgument):
    await ctx.send(embed=discord.Embed(title="Excuse me, who?", description="Like what the title says wait who are you talking about?", color = discord.Colour.orange()))
  else:
    raise error

@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.MissingAnyRole):
    await ctx.send(embed=discord.Embed(title="This command doesnt exist you bozo", description = "nice try", color = discord.Colour.red()))
  else:
    raise error

@unban.error
async def unban_error(ctx, error):
  if isinstance(error, commands.MissingAnyRole):
    await ctx.send(embed=discord.Embed(title="This command doesnt exist you bozo", description = "nice try", color = discord.Colour.red()))
  else:
    raise error
  
def _save():
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f) 

keep_alive()
client.run(os.environ['TOKEN'])