from openai import OpenAI

client = OpenAI(
    api_key="gsk_......................TQ1w",
    base_url="https://api.groq.com/openai/v1"
)

messages = [
    {"role": "system", "content": "You are a medical bot. Provide accurate and concise medical information."}
]

while True:
    user = input("you: ")
    if user.lower() == "quit":
        print("bot says: Bye!")
        break

    messages.append({"role": "user", "content": user})

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages
    )

    bot_reply = response.choices[0].message.content
    print("bot:", bot_reply)

    messages.append({"role": "assistant", "content": bot_reply})
