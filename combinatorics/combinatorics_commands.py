from discord.ext import commands
from builtins import bot
from combinatorics.combinatorics_functions import *

@bot.command(pass_context = True)
async def nCr(ctx, N = None, R = None):
    """
    Send the number of r-permutations in an n-length sequence
    to the server given by the Context object.
    """
    try:
        # Parameters not passed
        if not N: N = await get_n(ctx)
        else: N = int(N)
        if not R: R = await get_r(ctx)
        else: R = int(R)

        # Number of successes > number of trials
        if R > N:
            raise ArithmeticError
        
        await ctx.send(f"The number of combinations of n, choose r is {combinations(N, R)}")

    # Number of successes greater than number of trials
    except ArithmeticError:
        await ctx.send("Number of successes cannot be greater than number of trials.")

    # Trials and/or successes are not positive integers
    except ValueError:
        await ctx.send("Invalid input entered! Both the trials and successes must be positive integers.")

@bot.command(pass_context = True)
async def nPr(ctx, N = None, R = None):
    """
    Sends the number of r-combinations in an n-length sequence
    to the server given by the Context object.
    """
    try:
        # If parameters not passed
        if not N: N = await get_n(ctx)
        else: N = int(N)
        if not R: R = await get_r(ctx)
        else: R = int(R)

        # Number of successes > number of trials
        if R > N:
            raise ArithmeticError
        
        await ctx.send(f"The number of permutations of n, choose r is {permutations(N, R)}")
    
    # Number of successes greater than number of trials
    except ArithmeticError:
        await ctx.send("Number of successes cannot be greater than number of trials.")

    # Trials and/or successes are not positive integers
    except ValueError:
        await ctx.send("Invalid input entered! Both the trials and successes must be positive integers.")