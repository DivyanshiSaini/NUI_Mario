import speech_recognition as sr
import pyautogui
import time

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
    print("Sorry, I couldn't understand what you said.")
except sr.RequestError as e:
    print("Sorry, could not request results from Google Speech Recognition service".format(e))

# Map speech to keyboard commands
if "jump" in speech:
    pyautogui.press("up")
elif "down" in speech:
    pyautogui.press("down")
elif "up" in speech:
    pyautogui.press("up")
elif "left" in speech:
    pyautogui.keyDown("left")
    time.sleep(1)
    pyautogui.keyUp("left")
elif "right" in speech:
    pyautogui.keyDown("right")
    time.sleep(1)
    pyautogui.keyUp("right")
elif "select" in speech:
    pyautogui.press("enter")
elif "enter" in speech:
    pyautogui.press("enter")
elif "esc" in speech:
    pyautogui.press("esc")
else:
    print("Sorry, I didn't recognize that command.")