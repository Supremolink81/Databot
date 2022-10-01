from socket import INADDR_MAX_LOCAL_GROUP
from discord.ext import commands
from builtins import bot
import discord
import matplotlib.pyplot as plt
from generic.generic_functions import *

@bot.command(pass_context = True)
async def command_guide(ctx):
    await ctx.send(HELP())

@bot.command(pass_context = True)
async def scaly(ctx):
    with open("scaly.png", "rb") as img:
        pic = discord.File(img)
        await ctx.send(file = img)

@bot.command(pass_context = True)
async def clear_plot(ctx):
    plt.clf()