import os
from google import generativeai as genai

# Step 1: Configure with API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Step 2: Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Step 3: Start a chat session
chat = model.start_chat()

print("🤖 RockyBot: Hello! Ask me anything. (type 'exit' to quit)\n")

# Step 4: Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("🤖 RockyBot: Chalo bhai, milte hain phir! 😎")
        break

    try:
        response = chat.send_message(user_input)
        print("🤖 RockyBot:", response.text.strip())
    except Exception as e:
        print("❌ Error:", e)
