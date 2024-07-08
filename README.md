# 语音问答助手-glm

在这里我使用glm-4作为基座模型构建了一个语音问答助手

你可以自由的向机器人提问，例如”你好！“，“介绍一下大语言模型。”等等


## 如何使用
首先你需要确保安装了以下的库

`pip install pynput pyttsx3 zhipuai speechrecognition`

需要使用代码时，建议你的环境python版本不低于3.6否则可能出现奇怪的错误

注意你需要在`GLM.py`中使用自己的apiKey（在GLM官方平台申请即可https://maas.aminer.cn/overview ，首次登陆你将获得大量的免费token）

接下运行`main.py`即可
