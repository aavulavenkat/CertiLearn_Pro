import os
import telebot
from flask import Flask, request

API_TOKEN = os.getenv('TELEGRAM_TOKEN', '6214968103:AAFwHN0dK2_o_MWYqLnEjZGsOIK72NDRiS4')
WEBHOOK_HOST = os.getenv('WEBHOOK_HOST', 'https://your-render-app.onrender.com')
WEBHOOK_PATH = f"/webhook/{API_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

bot = telebot.TeleBot(API_TOKEN)

# Flask server to handle webhook requests
app = Flask(__name__)

msg = "Here is what you asked!"

# Commands start here ------------>

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''Welcome to Certi Learn Pro bot!
    /help 
    /learn
    ''')

@bot.message_handler(commands=['learn'])
def learn(message):
    bot.send_message(message.chat.id, '''Here are the popular topics:
    /python
    /java
    /WebDevelopment
    ''')

@bot.message_handler(commands=['python'])
def python(message):
    bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=XKHEtdqhLK8")

@bot.message_handler(commands=['java'])
def java(message):
    bot.send_message(message.chat.id, "https://youtu.be/hBh_CC5y8-s")

@bot.message_handler(commands=['WebDevelopment'])
def WebDevelopment(message):
    bot.send_message(message.chat.id, '''Great! WebDevelopment includes languages like HTML, CSS, JS
    https://youtu.be/tVzUXW6siu0?si=bFprtIudcZrATkOr''')

@bot.message_handler(commands=['certifications'])
def certifications(message):
    bot.send_message(message.chat.id, '''Select the platforms from where you want to certify..
    /linkedin
    /google
    /microsoft
    /freecodecamp 
    ''')

@bot.message_handler(commands=['linkedin'])
def linkedin(message):
    bot.send_message(message.chat.id, f"{msg}\nhttps://www.linkedin.com/learning/browse/certifications")

@bot.message_handler(commands=['google'])
def google(message):
    bot.send_message(message.chat.id, f"{msg}\nhttps://grow.google/intl/en_in/certificates/")

@bot.message_handler(commands=['microsoft'])
def microsoft(message):
    bot.send_message(message.chat.id, f"{msg}\nhttps://learn.microsoft.com/en-us/credentials/browse/?credential_types=certification")

@bot.message_handler(commands=['freecodecamp'])
def freecodecamp(message):
    bot.send_message(message.chat.id, f"{msg}\nhttps://www.freecodecamp.org/learn/")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, """ 
    Hi there!

Welcome to Certi Learn Pro bot. I'm here to help you with anything you need, from adding more content to our bot to getting help with your existing content.

Here are some things you can do with my bot:
   
1. Add more content.
2. Get help with your existing content.
3. Report a bug.

   I'm always happy to help, so please don't hesitate to contact me if you have any questions or need any assistance.

   Contact: @gamervicky456@gmail.com""")

# Webhook setup and handling
@app.route(WEBHOOK_PATH, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return '', 403

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
