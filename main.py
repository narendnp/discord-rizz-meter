import discord
from discord.ext import commands
import random
import asyncio
import logging
import datetime
import pytz
import functools
import time
import json
import os

with open('config.json') as f:
    setup_data = json.load(f)

GUILD_ID = int(setup_data['GUILD_ID']) or int(os.getenv('GUILD_ID'))
TIMEOUT_ROLE_ID = int(setup_data['TIMEOUT_ROLE_ID']) or int(os.getenv('TIMEOUT_ROLE_ID'))
BOT_TOKEN = setup_data['BOT_TOKEN'] or os.getenv('BOT_TOKEN')
timezone = pytz.timezone(setup_data['timezone'] or os.getenv('timezone') or 'Asia/Jakarta') # Defaults to Asia/Jakarta
treshold = int(setup_data['rizz_threshold']) or int(os.getenv('rizz_threshold')) or 90 # Defaults to 90

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False
intents.members = False
intents.reactions = False
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)
timeout_users = {}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Running on server: {bot.get_guild(GUILD_ID).name}')
    print(f'Timezone is set to: {timezone}')
    print(f'Rizz value treshold: {treshold}%')
    print(f'Bot is ready and running!')

def cooldown(func):
    last_called = 0
    @functools.wraps(func)
    async def wrapper(ctx, *args, **kwargs):
        nonlocal last_called
        if time.time() - last_called < 30:
            await ctx.reply("You're too fast homie, wait 30 seconds before using !rizz again.")
            logging.info(f'{ctx.author.name} tried to use !rizz too quickly')
            return
        last_called = time.time() # Update the last called time to now
        return await func(ctx, *args, **kwargs)
    return wrapper

@bot.command(name='rizz')
@cooldown
async def rizz(ctx):
    logging.info(f'!rizz command invoked by {ctx.author.name} in {ctx.channel.name} at {ctx.message.created_at.astimezone(timezone).strftime("%Y-%m-%d %H:%M:%S %Z")}')
    
    roll = random.randint(0, 100)
    logging.info(f'!rizz result: {roll}%')
    
    if roll >= (treshold):
        await ctx.reply(f'<@{ctx.author.id}> has overflowing {roll}% rizz! They now gain the ability to !timeout a user (for a limited time).')
        logging.info(f'{ctx.author.name} got >{treshold}% rizz and can use !timeout')
        
        timeout_users[ctx.author.id] = True
    
        # Check if the user has the timeout ability and wants to timeout another user
        def check_timeout(message):
            return message.author == ctx.author and message.content.startswith('!timeout')
        
        # Wait for the user to send a !timeout command
        try:
            timeout_message = await bot.wait_for('message', check=check_timeout, timeout=30)
        except asyncio.TimeoutError:
            pass
    else:
        await ctx.reply(f'<@{ctx.author.id}> has {roll}% rizz.')
            

@bot.command(name='timeout')
async def timeout(ctx, user: commands.UserConverter):
    mentioned_user = user
    # Check if the user is trying to use the !timeout command within 30 seconds of gaining the ability
    if ctx.author.id in timeout_users:
        timeout_ability_timestamp = timeout_users[ctx.author.id]
        if isinstance(timeout_ability_timestamp, bool):
            # If timeout_ability_timestamp is a boolean, set it to the current datetime
            timeout_users[ctx.author.id] = datetime.datetime.now()
            timeout_ability_timestamp = timeout_users[ctx.author.id]
        if (datetime.datetime.now() - timeout_ability_timestamp).total_seconds() <= 30:
            # Grant the mentioned user the timeout role
            timeout_role = bot.get_guild(GUILD_ID).get_role(TIMEOUT_ROLE_ID)
            await mentioned_user.add_roles(timeout_role)
            await ctx.reply(f'<@!{ctx.author.id}> used !timeout on <@!{mentioned_user.id}>.')
            logging.info(f'{ctx.author.name} used !timeout on {mentioned_user.name}')
            # Remove the timeout role after 30 seconds
            await asyncio.sleep(30)
            await mentioned_user.remove_roles(timeout_role)
            logging.info(f'{mentioned_user.name} has been removed from the timeout role')

bot.run(BOT_TOKEN)