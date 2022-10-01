from discord.ext import commands
from builtins import bot
import asyncio
from quantitative.quantitative_functions import *
from generic.generic_functions import *

@bot.command(pass_context = True)
async def a_q_d(ctx, *args):
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
    lst1 = await data_list_quantitative(ctx)
    lst2 = await data_list_quantitative(ctx)
    await analyze_quantitative_data_2(lst1, lst2, ctx)

@bot.command(pass_context = True)
async def p_q_d(ctx, *args):
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
    lst1 = await data_list_quantitative(ctx)
    lst2 = await data_list_quantitative(ctx)
    await plot_quantitative_data_2(lst1, lst2, ctx)

@bot.command(pass_context = True)
async def a_q_file(ctx, col = None):
    try:
        df = make_df_file(ctx)
        if not col: 
            await ctx.send("Enter the column to analyze:")
            column_name = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        else: column_name = col
        ser = df[column_name.content].squeeze()
        await analyze_quantitative_data(ser.tolist(), ctx)
    except RuntimeError:
        await ctx.send("Invalid input! A csv or xsls file must be attached.")
    except asyncio.TimeoutError:
        await ctx.send("Sorry, you took too long to give an input!")
    except KeyError: 
        await ctx.send("Invalid column name entered!")

@bot.command(pass_context = True)
async def a_2q_file(ctx, col1 = None, col2 = None):
    try:
        df = make_df_file(ctx)
        if not col1: 
            await ctx.send("Enter the first column:")
            column_name_1 = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        else: column_name_1 = col1
        if not col2:
            await ctx.send("Enter the second column:")
            column_name_2 = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        else: column_name_2 = col2
        ser1 = df[column_name_1.content].squeeze()
        ser2 = df[column_name_2.content].squeeze()
        await analyze_quantitative_data_2(ser1.tolist(), ser2.tolist(), ctx)
    except RuntimeError:
        await ctx.send("Invalid input! A csv or xsls file must be attached.")
    except asyncio.TimeoutError:
        await ctx.send("Sorry, you took too long to give an input!")
    except KeyError: 
        await ctx.send("Invalid column name entered!")