# -*- coding: utf-8 -*-
# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Word Encoder
# Author: Krzysztof Joachimiak
#
# License: MIT

import string


# TODO: remove with
def load_txt(path):
    '''

    Load text file

    Parameters
    ----------
    path: str
        Path to text file

    Returns
    -------
    f: file
        Text file

    '''
    with open(path, mode='r') as f:
        return f



def remove_punctuation(text):
    return text.translate(None, string.punctuation)


def txt_to_lines(path):

    text = open(path, mode='r')
    lines = [remove_punctuation(l.lower()).split()
             for l in text.readlines()]
    return lines


def text_pipe(path):
    from word_encoder import Word2Idx
    word2idx = Word2Idx()

    text = txt_to_lines("../../data/frost.txt")
    text = word2idx.fit_transform(text)

    return text, word2idx


if __name__ == "__main__":
    frost, w2i = text_pipe("../../data/frost.txt")

    import pdb
    pdb.set_trace()







