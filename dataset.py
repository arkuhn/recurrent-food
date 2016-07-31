import re
import numpy as np
import csv

def get_text():
    with open('Reviews.csv', 'rb') as csvfile:
        text_crawler = csv.reader(csvfile)
        text = ''
        headers = False
        for  row in text_crawler:
            if not headers:
                headers = True
                continue
            parsed_text = re.sub('<br />', ' ', row[9])
            parsed_text = re.sub('<a href="', 'Link:', parsed_text)
            parsed_text = re.sub('</a>', ' ', parsed_text)
            parsed_text = re.sub('>', '-', parsed_text)
            text = text + parsed_text

        text = list(text)
        for i in range(len(text)):
            text[i] = ord(text[i])
    return np.asarray(text).astype(np.float32, copy=False)
