""" 
This module translates between french and english
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    #write the code here
    """ 
    This method translates from english to french
    """
    french_text = MyMemoryTranslator(source = 'english', target = 'french').translate(english_text)
    return french_text


def french_to_english(french_text):
    #write the code here
    """ 
    This method translates from french to english
    """
    english_text = MyMemoryTranslator(source = 'french', target = 'english').translate(french_text)
    return english_text
