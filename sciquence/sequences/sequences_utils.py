import numpy as np
from itertools import groupby


def seq(array):
    '''

    Cuts input array into sequences consisting of the same elements

    Parameters
    ----------
    array: array-like
        Numpy array

    Returns
    -------
    seq_list: list of array-like
        List of sequences

    '''
    return [np.array(list(group)) for elem, group in groupby(array)]


def nseq(array):
    '''

    Returns sequences

    Parameters
    ----------
    array: array-like
        Numpy array

    Returns
    -------

    '''


def specific_seq(array):
    pass

# def seq_to_ind(sequence, only_true=False):
#     start = 0
#     indices = []
#     for elem in sequence:
#         indices.append(range(start, start + len(elem)))
#         start += len(elem)
#     if only_true:
#         return [seq_ind for seq_ind, seq_item in zip(indices, sequence) if seq_item[0]]
#     else:
#         return indices
#
# # def is_included(item, searched_seq):
# #     for s in searched_seq:
# #         if set(item).issubset(s):
# #             return True
# #     else:
# #         return False
#
#
#
# def get_sequences_tuples(array):
#     return [(elem, np.array(list(group))) for elem, group in groupby(array)]
#
#
#
#
# def get_positive_sequences(array):
#     return [np.array(list(group)) for elem, group in groupby(array) if elem]
#
#
# def get_negative_sequences(array):
#     return [np.array(list(group)) for elem, group in groupby(array) if not elem]


# def get_sequences_indices(array):
#     seq = Sequences.get_sequences(array)
#     indices = []
#     last_index = 0
#     for item in seq:
#         indices.append(range(last_index, last_index + len(item))) last_index+=len(item )
#     return indices
#
#
# def get_positive_sequences_indices(array):
#     seq = Sequences.get_sequences_tuples(array)
#     indices = []
#     last_index = 0
#     for item in seq:
#         if item[0] == 1:
#             indices.append(np.array(range(last_index, last_index + len(item[1]))))
#         last_index+=len( item[1])
#     return indices
