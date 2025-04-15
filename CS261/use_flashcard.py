# ============
# Demo Function
# ============

from flashcard import Flashcard

def use_flashcard(fc: Flashcard):
    front_text, back_text, facing_front = fc.get_front_text(), fc.get_back_text(), fc.is_facing_front()
    if facing_front:
        shown_side, hidden_side = front_text, back_text 
    else:
        shown_side, hidden_side = back_text, front_text
        
    guess = input(f"\n=== FLASHERRR ===\nPrompt: {shown_side}\nGuess: ")
    fc.switch_side()
    fc.score(guess == hidden_side)
    if guess == hidden_side:
        print("Correct!")
    else:
        input(f"Incorrect. The answer was '{hidden_side}'.\nPress ENTER to Continue.")
    

