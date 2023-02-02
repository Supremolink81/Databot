from builtins import bot
from binomial.binomial_functions import *
from combinatorics.combinatorics_functions import *

@bot.command(pass_context = True)
async def binom_prob(ctx, N = None, R = None, P = None):
    """
    Sends the binomial probability of N trials with R successes, each success
    having a probability of P (0 <= P <= 1, 0 <= R <= N), to the server 
    given in the Context object.
    """
    try:

        # If parameters not passed
        if not N: n = await get_n(ctx)
        else: n = int(N)
        if not R: r = await get_r(ctx)
        else: r = int(N)
        if not P: p = await get_p(ctx)
        else: p = float(P)

        # Ensure valid probability is entered
        if p < 0 or p > 1:
            raise RuntimeError

        # Ensure successes <= trials
        if r > n:
            raise ArithmeticError
        
        await ctx.send(f"The probability of getting {r} successes with {n} trials with a {p} chance of succeess is {prob(n, r, p)}")

    # Invalid probability value
    except RuntimeError:
        await ctx.send("Invalid input! Probability must be between 0 and 1.")

    # successes > trials
    except ArithmeticError:
        await ctx.send("Invalid input! Number of trials must be less than number of successes.")

    # Trials and/or successes are not integers 
    except ValueError:
        await ctx.send("Invalid input! Trials and successes must both be positive integers.")
    
@bot.command(pass_context = True)
async def binom_stats(ctx, N = None, P = None):
    """
    Sends summary statistics about a binomial distribution
    with N trials and probability of success P to the server
    given in the Context object (0 <= P <= 1).
    """
    try:

        # If parameters not passed
        if not N: n = await get_n(ctx)
        else: n = int(N)
        if not P: p = await get_p(ctx)
        else: p = float(P)

        # Ensure valid probability is entered
        if p < 0 or p > 1:
            raise RuntimeError
        
        await ctx.send(f"The mean of {n} trials with a {p} chance of succeess is {n*p}")
        await ctx.send(f"The standard deviation of {n} trials with a {p} chance of succeess is {stdev(n, p)}")
    
    # Invalid probability value
    except RuntimeError:
        await ctx.send("Invalid input! Probability must be between 0 and 1.")
    
    # Trials and/or successes are not positive integers 
    except ValueError:
        await ctx.send("Invalid input! Trials and successes must both be positive integers.")