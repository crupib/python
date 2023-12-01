import speach_recognition as sr
speach = sr.Recognizer()
print('Python is listening...')
with sr.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    audio= speach.listen(source)
    inp= speech.recognize_google(audio)
    print(f'YOu just said {inp}.')
