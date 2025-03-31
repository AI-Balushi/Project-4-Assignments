SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my "  # Beginning of the sentence

def main():
    """
    Prompts the user for an adjective, noun, and verb, then prints a fun sentence.
    """
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Construct and display the Mad Libs style sentence
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# Program starts here
if __name__ == '__main__':
    main()