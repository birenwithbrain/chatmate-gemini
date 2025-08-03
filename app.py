from flask import Flask, render_template, request, jsonify
from google import generativeai as genai
import os

app = Flask(__name__)

# API key configure karna
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Chat object globally maintain karna
chat = model.start_chat()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_response():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"response": "Kya bolu bhai? Khaali message!"})

    if user_input.lower() == 'exit':
        return jsonify({"response": "Accha bhai, fir milenge! 😎"})

    response = chat.send_message(user_input)
    return jsonify({"response": response.text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
