from __future__ import annotations

# Need to replace all Error Raises with reroutes to prevent crashing on user-end. 
# They are in place for the time being for testing purposes.

class Flashcard:
    def __init__(self, front_text: str = "", back_text: str = "", facing_front: bool = True):
        """
        Initializes the Flashcard object which holds internal flashcard data.

        Parameters:
            front_text: String representing the text which will be displayed on the front side of the card. Default is `""`. Can be any value which can be cast to a String.
            back_text: String representing the text which will be displayed on the back side of the card. Default is `""`. Can be any value which can be cast to a String.
            facing_front: Boolean representing what side is facing the user. Default is `True`, meaning that the front side is facing the user. 

        Raises:
            ValueError: if `front_text` is not castable to a String.
            ValueError: if `back_text` is not castable to a String.
            ValueError: if `facing_front` is not a Boolean. 
        """
        try:
            self._front_text = str(front_text)
        except:
            raise ValueError("Input must be castable to a String.")
        try:
            self._back_text = str(back_text)
        except:
            raise ValueError("Input must be castable to a String.")
        if isinstance(facing_front, bool): self._facing_front = facing_front
        else: raise ValueError("Input must be a Boolean.")
    
    def get_front_text(self):
        """
        Returns the `front_text` string.
        """
        return self._front_text
    
    def set_front_text(self, new_text: str):
        """
        Replaces the current front_text with the given new_text parameter.

        Arguments:
            new_text: String which represents the new content for the front_text attribute. 
        
        Raises:
            ValueError: if `new_text` is not castable to a String.
        """
        try:
            new_text = str(new_text)
        except:
            raise ValueError("Input must be castable to a String.")
        self._front_text = new_text

    def get_back_text(self):
        """
        Returns the `front_text` string.
        """
        return self._back_text
    
    def set_back_text(self, new_text):
        """
        Replaces the current back_text with the given new_text parameter.

        Arguments:
            new_text: String which represents the new content for the back_text attribute. 
        
        Raises:
            ValueError: if `new_text` is not castable to a String.
        """
        try:
            new_text = str(new_text)
        except:
            raise ValueError("Input must be castable to a String.")
        self._back_text = new_text
    
    def is_facing_front(self):
        return self._facing_front
    
    def switch_side(self):
        self._facing_front = False if self.is_facing_front() else True
