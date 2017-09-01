import sqlite3
import string
import tensorflow as tf


"""
Grab data
"""
def get_words():
    #Assumes database is in top level data directory
    con = sqlite3.connect('./data/database.sqlite')
    con.row_factory = lambda cursor, row: row[0]
    con.text_factory = str

    reviews = con.execute('SELECT Text FROM Reviews').fetchall()
    words = []
    for review in reviews:
        for word in review.split():
            words.append(word.translate(None, string.punctuation))
                
    return words

"""
Give most common (<=n_words) words unique IDs, 
"""
def build_dataset(words, n_words):
    """Process raw inputs into a dataset."""
    count = [['UNK', -1]]
    count.extend(collections.Counter(words).most_common(n_words - 1))
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)
    data = list()
    unk_count = 0
    for word in words:
        if word in dictionary:
            index = dictionary[word]
        else:
            index = 0  # dictionary['UNK']
            unk_count += 1
        data.append(index)
    count[0][1] = unk_count
    reversed_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    return data, count, dictionary, reversed_dictionary

