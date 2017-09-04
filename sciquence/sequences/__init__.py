from sequences_utils import seq, specseq, nseq, pseq, seqi, pseqi, nseqi, lseq_equal, chunk
from input import rnn_input, seq2seq_input
from cy_searching import mslc, longest_segment, max_avg_seq
from sorting import parallel_sort
#from comparision import lseq_equal #, shapes_equal, size_equal
#from cy_searchning2 import max_seq



__all__ = [
           # Trimming & cutting
           'seq',
           'specseq',
           'nseq',
           'pseq',
           'seqi',
           'pseqi',
           'nseqi',

           # Splitting into chunks
            'chunk',

           # Input transforming
            'rnn_input',
            'seq2seq_input',

            # Sorting
            'parallel_sort',

           # Searching functions
           'mslc',
           'longest_segment',
           'max_avg_seq',
           #'max_seq'

           # Comparisions
            #'lseq_equal',
            #'shapes_equal',
            #'size_equal'

           ]