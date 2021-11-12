from statistics import mean
from math import sqrt
from random import random
import matplotlib.pyplot as plt
import numpy as np



def expected_value(stock_return_vec):
    return mean(stock_return_vec)

# takes in a vector of the overall share of each stock in your portfolio,
# and a list of lists with the returns of each stock
#the lengths of these vectors should be equivalent
def expected_return_port(weights, stock_vecs):
    means = []
    for i in range(len(stock_vecs)):
        means.append(mean(stock_vecs[i]))
    return np.dot(means,weights)


def risk_port(weights, stock_vecs):
    return sqrt(np.dot(np.dot(np.cov(stock_vecs),weights),weights))

def randWeights(size):
    list = []
    total = 0
    for i in range(size):
        num = random()
        list.append(num)
        total += num
    for i in range(size):
        list[i] = list[i]/total
    return list

def makeFrontier(stock_vecs):
    returns = []
    stdev = []
    w = []
    for i in range(6000):
        weights = randWeights(len(stock_vecs))
        returns.append(expected_return_port(weights, stock_vecs))
        stdev.append(risk_port(weights, stock_vecs))
        w.append(weights)
    plt.scatter(stdev, returns)
    plt.title("Efficient Frontier")
    plt.xlabel("risk")
    plt.ylabel("return")
    plt.show()
    
def port_ret_cml(risk_free,market_vec, stock_vecs, weights):
    val = risk_free + (risk_port(weights, stock_vecs)*(expected_value(market_vec)-risk_free))/(np.var(market_vec))
    return val

def makeCML_ef(stock_vecs, risk_free,market_vec):
    returns_1 = []
    stdev_1 = []
    w_1 = []
    for i in range(6000):
        weights = randWeights(len(stock_vecs))
        returns_1.append(port_ret_cml(risk_free,market_vec, stock_vecs, weights))
        stdev_1.append(risk_port(weights, stock_vecs))
        w_1.append(weights)
    returns = []
    stdev = []
    w = []
    for i in range(6000):
        weights = randWeights(len(stock_vecs))
        returns.append(expected_return_port(weights, stock_vecs))
        stdev.append(risk_port(weights, stock_vecs))
        w.append(weights)
    plt.scatter(stdev_1, returns_1)
    plt.scatter(stdev, returns)
    plt.title("Efficient Frontier + CML")
    plt.xlabel("risk")
    plt.ylabel("return")
    plt.show()