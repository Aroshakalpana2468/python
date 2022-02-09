from pyrogram import Client,filters

bot = Client(
    "my first project",
    api_id = 7622044,
    api_hash = "1fcd3dd600503aa1ebc5033b58016264",
    bot_token = "5148488712:AAHahhs2uKE2N7KmgnzfAWLJ2RiVXrsLE0s"
)

@bot.on_message(filters.command('start') & filters.private)
def command1(bot, message):
    bot.send_message(message.chat.id, "Heya, I am a simple test bot.")

@bot.on_message(filters.command('help'))
def command1(bot, message):
    message.reply_text("This is test bot's help section.")


#welcomebot
GROUP = "ak_live_stream_2"
WELCOME_MESSAGE = "Hello, welcome to group chat!"

@bot.on_message(filters.chat(GROUP) & filters.new_chat_members)
def welcomebot(client, message):
    message.reply_text(WELCOME_MESSAGE)

#send_photo
@bot.on_message(filters.command('photo'))
def command3(bot, message):
    bot.send_photo(message.chat.id, "http://imgur.com/gallery/YUJYQ")
    bot.send_photo(message.chat.id, "http://imgur.com/gallery/wYTCtru")


print("I AM ALIVE")
bot.run()