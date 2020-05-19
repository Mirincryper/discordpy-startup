from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='sk\')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

await client.change_presence(activity=discord.Game(name='my game'))

# or, for watching:
activity = discord.Activity(name='test', type=discord.ActivityType.watching)
await client.change_presence(activity=activity)                   

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def help(ctx):
    await ctx.send('表示テストtest
ping=動作確認用です
mirin=まぁ…いいやつだったよ…
まだまだ機能追加')
                   
@bot.command()
async def mirin(ctx):
    await ctx.send('まぁ…いいやつだったよ…')
                   
bot.run(token)
