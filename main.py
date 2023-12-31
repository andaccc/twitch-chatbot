from loguru import logger
from twitchio.ext import commands
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

class Bot(commands.Bot):

    def __init__(self, *args, **kwargs):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(*args, **kwargs)

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'{config['BOT_PREFIX']}Hello {ctx.author.name}!')

    @commands.command()
    async def startpomo(self, ctx: commands.Context, task_name) -> None:
        # default 25 mins
        await ctx.send(f"{config['BOT_PREFIX']} time to focus on {task_name}!")

if __name__ == "__main__":
    channels = [config['CHANNELS']]
    client_id = config['CLIENT_ID']
    client_secret = config['CLIENT_SECRET']
    token = config['TOKEN']

    bot = Bot(
        token=token, 
        prefix="!", 
        initial_channels=channels
    )

    bot.run() # blocking
