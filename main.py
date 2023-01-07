from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import random
import fileStreaming
import os

#helper method removing the .json extension from a filename (needed for convenient files)
def removeExtension(fileName):
    return fileName[:fileName.find(".")]

#loading settings from the userSettings save file
settings = fileStreaming.readJsonFile("userSettings.json")

#AI chatbot that will talk based on
class AISpeaker:
    def __init__(self, name):
        self.name = name

        #streaming text file data
        jdata = fileStreaming.readJsonFile(f"bots\\{name}.json")

        #load training data onto the AI speaker
        self.chatbot = ChatBot(name)
        self.listTrainer = ListTrainer(self.chatbot)
        self.listTrainer.train(jdata)

        #adding extra linguistic abilities to the bot
        self.corpusTrainer = ChatterBotCorpusTrainer(self.chatbot)
        self.corpusTrainer.train("chatterbot.corpus.english")

    #responds to the previous message in a conversation
    def query(self, lastMessage):
        response = self.chatbot.get_response(lastMessage)
        return response
        
#loading every bot onto the application
bots = {}
for fileName in os.listdir("bots"):
    botName = removeExtension(fileName)
    bots[botName] = AISpeaker(botName)

print("Type in 'help' for information about this program!")

while True: #main loop of the program
    message = input("> ")

    if message == "help":
        pass
    elif message == "newchat":
        pass
    elif message == "name":
        pass
    elif message == "exit keyword": #set the exit keyword to something
        pass
    elif message == settings["exitcwd"]: #exit the program
        quit()
