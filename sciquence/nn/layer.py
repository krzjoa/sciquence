# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta


class Layer(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def forward(self, input):
        pass

