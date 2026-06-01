import gradio as gr
import openai

openai.api_key = "sk-66e55d25a2b141809fd79655ddb7f807"
openai.api_base = "https://api.deepseek.com/v1"

def chat(message, history):
    messages = [{"role": "system", "content": "你是一个专业的法语老师，帮助学生检查法语语法错误，用中文解释错误原因并给出修改建议。"}]
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        messages.append({"role": "assistant", "content": h[1]})
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(model="deepseek-chat", messages=messages)
    return response.choices[0].message.content

gr.ChatInterface(chat, title="🇫🇷 AI法语学习助手").launch(server_name="0.0.0.0", server_port=8501)
