import discord
import chatbots

currentBot = chatbots.bots["Trollbot"]

#setting up the discord infrastructure
class BotClient(discord.Client):
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

        if doResponse: #respond to the message based on the data being fed
            await message.reply(currentBot.query(message.content))
        else:
            pass

#logging the bot onto discord
botToken = "MTA2MTM4MDUyNTQwNDcyOTM0NA.GLfkX1.cJkirrxUu2eYEvag8npFLUDbFJvkReNsrdWxp4"
botClient = BotClient()
botClient.run(botToken)