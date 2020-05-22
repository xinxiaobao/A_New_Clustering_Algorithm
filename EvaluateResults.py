import numpy as np
import pandas as pd

def EvaluateResults(united):
    """
    Evaluate packing results, and calculate the number of sub-task and the sum of completion and price in each package
    :param united: the result executed by GreedyAlgorithm.py and NewClusteringAlgorithm.py
    :return: DataFrame of the number of sub-task in each task
    """
    output_args = pd.DataFrame(columns=('id','count','price','complete'))
    tmp1 = np.where(united["Index"] == -1)[0]
    tmp2 = np.where(united["Index"] == 0)[0]
    for u in range(len(tmp1)):
        count = 1
        sum = united.iloc[tmp1[u], 2]
        s = united.iloc[tmp1[u], 3]
        for v in range(len(united)):
            if tmp1[u]+1 == united.iloc[v, 4]:
                sum = sum + united.iloc[v, 2]
                s = s + united.iloc[v, 3]
                count = count + 1
        output_args.loc[u, 'id'] = tmp1[u]+1
        output_args.loc[u, 'count'] = count
        output_args.loc[u, 'price'] = sum
        output_args.loc[u, 'complete'] = s

    for w in range(len(tmp2)):
        output_args.loc[w + len(tmp1), 'id'] = tmp2[w]+1
        output_args.loc[w + len(tmp1), 'count'] = 1
        output_args.loc[w + len(tmp1), 'price'] = united.iloc[tmp2[w], 2]
        output_args.loc[w + len(tmp1), 'complete'] = united.iloc[tmp2[w], 3]

    return output_args