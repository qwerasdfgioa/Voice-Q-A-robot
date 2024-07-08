import GLM
import speech_to_text
import Glm_Speak
import threading
import time
from pynput import keyboard

exit_flag = False
recording = False

def on_press(key):
    global exit_flag, recording
    try:
        if key.char == 's' and not recording:
            recording = True
            threading.Thread(target=record_and_process).start()
        elif key.char == 'e' and recording:
            recording = False
        elif key.char == 'q':
            exit_flag = True
            return False
    except AttributeError:
        pass

def record_and_process():
    global recording
    while recording:
        text = speech_to_text.listen_and_recognize()
        if text:
            result = GLM.get_completions(text)
            result = Glm_Speak.remove_non_text_elements(result)
            print(result)
            Glm_Speak.speak(result)

listener = keyboard.Listener(on_press=on_press)
listener.start()

print("按下 's' 键开始语音转换，按下 'e' 键结束录音我将回答你的问题，按下 'q' 键退出程序。")

try:
    while not exit_flag:
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    listener.stop()
    print("程序已退出")

