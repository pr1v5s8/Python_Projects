import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want me to speak (or type 'q' to quit) : ")
        if x == 'q':
            break
        engine.say(x)
        engine.runAndWait()