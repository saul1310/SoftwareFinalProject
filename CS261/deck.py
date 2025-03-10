from __future__ import annotations
from flashcard import Flashcard

class Deck:
    def __init__(self, flashcards: list[Flashcard] | list = None, children: list[Deck] | list = None):
        if not isinstance(children, list):
            self._children = []
        else:
            self._children = [x for x in children if isinstance(x, Deck)]

        if not isinstance(flashcards, list):
            self._flashcards = []
        else:
            self._flashcards = [x for x in flashcards if isinstance(x, Flashcard)]
    

    def get_children(self):
        return self._parent
    
    def add_child(self, child: Deck):
        if isinstance(child, Deck): self._children.append(child)
        else: raise ValueError("Input must be a Deck.")
    
    def remove_child(self, child: Deck):
        if child in self._children: self._children.remove(child)
        else: raise ValueError("Input is not a valid Child.")

    def add_flashcard(self, flashcard: Flashcard):
        if isinstance(flashcard, Flashcard): self._flashcards.append(flashcard)
        else: raise ValueError("Input must be a Flashcard.")

    def get_flashcards(self):
        return self._flashcards
    
