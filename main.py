from discord.ext import commands
import builtins
import sys

bot = commands.Bot("/", case_insensitive = True)
builtins.bot = bot
sys.path.append('C:\\Users\\arioz\\OneDrive\\Documents\\Programming\\Python\\Databot')

#Command Imports
import quantitative.quantitative_commands
import categorical.categorical_commands
import generic.generic_commands
import combinatorics.combinatorics_commands
import binomial.binomial_commands

#Events
@bot.event
async def on_ready():
    print(f"Logged in as {bot}")
            
bot.run("OTc4ODI1MTY1MDgzMzgxNzYw.G0TEW5.ZYy0nU4kaDq3448q1bCJruR2IMQC1E0mx4DRiU")