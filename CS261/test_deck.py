from flashcard import Flashcard as fc
from deck import Deck as d

def my_fc():
    return fc('front', 'back')

def my_d():
    return d([fc(1,1), fc(2,2)])

def test_inter_deck_management(my_d = my_d()):
    # test initialize
    new_d1 = d([my_fc()])
    assert my_d.get_children() == []
    assert my_d.get_parent() == None

    #test add one child
    my_d.add_child(new_d1)
    assert my_d.get_children() == [new_d1]
    assert new_d1.get_parent() == my_d

    # test multiple children
    new_d2 = d([my_fc()])
    my_d.add_child(new_d2)
    assert my_d.get_children() == [new_d1, new_d2]
    assert new_d2.get_parent() == my_d


    # test add one child to a child
    new_d3 = d([my_fc()])
    new_d2.add_child(new_d3)
    assert new_d1.get_children() == []
    assert new_d2.get_children() == [new_d3]
    assert new_d3.get_parent() == new_d2

    # test move deck w/o child
    new_d3.change_parent(new_d1)
    assert new_d1.get_children() == [new_d3]
    assert new_d2.get_children() == []
    assert new_d3.get_parent() == new_d1

    # test move deck w/child
    new_d1.change_parent(new_d2)
    assert my_d.get_children() == [new_d2]
    assert new_d2.get_children() == [new_d1]
    assert new_d1.get_children() == [new_d3]

    # test remove w/o child
    new_d1.remove_child(new_d3)
    assert my_d.get_children() == [new_d2]
    assert new_d2.get_children() == [new_d1]
    assert new_d1.get_children() == []
    new_d1.add_child(new_d3)
    assert new_d1.get_children() == [new_d3]

    # test remove w/child keep_grandchild = True
    my_d.remove_child(new_d2, keep_grandchilds=True)
    assert my_d.get_children() == [new_d1]
    assert new_d2.get_children() == []
    assert new_d1.get_children() == [new_d3]

    # test remove w/child keep_grandchild = False
    new_d4 = d([my_fc()])
    new_d5 = d([my_fc()])
    new_d3.add_child(new_d4)
    new_d4.add_child(new_d5)
    new_d1.remove_child(new_d3, keep_grandchilds=False)
    assert my_d.get_children() == [new_d1]
    assert new_d1.get_children() == []

def test_intra_deck_management(my_fc = my_fc()):
    # initialize deck with flashcard
    deck = d()
    assert deck.get_flashcards() == []
    fc_1 = fc()
    deck.add_flashcard(fc_1)
    assert deck.get_flashcards() == [fc_1]
    
    # add multiple flashcard
    fc_2, fc_3, fc_4 = fc(), fc(), fc()
    deck.add_flashcard(fc_2)
    deck.add_flashcard(fc_3)
    deck.add_flashcard(fc_4)
    assert deck.get_flashcards() == [fc_1, fc_2, fc_3, fc_4]

    # move flashcard to new deck
    new_deck = d()
    deck.change_deck(fc_2, new_deck)
    assert new_deck.get_flashcards() == [fc_2]
    assert deck.get_flashcards() == [fc_1, fc_3, fc_4]

def 