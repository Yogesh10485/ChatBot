import openai
import gradio

openai.api_key = "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"


messages = [{"role": "system", "content": "You are DevOps Engineer and an expert in writing terraform scripts for bitbucket"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "DevOps Engineer and Terraform script Writer")

demo.launch(share=True)