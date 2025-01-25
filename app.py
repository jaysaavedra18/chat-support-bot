from flask import Flask, request, render_template
import nltk
from nltk.chat.util import Chat, reflections
from faq_pairs import faq_pairs

# Initialize the Flask app
app = Flask(__name__)

# Create a chatbot using the predefined responses and reflections
# The reflections dictionary allows the chatbot to respond with pronouns based on the user input
chatbot = Chat(faq_pairs, reflections)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    chatbot_response = chatbot.respond(user_input)
    return chatbot_response

if __name__ == '__main__':
    app.run(debug=True)