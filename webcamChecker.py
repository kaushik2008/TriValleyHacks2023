'''Imports'''
import cv2
from datetime import datetime
from fer import FER
from tkinter import *
# print('earliest hehe')
def process():
    '''Takes webcam and gives a livestream of processed images'''
    cam = cv2.VideoCapture(0)
    i = 0
    emotion_detector = FER()
    while True:
        # print('Before hehe')
        '''Checks each frame of the webcame'''
        a = datetime.now()
        ret, frame = cam.read()
        if ret:
            # print('hehe')
            '''Checks if frame exists'''
            detector= emotion_detector.detect_emotions(frame)
            if len(detector) == 0:
                '''Checks if faces are in frame, if not, output input frame'''
                newFrame = frame
            else:
                for rawOutput in detector:
                    '''Processes each face seperatly'''
                    highest = []
                    newFrame = None
                    '''Makes box around image'''
                    bounding_box = rawOutput['box']
                    newFrame = cv2.rectangle(frame,(bounding_box[0], bounding_box[1]),(bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]), (0, 155, 255), 2,)
                    '''Finds most dominant image and labels it to the box'''
                    emotions = rawOutput['emotions']
                    for label in emotions:
                        '''Checks for highest percentage value'''
                        if len(highest) == 0:
                            highest.append(label)
                        elif emotions[highest[0]] < emotions[label]:
                            highest = []
                            highest.append(label)
                        elif emotions[highest[0]] == emotions[label]:
                            highest.append(label)
                    output = ''
                    i = 1
                    for item in highest:
                        '''Writes label'''
                        if i == 1:
                            output = item
                        else:
                            output = output + '-' + item
                    newFrame = cv2.putText(newFrame, output, (bounding_box[0], bounding_box[1]+bounding_box[3]+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 155, 255), 2)
            '''Makes image screenwidth'''
            tkMod = Tk()
            screenwidth = tkMod.winfo_screenwidth()
            screenheight = tkMod.winfo_screenheight()
            cv2.resize(newFrame, (screenwidth, screenheight))
            cv2.imshow('Face Emotion Detection', newFrame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                exit()

if __name__ == '__main__':
    process()