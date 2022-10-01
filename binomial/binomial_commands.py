from builtins import bot
from binomial.binomial_functions import *
from combinatorics.combinatorics_functions import *

@bot.command(pass_context = True)
async def binom_prob(ctx, N = None, R = None, P = None):
    try:
        if not N: n = await get_n(ctx)
        else: n = int(N)
        if not R: r = await get_r(ctx)
        else: r = int(N)
        if not P: p = await get_p(ctx)
        else: p = float(P)
        if p < 0 or p > 1:
            raise RuntimeError
        await ctx.send(f"The probability of getting {r} successes with {n} trials with a {p} chance of succeess is {prob(n, r, p)}")
    except RuntimeError:
        await ctx.send("Invalid input! Probability must be between 0 and 1.")
    except ValueError:
        await ctx.send("Invalid input! Trials and successes must both be integers, and probability must be a decimal between 0 and 1.")
    
@bot.command(pass_context = True)
async def binom_stats(ctx, N = None, P = None):
    try:
        if not N: n = await get_n(ctx)
        else: n = int(N)
        if not P: p = await get_p(ctx)
        else: p = float(P)
        if p < 0 or p > 1:
            raise RuntimeError
        await ctx.send(f"The mean of {n} trials with a {p} chance of succeess is {n*p}")
        await ctx.send(f"The standard deviation of {n} trials with a {p} chance of succeess is {stdev(n, p)}")
    except RuntimeError:
        await ctx.send("Invalid input! Probability must be between 0 and 1.")
    except ValueError:
        await ctx.send("Invalid input! Trials and successes must both be integers, and probability must be between 0 and 1.")