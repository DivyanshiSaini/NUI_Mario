import pygame
from pygame.locals import *
import sys
import speech_recognition as sr
import pyautogui
import time

global r
global mic
r = sr.Recognizer()
mic = sr.Microphone()

class Input:
    
    def __init__(self, entity):
        self.mouseX = 0
        self.mouseY = 0
        self.entity = entity

    def checkForInput(self):
        events = pygame.event.get()
        self.checkForKeyboardInput()
        self.checkForMouseInput(events)
        self.checkForQuitAndRestartInputEvents(events)
        
    def checkForVoiceInput(self):
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
            
        if "left" in speech:
            self.entity.traits["goTrait"].direction = -1
        if "right" in speech:
            self.entity.traits["goTrait"].direction = 1
        if "up" in speech or "jump" in speech:
            self.entity.traits['jumpTrait'].jump(True)
        if "select" in speech or "enter" in speech:
            pyautogui.press("enter")
        if "escape" in speech:
            pyautogui.press("esc")
        else:
            print("Sorry, I didn't recognize that command")
        

    def checkForKeyboardInput(self):
        pressedKeys = pygame.key.get_pressed()

        if pressedKeys[K_LEFT] or pressedKeys[K_h] and not pressedKeys[K_RIGHT]:
            self.entity.traits["goTrait"].direction = -1
        elif pressedKeys[K_RIGHT] or pressedKeys[K_l] and not pressedKeys[K_LEFT]:
            self.entity.traits["goTrait"].direction = 1
        else:
            self.entity.traits['goTrait'].direction = 0

        isJumping = pressedKeys[K_SPACE] or pressedKeys[K_UP] or pressedKeys[K_k]
        self.entity.traits['jumpTrait'].jump(isJumping)

        self.entity.traits['goTrait'].boost = pressedKeys[K_LSHIFT]

    def checkForMouseInput(self,events):
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.isRightMouseButtonPressed(events):
            self.entity.levelObj.addKoopa(
                mouseY / 32, mouseX / 32 - self.entity.camera.pos.x
            )
            self.entity.levelObj.addGoomba(
                mouseY / 32, mouseX / 32 - self.entity.camera.pos.x
            )
        if self.isLeftMouseButtonPressed(events):
            self.entity.levelObj.addCoin(
                mouseX / 32 - self.entity.camera.pos.x, mouseY / 32
            )

    def checkForQuitAndRestartInputEvents(self,events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and \
                (event.key == pygame.K_ESCAPE or event.key == pygame.K_F5):
                self.entity.pause = True
                self.entity.pauseObj.createBackgroundBlur()

    def isLeftMouseButtonPressed(self, events):
        return self.checkMouse(events,1)



    def isRightMouseButtonPressed(self, events):
        return self.checkMouse(events,3)


    def checkMouse(self, events, button):
        for e in events:
                if e.type == pygame.MOUSEBUTTONUP:
                    if e.button == button:
                       return True
        else:
                       return False


