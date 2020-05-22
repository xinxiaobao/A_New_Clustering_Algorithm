import matplotlib.pyplot as plt
import numpy as np
from sklearn import  linear_model
import pandas as pd
from sklearn.preprocessing import  PolynomialFeatures

def Correlation(file):
    """
    Conduct regression between different radius and corresponding coefficient of correlation
    :param file: the excel path output from executed OptimalRadius.py
    :return: Tuple of coefficients and intercept of regression model
    """
    data = pd.read_excel(file)
    cor = data.corr()[999]
    df = pd.DataFrame(cor)
    df.to_excel("Result/Correlation.xlsx", header=False)

    datasets_X = list(map(float,cor.index.tolist()))
    datasets_X.pop()
    datasets_Y = cor.values.tolist()
    datasets_Y.pop()
    length =len(datasets_X)
    datasets_X= np.array(datasets_X).reshape([length,1])
    datasets_Y=np.array(datasets_Y)

    minX =min(datasets_X)
    maxX =max(datasets_X)
    X=np.arange(minX,maxX).reshape([-1,1])
    poly_reg =PolynomialFeatures(degree=2)
    X_ploy =poly_reg.fit_transform(datasets_X)
    lin_reg_2=linear_model.LinearRegression()
    lin_reg_2.fit(X_ploy,datasets_Y)

    plt.scatter(datasets_X,datasets_Y,color='red')
    plt.plot(X,lin_reg_2.predict(poly_reg.fit_transform(X)),color='blue')
    plt.xlabel('Radius')
    plt.ylabel('Correlation')
    plt.show()
    return (lin_reg_2.coef_, lin_reg_2.intercept_)

correlation = Correlation("Result/OptimalRadius.xlsx")
print('Coefficients:', correlation[0])
print('Intercept:',correlation[1])