from builtins import bot
import discord
import math
import seaborn as sns
from scipy import stats as scistats
import matplotlib.pyplot as plt
import pandas as pd
import asyncio
import os
from generic.generic_functions import *

#QUANTITATIVE DATA
async def analyze_quantitative_data(lst : list, ctx):
    """
    Provides summary statistics about 1-variable quantitative data, including:

    -mean, median and mode

    -variance and standard deviation

    -interquartile range

    -minimum and maximum values

    -range between min and max
    """
    IQR = scistats.iqr(lst, rng=(25, 75), interpolation="midpoint")
    ser = pd.Series(lst)
    await ctx.send(f"Minimum value: {ser.min()}")
    await ctx.send(f"Maximum value: {ser.max()}")
    await ctx.send(f"Range: {ser.max()-ser.min()}")
    await ctx.send(f"Mean: {ser.mean()}")
    await ctx.send(f"Median: {ser.median()}")
    await ctx.send(f"Mode: {ser.mode()}")
    await ctx.send(f"Variance: {ser.var()}")
    await ctx.send(f"Standard deviation: {ser.std()}")
    await ctx.send(f"Interquartile range (IQR): {IQR}")

async def analyze_quantitative_data_2(lstX : list, lstY : list, ctx):
    """
    Provides summary statistics about 1-variable quantitative data, including:

    ONE VARIABLE STATS

    -mean, median and mode

    -variance and standard deviation

    -interquartile range

    -minimum and maximum values

    -range between min and max

    TWO VARIABLE STATS

    -regression equation

    -correlation

    -correlation coefficient

    -p-value of regression line

    -standard error
    """

    # One variable statistics
    await ctx.send("Statistics for X: \n\n")
    await analyze_quantitative_data(lstX, ctx)
    await ctx.send("Statistics for Y: \n\n")
    await analyze_quantitative_data(lstY, ctx)

    # Regression line
    regression = scistats.linregress(lstX, lstY)

    # Two variable statistics
    await ctx.send(f"\nEquation: y = {regression.intercept} + {regression.slope}x")
    await ctx.send(f"Correlation: {regression.rvalue}")
    await ctx.send(f"Correlation coefficent: {regression.rvalue**2}")
    await ctx.send(f"P-Value: {regression.pvalue}")
    await ctx.send(f"Standard error: {regression.stderr}")

async def data_list_quantitative(ctx) -> list:
    """
    Creates a 1-dimensional list of quantitative data 
    to be used for analysis.
    """
    lst = []
    await ctx.send("Enter values (type 'done' when finished): ")

    while True:
        try:
            item = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
            if item.content == "done": 
                if len(lst) == 0: raise RuntimeError
                else: return lst
            try:
                if item.content[-1] == "!": lst.append(math.factorial(int(item.content[:-1])))
                elif "^" in item.content: lst.append(math.pow(float(item.content[:item.content.index("^")]), float(item.content[item.content.index("^")+1:])))
                else: lst.append(float(item.content))
            except ValueError: 
                await ctx.send("Invalid input! Must be a number.")
                continue
        except asyncio.TimeoutError:
            await ctx.send("Sorry, you took too long to give an input!")
            break
        except RuntimeError:
            await ctx.send("You must add at least one number to the data")

async def plot_quantitative_data(lst : list, ctx):
    """
    Plots 1-variable, quantitative data in a visual plot.

    Plots are given a title, axis values, and a plotting method from the following options:

    -histogram

    -distplot

    -boxplot
    """

    # Check for valid hex color
    def color_check(message):
        return message.author == ctx.author and len(message.content) == 7 and message.content[0] == '#'

    try:

        # Plot information
        await ctx.send("Enter Title:")
        title = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        await ctx.send("Enter X-Axis Label:")
        X = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        await ctx.send("Enter Y-Axis Label:")
        Y = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        df = make_df(lst, "DATA")
        await ctx.send("Enter plotting method: histogram, distplot, or boxplot")
        method = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)

        # Histogram
        if method.content == 'histogram':
            await ctx.send("Enter bin width:")
            width = await bot.wait_for("message", check = lambda m : m.author == ctx.author)
            await ctx.send("Enter color as a hexadecimal code (e.g. #706C5C):")
            col = await bot.wait_for("message", check = color_check, timeout = 30)
            plot = sns.histplot(data = df["DATA"], binwidth = int(width.content), color = col.content)

        # Distplot
        elif method.content == 'distplot':
            await ctx.send("Enter bin width:")
            width = await bot.wait_for("message", check = lambda m : m.author == ctx.author)
            await ctx.send("Show histogram?")
            positive = ["y", "ye", "yes", "ok", "alright"]
            negative = ["n", "no", "nah", "no thanks", "nope"]
            op = await bot.wait_for("message", check = lambda m : m.author == ctx.author and (m.content in positive or m.content in negative))
            await ctx.send("Enter color as a hexadecimal code (e.g. #706C5C):")
            col = await bot.wait_for("message", check = color_check, timeout = 30)
            plot = sns.distplot(a = df["DATA"].squeeze(), binwidth = int(width.content), color = col.content, hist = (op in positive))

        # Boxplot
        elif method.content == "boxplot":
            await ctx.send("Enter color as a hexadecimal code (e.g. #706C5C):")
            col = await bot.wait_for("message", check = color_check, timeout = 30)
            plot = sns.boxplot(data = df["DATA"], color = col.content)

        # Invalid method entered
        else:
            raise RuntimeError

        # Plot generation
        plt.title(title.content)
        plt.xlabel(X.content)
        plt.ylabel(Y.content)
        fig = plot.get_figure()
        fig.savefig("graph.png")
        await ctx.send(file = discord.File("graph.png"))

        # Cleanup
        os.remove("graph.png")
    
    # User took too long to respond
    except asyncio.TimeoutError:
        await ctx.send("Sorry, you took too long to give an input!")

    # Bin width must be a positive integer
    except ValueError:
        await ctx.send("Invalid bin width entered! Must be a positive integer.")

    # Invalid plotting method
    except RuntimeError:
        await ctx.send("Invalid method entered!")

async def plot_quantitative_data_2(lstX : list, lstY : list, ctx):
    """
    Plots 1-variable, quantitative data in a visual plot.

    Plots are given a title, axis values, and a plotting method from the following options:

    -linear regression model

    -scatteplot

    -heatmap
    """

    # Check for valid hex color
    def color_check(message):
        return message.author == ctx.author and len(message.content) == 7 and message.content[0] == '#'

    try:

        # Plot information
        await ctx.send("Enter Title:")
        title = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        await ctx.send("Enter X-Axis Label:")
        X = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        await ctx.send("Enter Y-Axis Label:")
        Y = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        await ctx.send("Enter color as a hexadecimal code (e.g. #706C5C):")
        col = await bot.wait_for("message", check = color_check, timeout = 30)
        df = make_df(lstX, "X-Axis", lstY, "Y-Axis")
        await ctx.send("Enter plotting method: linearmodel, scatterplot, or heatmap")
        method = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)

        # Linear regression model
        if method.content == "linearmodel":
            plot = sns.regplot(data = df, x = "X-Axis", y = "Y-Axis", color = col.content)

        # Scatterplot
        elif method.content == "scatterplot":
            plot = sns.scatterplot(data = df, x = "X-Axis", y = "Y-Axis", color = col.content)

        # Heatmap
        elif method.content == "heatmap":
            plot = sns.heatmap(data = df)
        
        # Invalid plotting method
        else:
            raise RuntimeError

        # Plot generation
        plt.title(title.content)
        plt.xlabel(X.content)
        plt.ylabel(Y.content)
        fig = plot.get_figure()
        fig.savefig("graph.png")
        await ctx.send(file = discord.File("graph.png"))

        # Cleanup
        os.remove("graph.png")
    
    # User took too long to respond
    except asyncio.TimeoutError:
        await ctx.send("Sorry, you took too long to give an input!")

    # Invalid plotting method
    except RuntimeError:
        await ctx.send("Invalid method entered!")

def normal_cdf(mean : float, sd : float, value : float) -> float:
    """
    Returns the proportion of values
    less than or equal to the one plugged in, or the
    probability a value less than or equal to the one
    plugged in occurs by chance.
    """
    return scistats.norm(mean,sd).cdf(value)