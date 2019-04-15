import re


def add_stop_symbol(word_list):
    for index, word in enumerate(word_list):
        if re.match(r"[.!?]+(\")*", word):
            word_list[index] = '<s>'
            word_list.insert(index, '</s>')
    word_list.insert(0, word_list.pop())
    return word_list


def design_text(text):
    text = text.replace(',', ' ')
    text = text.replace('/', ' ')
    text = text.replace('(', ' ')
    text = text.replace(')', ' ')
    text = text.replace('.', ' ')
    text = text.replace(':', ' ')
    text = text.replace(';', ' ')
    text = text.replace('...', ' ')
    text = text.replace('New York', 'Newyork')
    text = text.replace('United States of America', 'United-States-of-America')
    # Convert text string to a list of words
    return re.split('[^A-Za-z]+', text.lower())