import string

def load_txt(path):
    with open(path, mode='r') as f:
        return f.readlines()


def remove_punctuation(s):
    return s.translate(None, string.punctuation)

def word2idx(path):
    word2idx = {'START': 0, 'END': 1}
    current_idx = 2
    sentences = []
    for line in open(path):
        line = line.strip()
        if line:
            tokens = remove_punctuation(line.lower()).split()
            sentence = []
            for t in tokens:
                if t not in word2idx:
                    word2idx[t] = current_idx
                    current_idx += 1
                idx = word2idx[t]
                sentence.append(idx)
            sentences.append(sentence)
    return sentences, word2idx