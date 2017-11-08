from cutting import seq, specseq, nseq, pseq, seqi, pseqi, nseqi, specseqi, chunk
from input import rnn_input, seq2seq_input
from cy_searching import mslc, longest_segment, max_avg_seq
from sampling import random_slice
from sorting import parallel_sort
from comparision import lseq_equal, shapes_equal, size_equal
#from cy_searchning2 import max_seq



__all__ = [
           # Cutting
           'seq',
           'specseq',
           'nseq',
           'pseq',
           'seqi',
           'pseqi',
           'nseqi',
           'specseqi'

           # Splitting into chunks
            'chunk',

           # Input transforming
           #  'rnn_input',
           #  'seq2seq_input',

            # Sampling

            # Sorting
            'parallel_sort',

           # Searching functions
           'mslc',
           'longest_segment',
           'max_avg_seq',
           #'max_seq'

           # Comparisions
            'lseq_equal',
            'shapes_equal',
            'size_equal'

           ]