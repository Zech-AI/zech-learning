import random

def create_flashcards():
    flashcards = {}
    while True:
        term = input("Enter a term (or type 'exit' to finish): ").strip()
        if term.lower() == 'exit':
            break
        definition = input("Enter the definition: ").strip()
        flashcards[term] = definition
    return flashcards

def review_flashcards(flashcards):
    terms = list(flashcards.keys())
    random.shuffle(terms)
    for term in terms:
        input("Press Enter to reveal the definition of '{}': ".format(term))
        print(flashcards[term])

def main():
    print("Welcome to Flashcard Creator!")
    flashcards = create_flashcards()
    print("\n--- Flashcards Created ---\n")
    review_flashcards(flashcards)
    print("\n--- End of Flashcards ---")

if __name__ == "__main__":
    main()
