from flask import Flask, request, render_template
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Predefined responses (FAQs) for the chatbot
faq_pairs = [
    (r'hi|hello|hey', ['Hello! How can I help you today?']),
    (r'what is your name?', ['I am your friendly neighborhood chatbot, here to assist you!']),
    (r"what can I do here?", ['I can help you with any questions you have about the course!']),
    (r"how can I reset my password?", ['You can reset your password by clicking on the "Forgot Password" link on the login page.']),
    (r"how can I change my email address?", ['You can change your email address by going to the "Settings" page.']),
    (r"what are your business hours?", ['We are open Monday to Friday, 9am to 5pm. Feel free to email at any time!']),
    (r"Goodbye|Bye|See you later", ['Goodbye! Have a great day!']),
    (r"(.*)", ['I am sorry, I did not understand that. Can you please rephrase your question?'])
]

