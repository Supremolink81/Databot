from builtins import bot
import discord
import math
import seaborn as sns
from scipy import stats as scistats
import matplotlib.pyplot as plt
import pandas as pd
import asyncio

async def analyze_categorical_data(lst : list, ctx):
    """
    Provides summary statistics for one-variable categorical data, including:

    -total items

    -unique items

    -most frequent element
    
    -number of instances of most frequent element
    """
    ser = pd.Series(data = lst, copy = False)
    await ctx.send(f"Total items: {ser.count()}")
    await ctx.send(f"Unique items: {ser.unique()}")
    await ctx.send(f"Most frequent element: {ser.mode()}")
    await ctx.send(f"Number of instances of most frequent element: {ser.value_counts().max()}")

async def data_list_categorical(ctx):
    """
    Reads a list of one-variable categorical data from a user.
    """
    lst = []

    # Random word to ensure user doesn't accidentally end prematurely
    await ctx.send("Enter values (type 'MUNCHKINTASTIC' when finished): ")

    # while user wishes to enter items
    while True:

        try:

            item = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
            if item.content == "MUNCHKINTASTIC": return lst
            else: lst.append(item.content)
            
        # User did not respond in time
        except asyncio.TimeoutError:
            await ctx.send("Sorry, you took too long to give an input!")
            break

        # Certain characters included without escape sequences
        except:
            await ctx.send("Invalid input! any apostrophes (' or \"), back-slashes (\\), percentages (\%) or curly braces ({.}) must be preceded by a back-slash escape sequence.")
            break

async def plot_categorical_data(lst : list, ctx):
    """
    Plots a one-variable categorical dataset.
    """
    try:

        # Plot information
        await ctx.send("Enter Title:")
        title = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
        await ctx.send("Enter plotting method: piechart or countplot")
        method = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)

        plt.title(title.content)

        # Count plot
        if method == "countplot":
            plot = sns.countplot(lst)
            fig = plot.get_figure()
            fig.savefig("graph.png")

        # Pie chart
        elif method == "piechart":
            plt.pie(lst, labels = set(lst), colors = sns.color_palette('bright')[:len(set(lst))], autopct = "%.2f%%")
            plt.savefig("graph.png")

        await ctx.send(file = discord.File("graph.png"))

    # User took too long to respond
    except asyncio.TimeoutError:
        await ctx.send("Sorry, you took too long to give an input!")

    # Invalid plotting method
    except RuntimeError:
        await ctx.send("Invalid method entered!")