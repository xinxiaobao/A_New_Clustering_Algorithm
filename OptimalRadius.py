import pandas as pd
import numpy as np

def OptimalRadius(start, step, finish):
    """
    Calculate the density of users
    :param start: initial value of radius
    :param step: changed step of radius
    :param finish: final value of radius
    :return: DataFrame of the number of members around the task under different radius
    """
    person = pd.read_excel("Data/Users.xlsx", "Sheet1").iloc[:,1:]
    order = pd.read_excel("Data/Tasks.xlsx", "Sheet1").iloc[:,1:]
    tmp = 0
    cols = int((((finish+step)-start)/step)+1)
    result = np.empty(shape=[len(order)+1, cols], dtype="float")

    for k in np.arange(start, finish+step, step):
        if k == finish+step:
            break
        radius = k ** 2
        result[0, tmp] = k
        for i in range(len(order)):
            count = 0
            for j in range(len(person)):
                if (order.iloc[i, 0] - person.iloc[j, 0]) ** 2 + (order.iloc[i, 1] - person.iloc[j, 1]) ** 2 <= radius:
                    count = count + 1
            result[i+1, tmp] = count
        tmp = tmp + 1
    result[0, cols-1] = 999
    result[1:, cols-1] = order.iloc[:, 2]
    pd.DataFrame(result)
    return pd.DataFrame(result)

OptimalRadius(0.001,0.001,0.1).to_excel("Result/OptimalRadius.xlsx",header=False,index=False)