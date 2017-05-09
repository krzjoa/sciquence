from sklearn.base import BaseEstimator, ClassifierMixin
from cy_shapelet import optimal_split_point, subseq_dist_ea, calculate_ig
import numpy as np
from operator import add
import sys


class ShapeletClassifier(BaseEstimator, ClassifierMixin):

    '''

    Shapelet classifier. Simple version of this classifier is
    suitable for binary classification problems.

    Parameters
    ----------
    min_size: int
        Mininal shapelet length
    max_size: int
        Maximal shapelet length
    step: int
        Window size step when looking for potential shapelets
    shapelet_class: int, default None
        If not None, classifier takes only cadidate shapelets
        from one class

    References
    ----------

    Ye L., Keogh E. (2009).

    Time Series Shapelets: A New Primitive for Data Mining

    http://alumni.cs.ucr.edu/~lexiangy/Shapelet/kdd2009shapelet.pdf

    '''

    def __init__(self, min_len=10, max_len=100, step=10,
                 n_random=5, shapelet_class=None, metric='cosine'):
        self.min_len = min_len
        self.max_len = max_len
        self.step = step
        self.bsf_shapelet = None
        self.decision_threshold = 0.
        self.bsf_ig = 0.
        self.shapelet_class = shapelet_class

        # Class counts
        self.n_positive = 0
        self.n_negative = 1

        # Number of randomly chosen elements in
        self.n_random = n_random
        self.metric = metric


    def fit(self, X, y):
        '''

        Fit shapelet-based classifier

        Parameters
        ----------
        X: list of ndarray
            List of time seriries
        y: ndarray
            Array of

        Returns
        -------
        self: ShapeletClassifier
            Returns self

        '''

        # Count classes
        self.n_negative = reduce(add, [1 for sample in y if sample == 0])
        self.n_positive = reduce(add, [1 for sample in y if sample == 1])

        # Finding best-so-far shapelet
        for candidate in shgen(X, y, min_len=self.min_len, max_len=self.max_len,
                               step=self.step, one_label=self.shapelet_class, show_progress=True):

            gain, threshold = self._check_cadidate_prune(X, y, candidate)
            #print gain, self.bsf_ig, threshold

            if gain > self.bsf_ig:
                self.bsf_ig = gain
                self.bsf_shapelet = candidate
                self.decision_threshold = threshold

        return self


    def predict(self, X):
        '''

        Predict labels for new list of unseen time series

        Parameters
        ----------
        X: list of ndarray
            List of time series

        Returns
        -------
        predictions: ndarray
            Array of predictions

        '''

        predictions = []

        for sample in X:

            dist, best = subseq_dist_ea(sample, self.bsf_shapelet, metric=self.metric)

            #print dist

            # Decision
            if dist < self.decision_threshold:
                predictions.append(0)
            else:
                predictions.append(1)

        return np.array(predictions)


    def _check_cadidate_prune(self, X, y, candidate):
        '''

        Check shapelet candidate with early entropy prune

        Parameters
        ----------
        X: list of ndarray
            List of time series
        y: ndarray
            Time series labels
        candidate: ndarray
            Potential shapelet

        Returns
        -------
        information_gain: float
            Information gain

        '''

        y = list(y)
        objects = []



        # Get randomly chosen objects to check an optimistic example
        indices = random_pick(y, self.n_random)

        for i in indices:
            dist, best_seq = subseq_dist_ea(X[i], candidate, metric=self.metric)
            objects.append({'value': dist,
                            0: 1 if not y[i] else 0,
                            1: 1 if y[i] else 0})


        # Calculations with entropy early prune

        for ts, label, idx in zip(X, y, range(len(X))):

            positive_rest = {
                'value': np.finfo(float).max,
                0: 0,
                1: self.n_positive - self.n_random
            }
            negative_rest = {
                'value': 0,
                0: self.n_negative - self.n_random,
                1: 0}

            ig, sp = calculate_ig([positive_rest]+objects)
            if ig < self.bsf_ig:
                break

            ig, sp = calculate_ig(objects+[negative_rest])
            if ig < self.bsf_ig:
                break

            dist, best_seq = subseq_dist_ea(ts, candidate, metric=self.metric)
            objects.append({'value': dist,
                            0: 1 if not label else 0,
                            1: 1 if label else 0 })

            if label:
                self.n_positive -= 1
            else:
                self.n_negative -= 1

        info_gain, osp = calculate_ig(objects)
        return info_gain, osp


    def _check_candidate(self, X, y, candidate):
        '''

        Check shapelet candidate

        Parameters
        ----------
        X: list of ndarray
            List of time series
        y: ndarray
            Time series labels
        candidate: ndarray
            Potential shapelet

        Returns
        -------
        information_gain: float
            Information gain

        '''

        objects = []

        for ts, label, idx in (X, y, range(len(X))):
            dist = subseq_dist_ea(ts, candidate)
            objects.append((label, idx, dist))

        return calculate_ig(objects)



# Shapelet generator
def shgen(X, y, min_len, max_len, step=1,
          one_label=None, show_progress=False):
    '''

    Generator yielding all the subsequences
    from all the time series of given
    length between min_len and max_len

    Parameters
    ----------
    X: list of ndarray
        List of time series
    min_len: int
        Min length of subsequence
    max_len: int
        Max length of subsequence
    step: int
        Step of subsequence length

    Yields
    ------
    subsequence: ndarray
        A subsequence of a time series from X set

    '''
    for ln in xrange(min_len, max_len+1, step):
        print "Checking len", ln
        # progress = 0
        for ts, label in zip(X, y):
            # if show_progress:
            #     update_progress(progress, len(X))
            show_progress += 1
            if one_label is not None and label == one_label:
                for i in xrange(0, len(X)):
                    yield ts[i:i+ln]





def random_pick(y, n_samples_per_class=5):
    '''

    Pick randomly indices in binary classification

    Parameters
    ----------
    y: ndarray
        List of labels
    n_samples_per_class: int
        Number of samples per class

    Returns
    -------
    random_indices: list
        List of randomly picked indices

    '''
    positive = []
    negative = []

    while len(positive) != n_samples_per_class and len(negative) != n_samples_per_class:
        random_idex = np.random.randint(0, len(y))

        if y[random_idex] == 0 and len(negative) < n_samples_per_class:
            negative.append(y[random_idex])

        if y[random_idex] == 0 and len(positive) < n_samples_per_class:
            positive.append(y[random_idex])

    return positive + negative


def update_progress(progress, total_num=10):
    print progress / total_num
    sys.stdout.write('\r[{0}] {1}%'.format('#'*(progress/total_num), progress))