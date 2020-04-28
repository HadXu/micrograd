# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     demo
   Description :
   Author :       haxu
   date：          2020-04-28
-------------------------------------------------
   Change Activity:
                   2020-04-28:
-------------------------------------------------
"""
__author__ = 'haxu'

import random
import numpy as np

from micrograd.engine import Value
from micrograd.nn import Neuron, Layer, MLP

np.random.seed(1337)
random.seed(1337)

from sklearn.datasets import make_moons, make_blobs

X, y = make_moons(n_samples=100, noise=0.1)

y = y * 2 - 1

if __name__ == '__main__':
    model = MLP(2, [16, 16, 1])


    def loss(batch_size=None):
        if batch_size is None:
            Xb, yb = X, y
        else:
            ri = np.random.permutation(X.shape[0])[:batch_size]
            Xb, yb = X[ri], y[ri]
        inputs = [list(map(Value, xrow)) for xrow in Xb]

        # forward the model to get scores
        scores = list(map(model, inputs))

        # svm "max-margin" loss
        losses = [(1 + -yi * scorei).relu() for yi, scorei in zip(yb, scores)]
        data_loss = sum(losses) * (1.0 / len(losses))
        # L2 regularization
        alpha = 1e-4
        reg_loss = alpha * sum((p * p for p in model.parameters()))
        total_loss = data_loss + reg_loss

        # also get accuracy
        accuracy = [(yi > 0) == (scorei.data > 0) for yi, scorei in zip(yb, scores)]
        return total_loss, sum(accuracy) / len(accuracy)


    total_loss, acc = loss()
    print(total_loss, acc)

    for k in range(100):
        total_loss, acc = loss()

        model.zero_grad()

        total_loss.backward()

        learning_rate = 1.0 - 0.9 * k / 100
        for p in model.parameters():
            p.data -= learning_rate * p.grad

        print(f"step {k} loss {total_loss.data}, accuracy {acc * 100}%")
