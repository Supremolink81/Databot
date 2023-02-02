from discord.ext import commands
from builtins import bot
import asyncio
from quantitative.quantitative_functions import *
from generic.generic_functions import *

@bot.command(pass_context = True)
async def a_q_d(ctx, *args):
    """
    Sends summary statistics about 1-variable, quantitative data from
    user input to the server.
    """
    # No dataset passed in
    if len(args) == 0: lst = await data_list_quantitative(ctx)

    else:
        try:
            lst = list(map(int, args))
        except:
            await ctx.send("Invalid input! All entered values must be numbers.")
            return
    
    await analyze_quantitative_data(lst, ctx)

@bot.command(pass_context = True)
async def a_2q_d(ctx):
    """
    Sends summary statistics about 2-variable, quantitative data from
    user input to the server.
    """
    lst1 = await data_list_quantitative(ctx)
    lst2 = await data_list_quantitative(ctx)
    await analyze_quantitative_data_2(lst1, lst2, ctx)

@bot.command(pass_context = True)
async def p_q_d(ctx, *args):
    """
    Plots 1-variable, quantitative data and sends the plot to the server.
    """
    if len(args) == 0: lst = await data_list_quantitative(ctx)
    else:
        try:
            lst = list(map(int, args))
        except:
            await ctx.send("Invalid input! All entered values must be numbers.")
            return
    await plot_quantitative_data(lst, ctx)

@bot.command(pass_context = True)
async def p_2q_d(ctx):
    """
    Plots 2-variable, quantitative data and sends the plot to the server.
    """
    lst1 = await data_list_quantitative(ctx)
    lst2 = await data_list_quantitative(ctx)
    await plot_quantitative_data_2(lst1, lst2, ctx)

@bot.command(pass_context = True)
async def a_q_file(ctx, col = None):
    """
    Send summary statistics about 1-variable, quantitative data
    from a csv or xsls file to the server.
    """
    try:
        df = make_df_file(ctx)
        if not col: 
            await ctx.send("Enter the column to analyze:")
            column_name = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        else: column_name = col
        ser = df[column_name.content].squeeze()
        await analyze_quantitative_data(ser.tolist(), ctx)
    
    # Not csv or xsls file
    except RuntimeError:
        await ctx.send("Invalid input! A csv or xsls file must be attached.")

    # Useer took too long to respond
    except asyncio.TimeoutError:
        await ctx.send("Sorry, you took too long to give an input!")

    # Invalid column name
    except KeyError: 
        await ctx.send("Invalid column name entered!")

@bot.command(pass_context = True)
async def a_2q_file(ctx, col1 = None, col2 = None):
    """
    Send summary statistics about 2-variable, quantitative data
    from a csv or xsls file to the server.
    """
    try:
        df = make_df_file(ctx)

        # Column name 1 not passed as parameter
        if not col1: 
            await ctx.send("Enter the first column:")
            column_name_1 = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        else: column_name_1 = col1

        # Column name 2 not passed as parameter
        if not col2:
            await ctx.send("Enter the second column:")
            column_name_2 = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        else: column_name_2 = col2

        ser1 = df[column_name_1.content].squeeze()
        ser2 = df[column_name_2.content].squeeze()
        await analyze_quantitative_data_2(ser1.tolist(), ser2.tolist(), ctx)

    # Not csv or xsls file
    except RuntimeError:
        await ctx.send("Invalid input! A csv or xsls file must be attached.")

    # Useer took too long to respond
    except asyncio.TimeoutError:
        await ctx.send("Sorry, you took too long to give an input!")

    # Invalid column name
    except KeyError: 
        await ctx.send("Invalid column name entered!")