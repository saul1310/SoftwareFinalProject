# ============
# Demo Function
# ============

from create_flashcard import create_flashcard
from use_flashcard import use_flashcard

def main():
    fcs = [create_flashcard() for i in range(4)]
    for fc in fcs:
        use_flashcard(fc)

if __name__ == "__main__":
    main()