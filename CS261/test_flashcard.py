from flashcard import Flashcard as fc
from deck import Deck as d

def my_fc():
    return fc('front', 'back')

def my_d():
    return d([fc(1,1), fc(2,2)])

def test_fc_init_get_set(my_fc = my_fc()):
    assert my_fc.get_front_text() == 'front'
    assert my_fc.get_back_text() == 'back'
    my_fc.set_front_text('newfront')
    my_fc.set_back_text('newback')
    assert my_fc.get_front_text() == 'newfront'
    assert my_fc.get_back_text() == 'newback'

def test_fc_facing_correct_side(my_fc = my_fc()):
    assert my_fc.is_facing_front()
    my_fc.switch_side()
    assert not my_fc.is_facing_front()

def test_fc_init_typecasting_front_back_texts_to_str():
    try:
        first_fc = fc(1, True)
    except:
        assert 1 == 0
    
    try:
        second_fc = fc(fc(), fc())
    except:
        pass

def test_d_init_get_set(my_d = my_d()):
    assert len(my_d.get_flashcards()) == 2
    assert my_d.get_children() == None
    new_d = d()