from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot=ChatBot("Chat BOT")

conversation = [
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
]
trainer = ListTrainer(bot)
trainer.train(conversation)

response=bot.get_response("Hello")
print("From Bot :" , response)