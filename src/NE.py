import numpy as np
from softmax import softmax
from sklearn.neighbors import BallTree
from sklearn.base import BaseEstimator


class NESampler(BaseEstimator):
    def __init__(self, k=5, temp=1.0):
        self.y = None
        self.tree = None
        self.k = k
        self.temp = temp

    def fit(self, val1, y):
        self.tree = BallTree(val1)
        self.y = np.array(y)

    def predict(self, val1):
        distances, ind = self.tree.query(val1, return_distance=True, k=self.k)
        result = []
        for distances, index in zip(distances, ind):
            result.append(np.random.choice(index, p=softmax(distances * self.temp)))

        return self.y[result]

