# QR Code Reader for COVID-19
Using a robot powered by Fischertechnik TXT controller.

QR Code Reader for COVID-19
A Python code for Fischertechnik TXT robot with Camera.

The robot will capture an image for QR Code label, and it'll decode it using OpenCV library.

After decoding the QR Code label, it will pronounce the result using [gTTS](https://gtts.readthedocs.io/en/latest/) library in Python.

QR Code labels are generated depending on a two results:

1. **infected** (Its used with COVID-19 infected people)
2. **healthy** (Its used with healthy people)

I used [ftrobopy](https://github.com/ftrobopy/ftrobopy) to connect and control TXT Controller, and the used robot was built using [Robotics Competition Set](https://www.fischertechnik.de/en/products/teaching/stem-robotics/519143-robotics-competition-set) kit from Fischertechnik.

Attached, the test samples of QR labels that are captured by the TXT Camera in the robot. Also, the audio file for a result while testing.

Follow me on [Twitter](https://twitter.com/MeqdadDev), [LinkedIn](https://www.linkedin.com/in/meqdad-darwish/)
