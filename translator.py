from dictionary import words_list
import pyttsx3
text_speech = pyttsx3.init()

def nyk_eng_translator(nyk):
    nyk = nyk.lower()

    # Check if any part of user's input matches a key in words_list_two
    matched_word = next((word for word in words_list.keys() if word in nyk), None)
      

    if matched_word:
        print(f'==> {words_list.get(matched_word)}')

        #converting text to speech
        answer = words_list.get(matched_word)
        text_speech.say(answer)
        text_speech.runAndWait()

    else:
        print("I'm sorry, I couldn't understand that.")

def main():
    while True:
        # Taking input from the user
        user_talk = input("Andika kinyakyusa (type 'exit' to quit): ")

        if user_talk.lower() == "exit":
            print("Asante! Kwaheri!")
            break  # Exit the loop if the user types 'exit'

        nyk_eng_translator(user_talk)


if __name__ == "__main__":
    main()
