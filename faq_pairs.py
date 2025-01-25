# Predefined responses (FAQs) for the chatbot to use to answer user questions
# Pairs allow the chatbot to respond to user input based on the regular expression pattern
faq_pairs = [
    # Greetings
    (r'hi|hello|hey', ['Hello! How can I help you today?', 'Hi there! How can I assist you?']),
    (r'good morning|good afternoon|good evening', ['Good day! How can I help you?', 'Hello! What can I do for you?']),
    (r'how are you?', ['I am just a bot, but I am here to assist you! How can I help?']),

    # Basic Information
    (r'what is your name\??', ['I am your friendly neighborhood chatbot, here to assist you!', 'You can call me ChatBot!']),
    (r"what can I do here\??", ['You can ask me questions about our services, courses, or general inquiries.']),
    (r"what is this platform for\??", ['This platform is designed to provide assistance and information for your needs!']),

    # Account & Settings
    (r"how can I reset my password\??", [
        'You can reset your password by clicking on the "Forgot Password" link on the login page.',
        'If you have trouble resetting your password, feel free to contact support.'
    ]),
    (r"how can I change my email address\??", ['You can change your email address by going to the "Settings" page.']),
    (r"how do I delete my account\??", [
        'We are sorry to see you go! To delete your account, please visit the "Settings" page and follow the account deletion instructions.',
        'If you need help deleting your account, contact support.'
    ]),
    (r"how do I update my profile picture\??", ['You can update your profile picture on the "Profile" page by uploading a new photo.']),

    # Services and Features
    (r"what services do you offer\??", ['We provide assistance with courses, account management, and general inquiries.']),
    (r"how can I access the courses\??", ['You can access the courses from the "Courses" section in the main menu.']),
    (r"do you offer refunds\??", [
        'Yes, we offer refunds within 30 days of purchase. Please contact support for assistance.',
        'Refunds are subject to our refund policy. Check the "Refund Policy" page for more information.'
    ]),
    (r"how do I download the course materials\??", ['You can download course materials from the "Downloads" section of the course page.']),

    # Business & Contact Info
    (r"what are your business hours\??", [
        'We are open Monday to Friday, 9am to 5pm. Feel free to email at any time!',
        'Our support team is available during business hours: 9 AM to 5 PM (Monday to Friday).'
    ]),
    (r"where are you located\??", [
        'Our headquarters are located at 123 Main Street, Springfield, USA.',
        'We are an online-first platform but our main office is located in Springfield.'
    ]),
    (r"how do I contact support\??", [
        'You can contact support by emailing support@company.com or calling 1-800-123-4567.',
        'Our support team is available at support@company.com!'
    ]),
    (r"do you have a phone number\??", ['Yes, you can call us at 1-800-123-4567.']),

    # Technical Support
    (r"why am I unable to log in\??", [
        'Please ensure you are using the correct username and password. If the problem persists, try resetting your password.',
        'Try clearing your browser cache or using a different browser. If the issue continues, contact support.'
    ]),
    (r"why is the website slow\??", [
        'It might be due to high traffic. Try refreshing the page or checking your internet connection.',
        'We are working to resolve any performance issues. Please try again later or contact support if it continues.'
    ]),
    (r"how do I clear my browser cache\??", [
        'To clear your browser cache, go to your browser settings and look for "Clear Browsing Data."',
        'You can search online for specific instructions based on your browser (e.g., Chrome, Firefox, Edge).'
    ]),

    # Payments
    (r"how do I make a payment\??", ['You can make a payment through the "Payments" section in your account.']),
    (r"what payment methods do you accept\??", ['We accept credit/debit cards, PayPal, and other major payment methods.']),
    (r"is my payment information secure\??", ['Yes, your payment information is encrypted and secure.']),
    (r"can I set up a payment plan\??", [
        'Yes, we offer payment plans for select courses. Check the course page for more details.',
        'Payment plans are available for certain services. Please contact billing support for assistance.'
    ]),

    # FAQs for Miscellaneous
    (r"what is your refund policy\??", [
        'We offer a 30-day money-back guarantee on most purchases. Check our refund policy for more details.',
        'Our refund policy allows for refunds within 30 days of purchase. Please contact support for help.'
    ]),
    (r"how do I track my order\??", [
        'You can track your order by clicking the "Track Order" link in your confirmation email.',
        'Order tracking is available on the "My Orders" page after logging in.'
    ]),
    (r"do you offer gift cards\??", ['Yes, we offer gift cards! Check out the "Gift Cards" page for more information.']),
    (r"what is your privacy policy\??", [
        'You can read our privacy policy on the "Privacy Policy" page linked in the website footer.',
        'Our privacy policy outlines how we handle your data securely. Visit the Privacy Policy page for details.'
    ]),

    # Farewell
    (r"goodbye|bye|see you later", ['Goodbye! Have a great day!', 'Take care! Hope to assist you again soon.']),

    # Fallback
    (r"(.*)", [
        'I am sorry, I did not understand that. Can you please rephrase your question?',
        'Can you clarify your query? I want to make sure I provide the right information.'
    ])
]
