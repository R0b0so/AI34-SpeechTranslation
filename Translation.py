from googletrans import Translator; import speech_recognition as sr; import pyttsx3;

def speak(text,language="en"):
    engine=pyttsx3.init()
    engine.setProperty("rate",150)
    voices = engine.getProperty("voices")

    if language == "en":
        engine.setProperty("voice",voices[0].id)
    else:
        engine.setProperty("voice",voices[1].id)

    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("please speak in english")
        audio = recognizer.listen(source)
    
    try:
        print("recognizing speech")
        text = recognizer.recognize_google(audio,language="en-US")
        print("you said: ", text)
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print("API error", e)
    return ""

def translating_text(text,target_language="es"):
    translator = Translator()
    translation=translator.translate(text,dest=target_language)
    print("translated text", translation.text)
    return translation.text

def display_language_options():
    print("availible translation languages: ")
    print("1. Hindi (hi) \n 2. Tamil (ta) \n 3. Telugu (te)")

    choice = input("please select target language ")
    language_dict = {
        "1":"hi",
        "2":"ta",
        "3":"te",
        "hindi":"hi",
        "tamil":"ta",
        "telugu":"te"
    }

    return language_dict.get(choice.lower(),"es")

def main():
    target_language = display_language_options()
    original_text = speech_to_text()
    if original_text:
        translate_text = translating_text(original_text,target_language=target_language)
        speak(translate_text,language="en")
        print("translation spoken out")
if __name__=="__main__":
    main()
