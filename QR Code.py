'''
QR Code Reader for COVID-19
A Python code for Fischertechnik TXT robot with Camera.

The robot will capture an image for QR Code label, and it'll decode it.

After decoding the QR Code label, it will pronounce the result using gTTS library in Python.

QR Code labels are generated depending on a two results:
1- 'infected' (Its used with COVID-19 infected people)
2- 'healthy' (Its used with healthy people)

Done by: Eng. Meqdad Darwish
'''
import cv2 as cv
import ftrobopy
# from PIL import Image
import time
from gtts import gTTS
import os

# txt = ftrobopy.ftrobopy('192.168.1.130', 65000)  # Connecting with TXT Controller using Wlan client mode.
txt = ftrobopy.ftrobopy('192.168.7.2', 65000)  # USB

ultrasonic_sensor = txt.ultrasonic(1)  # I1
stop_condition = False

M1 = txt.motor(1)  # Create a motor object (M1)
M2 = txt.motor(4)  # Create a motor object (M4)
M1.setSpeed(280)  # Set speed
M2.setSpeed(-268)  # Set speed (negative for reversing the direction)
# M1.setDistance(1000) # Set the number of steps
txt.updateWait()

while not stop_condition:
    txt.updateWait()
    distance = ultrasonic_sensor.distance()
    s = "Measured distance: {:5f}".format(distance)
    print(s, end='\r')
    if distance <= 15:
        stop_condition = True
        M1.stop()
        M2.stop()
        print("Stopped")

if stop_condition is True:
    txt.startCameraOnline()
    time.sleep(3)
    im = "TXTimage.jpg"
    pic = txt.getCameraFrame()
    time.sleep(2)

    with open(im, 'wb') as f:
        f.write(bytearray(pic))

    time.sleep(1)
    txt.stopCameraOnline()

    # im = cv2.imread("1.jpg")
    im = cv.imread(im)

    det = cv.QRCodeDetector()

    qr_text, points, straight_qrcode = det.detectAndDecode(im)
    print(qr_text)
    cv.imshow(qr_text, im)
    language = 'en'  # English
    if qr_text == "infected":
        # Run a buzzer
        print("infected")
    elif qr_text == "healthy":
        # Run a Green LED
        print("healthy")
    else:
        print("Unknown")

    text_to_speech = gTTS(text=qr_text, lang=language, slow=False)
    text_to_speech.save("qr_result.mp3")
    os.system("start qr_result.mp3")

    cv.waitKey(0)
