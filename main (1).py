<FULL CODE OMITTED HERE FOR BREVITY>
import openai
openai.api_key = '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'  # Replace with your key

def get_ai_suggestion(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Suggest something useful about {query}"}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print("AI Error:", e)
        return "❌ Failed to get suggestion from AI."
@bot.message_handler(func=lambda message: True)
def handle_query(message):
    query = message.text.strip("🌍🍔❤️ ").strip()
    amazon_url = f"https://www.amazon.com/s?k={query.replace(' ', '+')}&tag=nepdostroe-20"
    suggestion = get_ai_suggestion(query)

    response = f"""🔍Search Query: {message.text}

🛒 Amazon Link:
{amazon_url}

🤖 AI Suggestion:
{suggestion}"""

    bot.send_message(message.chat.id, response)
