import math
from builtins import bot

def permutations(n : int, r : int):
    """
    Number of r-permutations in an n-length sequence.
    """
    return math.perm(n, r)

def combinations(n : int, r : int):
    """
    Number of r-combinations in an n-length sequence.
    """
    return math.comb(n, r)

async def get_n(ctx):
    """
    Gets an N value from the user (usually total length or trials).
    """
    await ctx.send("Enter the total amount:")
    n = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
    return int(n.content)

async def get_r(ctx):
    """
    Gets an R value from the user (usually permutations/combination length or successes).
    """
    await ctx.send("Enter the number to select:")
    r = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
    return int(r.content)

async def get_p(ctx):
    """
    Gets a P value from the user (usually probability).
    """
    await ctx.send("Enter the probability of success:")
    p = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
    return float(p.content)