import speech_recognition as sr
import pyautogui

r = sr.Recognizer()
mic = sr.Microphone()

# Listen for speech and recognize it
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
try:
    speech = r.recognize_google(audio)
    print("Speech:", speech)
except sr.UnknownValueError:
    print("Speech recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Map speech to keyboard commands
if "jump" in speech:
    pyautogui.press("up")
elif "down" in speech:
    pyautogui.keyDown("down")
elif "up" in speech:
    pyautogui.press("up")
elif "left" in speech:
    pyautogui.keyDown("left")
elif "right" in speech:
    pyautogui.keyDown("right")
elif "select" in speech:
    pyautogui.keyDown("enter")
elif "enter" in speech:
    pyautogui.keyDown("enter")
elif "esc" in speech:
    pyautogui.keyDown("esc")
else:
    pyautogui.keyUp("down")