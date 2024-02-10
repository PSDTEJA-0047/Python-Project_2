def count_words(sentence):
    words = sentence.split()
    return len(words)
def main():
    print("Can i help to count the words?")
    user_input = input("Type here: ")
    if not user_input:
        print("Error: You didn't enter anything.")
        return
    word_count = count_words(user_input)
    print(f"Word count: {word_count}")
if __name__ == "__main__":
    main()
