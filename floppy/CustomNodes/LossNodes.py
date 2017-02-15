from floppy.node import Node, Input, Output, Loss

import chainer
from chainer import functions


class SoftmaxCrossEntropy(Loss):
    Input('in_array', chainer.Variable)
    Input('ground_truth', chainer.Variable)

    def call(self):
        return "functions.softmax_cross_entropy({0}, {1})".format(self._in_array, self._ground_truth)

