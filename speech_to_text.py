import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def listen_and_recognize():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("请说话...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="zh-CN")
        print("你说的是: " + text)
        return text
    except sr.UnknownValueError:
        print("无法识别音频")
        return ""
    except sr.RequestError as e:
        print("无法请求结果; {0}".format(e))
        return ""

