import math
import pandas as pd
import EvaluateResults
import numpy as np

def GreedyAlgorithm(radius):
    """
    Packing tasks by using Greedy Algorithm
    :param radius: optimal radius
    :return: DataFrame of each task point and corresponding clustering center point index
    """
    data = pd.read_excel("Data/Tasks.xlsx", "Sheet1")
    order = data.iloc[:,1:]
    order['Index'] = 0
    orderlen = len(order)

    distance = np.full((orderlen,orderlen), fill_value=0, dtype="float")

    for i in range(orderlen):
        for j in range(i + 1, orderlen):
            distance[i,j] = distance[j, i] = math.sqrt((order.iloc[i, 0] - order.iloc[j, 0]) ** 2 + (order.iloc[i, 1] - order.iloc[j, 1]) ** 2)

    while 1:
        density = np.array([],dtype="int")
        for k in range(len(distance)):
            density = np.append(density,len(np.where(distance[k,:] <= radius)[0]))
        index = np.argmax(density)
        length = density[index]
        maxRowDensity = np.where(distance[index,:] <= radius)[0]

        distance[:, maxRowDensity] = 10000000000000000
        order.iloc[maxRowDensity, 4] = index + 1
        order.iloc[index, 4] = -1

        if length <= 1 :
            break

    return order

EvaluateResults.EvaluateResults(GreedyAlgorithm(0.045)).to_excel("Result/GreedyAlgorithm.xlsx", index=False)
