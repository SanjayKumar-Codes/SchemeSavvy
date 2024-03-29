import google.generativeai as genai

# Configure Google API
GOOGLE_API_KEY = 'API_KEY'
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Generative Model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_response(msg):
    response = chat.send_message(msg)
    return response.text
