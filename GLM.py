from zhipuai import ZhipuAI

client = ZhipuAI(api_key="你的apikey") # 请填写您自己的APIKey

def get_completions(text):
    prompt = '请尽量将回答限制在150字以内'

    response = client.chat.completions.create(
        model="glm-4",  # 请选择参考官方文档，填写需要调用的模型名称
        messages=[{"role": "system", "content": "你是人工智能助手小谢，尽量输出简洁。"},
                  {"role": "user", "content": text + prompt}], # 将结果设置为“消息”格式
        stream=True,  # 流式输出
    )
    full_content = ''  # 合并输出
    for chunk in response:
        full_content += chunk.choices[0].delta.content
    return full_content


