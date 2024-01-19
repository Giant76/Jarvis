import speech_recognition as sr
import os
import sys
import pyttsx3

recognizer = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def run_script(script_name, script_folder="/home/vboxuser/Documents"):
    script_path = os.path.join(script_folder, script_name)
    try:
        os.system(f"bash {script_path}")
    except Exception as e:
        print(f"Error executing script: {e}")
        speak("Error executing script.")


def main():
    activation_word = "computer"
    exit_word = "exit"

    speak("Hey Kevin, how may I assist you...")
    print("Listening for activation word...")
    speak("Listening for activation word..")

    while True:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.3)
            audio = recognizer.listen(mic)

        try:
            text = recognizer.recognize_google(audio).lower()

            if activation_word in text:
                print("Activation word detected. Listening for script keywords...")
                speak('Activation word heard...')
                speak('listening for keywords')

                while True:
                    with sr.Microphone() as mic_script:
                        recognizer.adjust_for_ambient_noise(mic_script, duration=0.3)
                        audio_script = recognizer.listen(mic_script)

                    try:
                        script_keyword = recognizer.recognize_google(audio_script).lower()
                        print(f"Script Keyword: {script_keyword}")

                        if "run report" in script_keyword:
                            run_script('report.sh')
                            print('running reports...')
                            speak("your report is ready..")
                        elif "run backup" in script_keyword:
                             run_script('backup.sh', 'home/vboxuser/Documents/Machine')
                             print('Backing up....')
                             speak('backing data')
                        elif "run update" in script_keyword:
                            run_script('update.sh', 'home/vboxuser/Documents/Machine')
                            print('updating.........')
                            speak('this may take a moment')
                    
                        elif exit_word in script_keyword:
                            print("Exiting...")
                            speak("Goodbye Kevin..")
                            sys.exit()

                    except sr.UnknownValueError:
                        continue

        except sr.UnknownValueError:
            print("Failed to recognize activation word.")
            speak("Sorry, try again...")

if __name__ == "__main__":
    main()

