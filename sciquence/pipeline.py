"""
The :mod:`imblearn.pipeline` module implements utilities to build a
composite estimator, as a chain of transforms, samples and estimators.
"""
# Adapted from scikit-learn

# Author: Edouard Duchesnay
#         Gael Varoquaux
#         Virgile Fritsch
#         Alexandre Gramfort
#         Lars Buitinck
#         chkoar
# License: BSD

from __future__ import print_function
from __future__ import division

from warnings import warn

from sklearn.externals import six
from sklearn import pipeline
from sklearn.utils import tosequence
from sklearn.utils.metaestimators import if_delegate_has_method

__all__ = ['Pipeline']


class Pipeline(pipeline.Pipeline):

    """Pipeline of transforms and resamples with a final estimator.

    Sequentially apply a list of transforms, samples and a final estimator.
    Intermediate steps of the pipeline must be transformers or resamplers,
    that is, they must implement fit, transform and sample methods.
    The final estimator only needs to implement fit.

    The purpose of the pipeline is to assemble several steps that can be
    cross-validated together while setting different parameters.
    For this, it enables setting parameters of the various steps using their
    names and the parameter name separated by a '__', as in the example below.

    Parameters
    ----------
    steps : list
        List of (name, transform) tuples (implementing
        fit/transform/fit_sample) that are chained, in the order in which they
        are chained, with the last object an estimator.

    Attributes
    ----------
    named_steps : dict
        Read-only attribute to access any step parameter by user given name.
        Keys are step names and values are steps parameters.

    """

    # BaseEstimator interface

    def __init__(self, steps):
        names, estimators = zip(*steps)
        if len(dict(steps)) != len(steps):
            raise ValueError("Provided step names are not unique: %s"
                             % (names,))

        # shallow copy of steps
        self.steps = tosequence(steps)
        transforms = estimators[:-1]
        estimator = estimators[-1]

        for t in transforms:
            if (not (hasattr(t, "fit") or hasattr(t, "fit_transform") or
                     hasattr(t, "fit_sample")) or
                    not (hasattr(t, "transform") or hasattr(t, "sample"))):
                raise TypeError("All intermediate steps of the chain should "
                                "be transforms and implement fit and transform"
                                " '%s' (type %s) doesn't)" % (t, type(t)))

        if not hasattr(estimator, "fit"):
            raise TypeError("Last step of chain should implement fit "
                            "'%s' (type %s) doesn't)"
                            % (estimator, type(estimator)))

    # Estimator interface

    def _pre_transform(self, X, y=None, **fit_params):
        fit_params_steps = dict((step, {}) for step, _ in self.steps)
        for pname, pval in six.iteritems(fit_params):
            step, param = pname.split('__', 1)
            fit_params_steps[step][param] = pval
        Xt = X
        yt = y
        for name, transform in self.steps[:-1]:
            if hasattr(transform, "fit_transform"):
                Xt = transform.fit_transform(Xt, yt, **fit_params_steps[name])
            elif hasattr(transform, "fit_sample"):
                Xt, yt = transform.fit_sample(Xt, yt, **fit_params_steps[name])
            else:
                Xt = transform.fit(Xt, yt, **fit_params_steps[name]) \
                              .transform(Xt)
        return Xt, yt, fit_params_steps[self.steps[-1][0]]

    def fit(self, X, y=None, **fit_params):
        """Fit all the transforms and samples one after the other and transform
        the data, then fit the transformed data using the final estimator.

        Parameters
        ----------
        X : iterable
            Training data. Must fulfill input requirements of first step of the
            pipeline.
        y : iterable, default=None
            Training targets. Must fulfill label requirements for all steps of
            the pipeline.
        """
        Xt, yt, fit_params = self._pre_transform(X, y, **fit_params)
        self.steps[-1][-1].fit(Xt, yt, **fit_params)
        return self

    def fit_transform(self, X, y=None, **fit_params):
        """Fit all the transforms and samples one after the other and
        transform or sample the data, then use fit_transform on
        transformed data using the final estimator.

        Parameters
        ----------
        X : iterable
            Training data. Must fulfill input requirements of first step of the
            pipeline.

        y : iterable, default=None
            Training targets. Must fulfill label requirements for all steps of
            the pipeline.
        """
        Xt, yt, fit_params = self._pre_transform(X, y, **fit_params)
        if hasattr(self.steps[-1][-1], 'fit_transform'):
            return self.steps[-1][-1].fit_transform(Xt, yt, **fit_params)
        else:
            return self.steps[-1][-1].fit(Xt, yt, **fit_params).transform(Xt)

    @if_delegate_has_method(delegate='_final_estimator')
    def fit_sample(self, X, y=None, **fit_params):
        """Fit all the transforms and samples one after the other and
        transform or sample the data, then use fit_sample on
        transformed data using the final estimator.

        Parameters
        ----------
        X : iterable
            Training data. Must fulfill input requirements of first step of the
            pipeline.

        y : iterable, default=None
            Training targets. Must fulfill label requirements for all steps of
            the pipeline.
        """
        Xt, yt, fit_params = self._pre_transform(X, y, **fit_params)
        return self.steps[-1][-1].fit_sample(Xt, yt, **fit_params)

    @if_delegate_has_method(delegate='_final_estimator')
    def sample(self, X, y):
        """Applies transforms to the data, and the sample method of
        the final estimator. Valid only if the final estimator
        implements sample.

        Parameters
        ----------
        X : iterable
            Data to predict on. Must fulfill input requirements of first step
            of the pipeline.
        """
        Xt = X
        for _, transform in self.steps[:-1]:
            if hasattr(transform, "fit_sample"):
                pass
            else:
                Xt = transform.transform(Xt)
        return self.steps[-1][-1].sample(Xt, y)

    @if_delegate_has_method(delegate='_final_estimator')
    def predict(self, X):
        """Applies transforms to the data, and the predict method of
        the final estimator. Valid only if the final estimator
        implements predict.

        Parameters
        ----------
        X : iterable
            Data to predict on. Must fulfill input requirements of first step
            of the pipeline.
        """
        Xt = X
        for _, transform in self.steps[:-1]:
            if hasattr(transform, "fit_sample"):
                pass
            else:
                Xt = transform.transform(Xt)
        return self.steps[-1][-1].predict(Xt)

    @if_delegate_has_method(delegate='_final_estimator')
    def fit_predict(self, X, y=None, **fit_params):
        """Applies fit_predict of last step in pipeline after transforms
        and samples.

        Applies fit_transforms or fit_samples of a pipeline to the data,
        followed by the fit_predict method of the final estimator in the
        pipeline. Valid only if the final estimator implements fit_predict.

        Parameters
        ----------
        X : iterable
            Training data. Must fulfill input requirements of first step of
            the pipeline.
        y : iterable, default=None
            Training targets. Must fulfill label requirements for all steps
            of the pipeline.
        """
        Xt, yt, fit_params = self._pre_transform(X, y, **fit_params)
        return self.steps[-1][-1].fit_predict(Xt, yt, **fit_params)

    @if_delegate_has_method(delegate='_final_estimator')
    def predict_proba(self, X):
        """Applies transforms to the data, and the predict_proba method of the
        final estimator. Valid only if the final estimator implements
        predict_proba.

        Parameters
        ----------
        X : iterable
            Data to predict on. Must fulfill input requirements of first step
            of the pipeline.
        """
        Xt = X
        for _, transform in self.steps[:-1]:
            if hasattr(transform, "fit_sample"):
                pass
            else:
                Xt = transform.transform(Xt)
        return self.steps[-1][-1].predict_proba(Xt)

    @if_delegate_has_method(delegate='_final_estimator')
    def decision_function(self, X):
        """Applies transforms to the data, and the decision_function method of
        the final estimator. Valid only if the final estimator implements
        decision_function.

        Parameters
        ----------
        X : iterable
            Data to predict on. Must fulfill input requirements of first step
            of the pipeline.
        """
        Xt = X
        for _, transform in self.steps[:-1]:
            if hasattr(transform, "fit_sample"):
                pass
            else:
                Xt = transform.transform(Xt)
        return self.steps[-1][-1].decision_function(Xt)

    @if_delegate_has_method(delegate='_final_estimator')
    def predict_log_proba(self, X):
        """Applies transforms to the data, and the predict_log_proba method of
        the final estimator. Valid only if the final estimator implements
        predict_log_proba.

        Parameters
        ----------
        X : iterable
            Data to predict on. Must fulfill input requirements of first step
            of the pipeline.
        """
        Xt = X
        for _, transform in self.steps[:-1]:
            if hasattr(transform, "fit_sample"):
                pass
            else:
                Xt = transform.transform(Xt)
        return self.steps[-1][-1].predict_log_proba(Xt)

    @if_delegate_has_method(delegate='_final_estimator')
    def transform(self, X):
        """Applies transforms to the data, and the transform method of the
        final estimator. Valid only if the final estimator implements
        transform.

        Parameters
        ----------
        X : iterable
            Data to predict on. Must fulfill input requirements of first step
            of the pipeline.
        """
        Xt = X
        for _, transform in self.steps:
            if hasattr(transform, "fit_sample"):
                pass
            else:
                Xt = transform.transform(Xt)
        return Xt

    @if_delegate_has_method(delegate='_final_estimator')
    def inverse_transform(self, X):
        """Applies inverse transform to the data.
        Starts with the last step of the pipeline and applies
        ``inverse_transform`` in inverse order of the pipeline steps.
        Valid only if all steps of the pipeline implement inverse_transform.

        Parameters
        ----------
        X : iterable
            Data to inverse transform. Must fulfill output requirements of the
            last step of the pipeline.
        """
        if X.ndim == 1:
            warn("From version 0.19, a 1d X will not be reshaped in"
                 " pipeline.inverse_transform any more.", FutureWarning)
            X = X[None, :]
        Xt = X
        for _, step in self.steps[::-1]:
            if hasattr(step, "fit_sample"):
                pass
            else:
                Xt = step.inverse_transform(Xt)
        return Xt

    @if_delegate_has_method(delegate='_final_estimator')
    def score(self, X, y=None):
        """Applies transforms to the data, and the score method of the
        final estimator. Valid only if the final estimator implements
        score.

        Parameters
        ----------
        X : iterable
            Data to score. Must fulfill input requirements of first step of the
            pipeline.

        y : iterable, default=None
            Targets used for scoring. Must fulfill label requirements for all
            steps of the pipeline.
        """
        Xt = X
        for _, transform in self.steps[:-1]:
            if hasattr(transform, "fit_sample"):
                pass
            else:
                Xt = transform.transform(Xt)
        return self.steps[-1][-1].score(Xt, y)


def make_pipeline(*steps):
    """Construct a Pipeline from the given estimators.

    This is a shorthand for the Pipeline constructor; it does not require, and
    does not permit, naming the estimators. Instead, their names will be set
    to the lowercase of their types automatically.

    Returns
    -------
    p : Pipeline
    """
    return Pipeline(pipeline._name_estimators(steps))
