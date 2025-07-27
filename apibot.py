from openai import OpenAI

client=OpenAI(
    api_key="gsk_.......................TQ1w",
    base_url="https://api.groq.com/openai/v1"
)

while True:
    user=input("you:")
    if user=="quit":
        print("bot says: bye")
    response=client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role":"system","content":"you are a medical bot ,provide information medical"},
            {"role":"user","content":user}
        ]
    )
    print("bot:",response.choices[0].message.content)


