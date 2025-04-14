from __future__ import annotations
from flashcard import Flashcard

class Deck:
    def __init__(self, flashcards: list[Flashcard] | None = [], children: list[Deck] | None = [], parent: Deck | None = None):
        """
        Initializes the Deck object which manages inter-deck connections and flashcard pointers.

        Parameters:
            flashcards: list[Flashcard] | None which provides the initial flashcards in the deck. Default is the empty list `[]`. Can be any value, but only list[Flashcard] type will retain information.
            children: list[Deck] | None providing decks which will become children of this deck. Default is the empty list `[]`. Can be any value, but only list[Deck] type will retain information.
            parent: Deck representing the deck which will be the parent of this deck. Default is `None`. Can be any value, but only Deck type will retain information. 

        Raises:
            None
        """
        if not isinstance(parent, Deck): self._parent = None
        else: self._parent = parent

        if not isinstance(children, list): self._children = []
        else: self._children = [x for x in children if isinstance(x, Deck)]
        for child in self._children:
            child.change_parent(self)

        if not isinstance(flashcards, list): self._flashcards = []
        else: self._flashcards = [x for x in flashcards if isinstance(x, Flashcard)]
    
    # Inter-Deck Management
    def get_children(self) -> list[Deck]:
        return self._children
    
    def add_child(self, child: Deck) -> None:
        if not isinstance(child, Deck): raise ValueError("Input must be a Deck.")
        if child in self.get_children(): raise ValueError('Child is already in Deck')
        self._children.append(child)
        child._parent = self
    
    def remove_child(self, child: Deck, keep_grandchilds: bool = True) -> None:
        if child in self._children: self._children.remove(child)
        else: raise ValueError("Input is not a Child in this Deck.")
        
        if len(child.get_children()) != 0:
            if keep_grandchilds:
                child_children = child.get_children()
                for c in child_children:
                    c.change_parent(self)
    
    def get_parent(self) -> Deck:
        return self._parent
    
    def change_parent(self, new_parent: Deck | None = None) -> None:
        if not isinstance(new_parent, Deck) and new_parent != None: raise ValueError("Input must be a List")
        try: self._parent._children.remove(self)
        except: pass
        new_parent.add_child(self)
        


    # Intra-Deck Management

    def get_flashcards(self) -> list[Flashcard]:
        return self._flashcards
    
    def add_flashcard(self, flashcard: Flashcard) -> None:
        if isinstance(flashcard, Flashcard): self._flashcards.append(flashcard)
        else: raise ValueError("Input must be a Flashcard.")

    def remove_flashcard(self, flashcard: Flashcard) -> None:
        if isinstance(flashcard, Flashcard): self._flashcards.remove(flashcard)
        else: raise ValueError("Input must be a Flashcard.")

    def change_deck(self, flashcard: Flashcard, new_deck: Deck) -> None:
        if not isinstance(flashcard, Flashcard):
            raise ValueError("\"Flashcard\" Input must be a Flashcard")
        if not isinstance(new_deck, Deck):
            raise ValueError("\"new_deck\" Input must be a Deck")
        self.remove_flashcard(flashcard)
        new_deck.add_flashcard(flashcard)
    
    def delete_deck(self) -> None:
        parent = self._parent
        try: parent.remove_child(self)
        except: pass
        for child in self.get_children():
            child._parent = None
        del self

    
