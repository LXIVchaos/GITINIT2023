import discord
from discord import app_commands
from discord.ext import commands
import chatbots
import random
import sqlite3

global currentBot 
currentBot = "Trollbot"

#setting up the discord infrastructure
class BotClient(commands.Bot):
    async def on_message(self, message): #should the bot be pinged in any way, it will respond to the user.
        if message.author == self.user:
            return

        doResponse = False
        
        #check if the bot was pinged in the message
        for member in message.mentions:
            if member == self.user:
                doResponse = True
                break

        #check if said message was a reply to the bot
        reference = message.reference
        if reference != None:
            rm = reference.cached_message
            if rm == None:
                channel = self.get_channel(reference.channel_id)
                rm = await channel.fetch_message(reference.message_id)

            if rm.author == self.user:
                doResponse = True

        if doResponse or random.randint(1, 25) == 1: #respond to the message based on the data being fed
            await message.reply(chatbots.bots[currentBot].query(message.content))            

    async def on_ready(self):
        await self.tree.sync()
        print("ready to go!")

botClient = BotClient(command_prefix = "!", intents = discord.Intents.all())

@botClient.tree.command(name = "mode", description = "Change the bot's behavior to a specified setting.")
@discord.app_commands.describe(mode = "mode")
async def mode_command(interaction, mode: str): #changes which AI is being used to chat
    if testparam in chatbots.bots:
        global currentBot
        currentBot = testparam
        embed = discord.Embed(colour = discord.Colour.green())
        embed.set_author(name = "Successfully updated Bot Mode!", icon_url = botClient.user.avatar.url)
        await interaction.response.send_message(embed = embed)
    else:
        embed = discord.Embed(colour = discord.Colour.red())
        embed.set_author(name = "Bot mode not found.", icon_url = botClient.user.avatar.url)
        await interaction.response.send_message(embed = embed)

@botClient.tree.command(name = "modeinfo", description = "List of currently available chat bot modes for this bot.")
async def info_command(interaction): #returns a list of all the loaded bots
    concat = ""
    for mode in chatbots.bots:
        concat += mode + " "

    #create an embed to make the message look prettier
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.set_author(name = "Mode Information", icon_url = botClient.user.avatar.url)
    embed.add_field(name = "Current Mode:", value = currentBot, inline = True)
    embed.add_field(name = "Available Modes:", value = concat, inline = False)

    await interaction.response.send_message(embed = embed)

#logging the bot onto discord
botToken = ""
botClient.run(botToken)