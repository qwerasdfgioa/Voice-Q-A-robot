import re
import pyttsx3

def remove_non_text_elements(text):
    # 定义一个正则表达式，匹配表情符号和特殊符号
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # 表情符号
        "\U0001F300-\U0001F5FF"  # 符号和图标
        "\U0001F680-\U0001F6FF"  # 运输和地图图标
        "\U0001F1E0-\U0001F1FF"  # 国旗
        "\U00002500-\U00002BEF"  # 其他符号
        "\U00002700-\U000027BF"  # 杂项符号
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U00002000-\U0000207F"  # 常见符号和标点
        "]+",
        flags=re.UNICODE
    )

    # 使用正则表达式移除匹配的部分
    return emoji_pattern.sub(r'', text)

# 移除非文字元素
# clean_text = remove_non_text_elements(responses)
#
# print(clean_text)  # 输出：你好，这是一个测试文本！

def speak(text, rate=225, volume=1.0):
    engine = pyttsx3.init()
    # 设置语速
    engine.setProperty('rate', rate)
    # 设置音量
    engine.setProperty('volume', volume)
    engine.say(text)
    engine.runAndWait()
# speak(clean_text, rate=200, volume=1)

