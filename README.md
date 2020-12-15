# Build-Google-Assistant-in-Python

**Install below packages**

- pip install SpeechRecognition - For the robot to listen to our voice/speech

- pip install pyttsx3 - To speak out, or text to speech 

- pip install pywhatkit - For advance control on browser 

- pip install wikipedia - To get wikipedia data

- pip install pyjokes - To get funny jokes 

- pip install PyAudio 


If you come across any issues regarding pyaudio or Text to speech module, please go through below solution. 

error: failed building wheel for pyaudio

if you are getting above error then try below steps on windows

1. open command prompt.
2. pip install pipwin (then press enter)
3. pipwin install pyaudio (press enter)

if Text to speech (pyttsx3) module is not working on windows 10 then install the older version of pyttsx3.

python -m pip install pyttsx3==2.71 

(Run the above code in terminal. It will uninstall current version and then it installs the older version.)
