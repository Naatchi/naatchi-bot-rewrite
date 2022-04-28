import numpy

def softmax(x):
    proba = numpy.exp(-x)
    return proba/sum(proba)
