import string


def strip_text(data):
    """Returns a cleaned (stripped of punctuation) text

    Args:
        data (str): String to be stripped

    Returns:
        cleaned_text (str): Input string, lower-cased and stripped of punctuation"""
    cleaned_text = ''
    data_words = data.split()

    for word in data_words:
        clean_word = ''

        for count, character in enumerate(word):

            if character in string.punctuation:
                continue

            clean_word += character.lower()

        cleaned_text += ' ' + clean_word

    return cleaned_text
