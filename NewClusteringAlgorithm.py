import math
import pandas as pd
import EvaluateResults
import numpy as np

def NewClusteringAlgorithm(minDistant):
    """
    Packing tasks by using New Clustering Algorithm
    :param minDistant: optimal radius
    :return: DataFrame of each task point and corresponding clustering center point index
    """
    data = pd.read_excel("Data/Tasks.xlsx", "Sheet1")
    order = data.iloc[:,1:]
    order['Index'] = 0
    orderlen = len(order)

    distance = np.full((orderlen,orderlen), fill_value=10000000000000000, dtype="float")

    for i in range(orderlen):
        for j in range(i + 1, orderlen):
            distance[i,j] = math.sqrt((order.iloc[i, 0] - order.iloc[j, 0]) ** 2 + (order.iloc[i, 1] - order.iloc[j, 1]) ** 2)

    minD = np.min(distance)
    minDx = np.where(distance==minD)[0][0]
    minDy = np.where(distance==minD)[1][0]
    while(minD <= minDistant):
        order.iloc[minDx, 4] = -1
        order.iloc[minDy, 4] = minDx + 1
        distance[:, minDy] = 10000000000000000
        distance[:, minDx] = 10000000000000000
        distance[minDy, :] = 10000000000000000
        minD = np.min(distance)
        minDx = np.where(distance == minD)[0][0]
        minDy = np.where(distance == minD)[1][0]

    return order

EvaluateResults.EvaluateResults(NewClusteringAlgorithm(0.045)).to_excel("Result/NewClusteringAlgorithm.xlsx", index=False)