from discord.ext import commands
from builtins import bot
from categorical.categorical_functions import *
from generic.generic_functions import *

@bot.command(pass_context = True)
async def a_c_d(ctx, *args):
    """
    Takes in a list of one-variable categorical data from a message,
    then sends summary statistics (unique values, most common
    value) to the server given by the Context object.
    """
    if len(args) == 0: lst = await data_list_categorical(ctx)
    else: lst = args
    await analyze_categorical_data(lst, ctx)

@bot.command(pass_context = True)
async def p_c_d(ctx, *args):
    """
    Takes in a list of one-variable categorical data from a message,
    then sends a customized plot of the data 
    to the server given by the Context object.
    """
    if len(args) == 0: lst = await data_list_categorical(ctx)
    else: lst = args
    await plot_categorical_data(lst, ctx)

@bot.command(pass_context = True)
async def a_c_file(ctx):
    """
    Takes in a list of one-variable categorical data from a 
    file sent by a user, then sends summary statistics (unique values, most common
    value) to the server given by the Context object.
    """
    try:
        
        df = make_df_file(ctx)
        await ctx.send("Enter the column to analyze:")
        column_name = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        ser = df[column_name.content].squeeze()
        await analyze_categorical_data(ser.tolist(), ctx)

    # Invalid file attached
    except RuntimeError:
        await ctx.send("Invalid input! A csv or xsls file must be attached.")

    # User did not respond in time
    except asyncio.TimeoutError:
        await ctx.send("Sorry, you took too long to give an input!")

    # Invalid column name
    except KeyError: 
        await ctx.send("Invalid column name entered!")