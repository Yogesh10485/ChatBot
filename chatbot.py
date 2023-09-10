import openai

openai.api_key = "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"

messages = []

messages.append({"role": "system", "content": "you are professional wordpress web developer"})


while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")