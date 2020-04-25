# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     engine
   Description :
   Author :       haxu
   date：          2020-04-25
-------------------------------------------------
   Change Activity:
                   2020-04-25:
-------------------------------------------------
"""
__author__ = 'haxu'


class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data

        self.grad = 0

        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')

        def _backward():
            self.grad += out.grad
            other.grad += out.grad

        out._backward = _backward

        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        out._backward = _backward
        return out
