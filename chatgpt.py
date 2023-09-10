import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write an essay on trees"}])
print(completion.choices[0].message.content)