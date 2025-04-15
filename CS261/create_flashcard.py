# ============
# Demo Function
# ============

from flashcard import Flashcard

def create_flashcard():
    input_check = True
    while input_check:
        inputs = input("Please input the front-text and back-text in one line, separated by the key phrase '//'\nExample: > front-text//back-text\n    > ").strip().split("//")
        try:
            front, back = inputs
            input_check = False
        except:
            print('\nThat did not work. Please try again.')
    fc = Flashcard(front, back)
    return fc