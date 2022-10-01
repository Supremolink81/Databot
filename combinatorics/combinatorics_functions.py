import math
from builtins import bot

def permutations(n : int, r : int):
    return math.perm(n, r)

def combinations(n : int, r : int):
    return math.comb(n, r)

async def get_n(ctx):
    await ctx.send("Enter the total amount:")
    n = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
    return int(n.content)

async def get_r(ctx):
    await ctx.send("Enter the number to select:")
    r = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
    return int(r.content)

async def get_p(ctx):
    await ctx.send("Enter the probability of success:")
    p = await bot.wait_for("message", check = lambda m : m.author == ctx.author, timeout = 30)
    return float(r.content)