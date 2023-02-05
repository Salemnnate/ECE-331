"""This is the beginning of the program"""
import speech_recognition as sr

def take():
    """This function is where most of the work is done"""
    recognizer = sr.Recognizer()

    # Added an audio file of my own here.
    audio_file = sr.AudioFile('main_recog.wav')

    # For audio files
    with audio_file as source:
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        print("Recognizing your speech...")
        audio = recognizer.record(source)

    try:
        result = recognizer.recognize_google(audio, language='en-US')
        print("\n")
        print(result)

    except sr.UnknownValueError as error:
        print("An error occurred. Please enable internet connection")
        print("Error: ", error)
        return None

    except sr.RequestError as error:
        print("An error occurred. Please enable internet connection")
        print("Error: ", error)
        return None

    return result


query = take()
print("Quitting the program now")
