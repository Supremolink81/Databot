from discord.ext import commands
from builtins import bot
from combinatorics.combinatorics_functions import *

@bot.command(pass_context = True)
async def nCr(ctx, N = None, R = None):
    while True:
        try:
            if not N: N = await get_n(ctx)
            else: N = int(N)
            if not R: R = await get_r(ctx)
            else: R = int(R)
            if R > N:
                raise ArithmeticError
            else:
                await ctx.send(f"The number of combinations of n, choose r is {combinations(N, R)}")
            break
        except ArithmeticError:
            await ctx.send("Number of successes cannot be greater than number of trials.")
        except ValueError:
            await ctx.send("Invalid input entered! Both the trials and successes must be integers")

@bot.command(pass_context = True)
async def nPr(ctx, N = None, R = None):
    while True:
        try:
            if not N: N = await get_n(ctx)
            else: N = int(N)
            if not R: R = await get_r(ctx)
            else: R = int(R)
            if R > N:
                raise ArithmeticError
            else:
                await ctx.send(f"The number of permutations of n, choose r is {permutations(N, R)}")
            break
        except ArithmeticError:
            await ctx.send("Number of successes cannot be greater than number of trials.")
        except ValueError:
            await ctx.send("Invalid input entered! Both the trials and successes must be integers")