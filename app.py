from flask import Flask, request, render_template
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Predefined responses (FAQs) for the chatbot
faq_pairs = [
    (r'hi|hello|hey', ['Hello! How can I help you today?']),
    (r'what is your name?', ['I am your friendly neighborhood chatbot, here to assist you!']),
]