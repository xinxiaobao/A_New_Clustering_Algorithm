from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

def KMeansAlgorithm(K):
    """
    Packing tasks by K-means Algorithm
    :param K: the number of clustering
    :return: DataFrame of the number of sub-task in each task
    """
    loan_data=pd.DataFrame(pd.read_excel('Data/Tasks.xlsx'))
    loan = np.array(loan_data[['Latitude of Task','Longitude of Task']])
    clf=KMeans(n_clusters=K)
    clf=clf.fit(loan)

    print(clf.cluster_centers_)
    loan_data['label']=clf.labels_

    result = []
    for i in range(K):
        count = 0
        sum = 0
        s = 0
        for j in range(len(loan_data)):
            if (i == loan_data.loc[j, 'label']):
                count = count + 1
                sum = sum + loan_data.loc[j, 'Task Pricing']
                s = s + loan_data.loc[j, 'Task Completion status']
        result.append([i,count,sum,s])
    df = pd.DataFrame(result)
    df.rename(columns={0: 'id', 1: 'count', 2: 'price', 3: 'complete'}, inplace=True)
    return df

KMeansAlgorithm(300).to_excel("Result/KMeansAlgorithm.xlsx", index=False)



