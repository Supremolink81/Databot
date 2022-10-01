from discord.ext import commands
from builtins import bot
from categorical.categorical_functions import *
from generic.generic_functions import *

@bot.command(pass_context = True)
async def a_c_d(ctx, *args):
    if len(args) == 0: lst = await data_list_categorical(ctx)
    else: lst = args
    await analyze_categorical_data(lst, ctx)

@bot.command(pass_context = True)
async def p_c_d(ctx, *args):
    if len(args) == 0: lst = await data_list_categorical(ctx)
    else: lst = args
    await plot_categorical_data(lst, ctx)

@bot.command(pass_context = True)
async def a_c_file(ctx):
    try:
        df = make_df_file(ctx)
        await ctx.send("Enter the column to analyze:")
        column_name = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        ser = df[column_name.content].squeeze()
        await analyze_categorical_data(ser.tolist(), ctx)
    except RuntimeError:
        await ctx.send("Invalid input! A csv or xsls file must be attached.")
    except asyncio.TimeoutError:
        await ctx.send("Sorry, you took too long to give an input!")
    except KeyError: 
        await ctx.send("Invalid column name entered!")